"""Loads config.yaml + .env, validates required fields, exposes helpers."""
import os
import sys
import yaml
from pathlib import Path

ROOT = Path(__file__).parent.parent


def _load_env(env_path: Path) -> None:
    if not env_path.exists():
        return
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip())


def load(env_file: Path | None = None) -> dict:
    _load_env(env_file or ROOT / ".env")

    config_path = ROOT / "config.yaml"
    if not config_path.exists():
        sys.exit(f"ERROR: config.yaml not found at {config_path}")

    with open(config_path) as f:
        config = yaml.safe_load(f)

    config["secrets"] = {
        "rae_username": os.environ.get("RAE_USERNAME", ""),
        "rae_password": os.environ.get("RAE_PASSWORD", ""),
        "orcid_id": os.environ.get("ORCID_ID", ""),
        "os_username": os.environ.get("OS_USERNAME", ""),
        "os_password": os.environ.get("OS_PASSWORD", ""),
        "elsevier_email": os.environ.get("ELSEVIER_EMAIL", ""),
        "elsevier_password": os.environ.get("ELSEVIER_PASSWORD", ""),
    }

    return config


def validate(config: dict, articles: list[str] | None = None) -> None:
    """Validate that required fields are present. Raises ValueError listing gaps."""
    errors = []
    author = config.get("author", {})

    for field in ("first_name", "last_name", "email", "institution", "phone"):
        if not author.get(field, "").strip():
            errors.append(f"author.{field} is empty in config.yaml")

    if not author.get("orcid", "").strip():
        errors.append("author.orcid is empty (required by RAE ScholarOne)")

    secrets = config.get("secrets", {})
    targets = articles or list(config.get("articles", {}).keys())

    for art_id in targets:
        art = config["articles"].get(art_id, {})
        journal = art.get("journal", "")
        title = art.get("title_pt") or art.get("title_en", "")

        if not title.strip():
            errors.append(f"articles.{art_id}: title is empty")

        abstract = art.get("abstract_pt") or art.get("abstract_en", "")
        if not abstract.strip():
            errors.append(f"articles.{art_id}: abstract is empty")

        keywords_key = "keywords_pt" if art.get("language") == "pt" else "keywords_en"
        if not art.get(keywords_key):
            errors.append(f"articles.{art_id}: {keywords_key} is empty")

        file_path = ROOT / art.get("file", "")
        if not file_path.exists():
            errors.append(f"articles.{art_id}: file not found at {file_path}")

        if journal == "RAE":
            if not secrets["rae_username"]:
                errors.append("RAE_USERNAME missing in .env")
            if not secrets["rae_password"]:
                errors.append("RAE_PASSWORD missing in .env")
            if not secrets["orcid_id"]:
                errors.append("ORCID_ID missing in .env")
            if art.get("area_rae", "").strip() == "":
                errors.append(f"articles.{art_id}: area_rae is empty (required by ScholarOne)")
            supp = ROOT / config["journals"]["RAE"].get("supplemental", "")
            if not supp.exists():
                errors.append(
                    f"RAE supplemental file not found: {supp}\n"
                    "  Download the Open Science Compliance Form from the RAE website\n"
                    "  and save it to supplemental/RAE_Open_Science_Compliance_Form.docx"
                )

        elif journal == "OS":
            pass  # OS_USERNAME can be blank — script will register a new account

        elif journal == "JBR":
            if not secrets["elsevier_email"]:
                errors.append("ELSEVIER_EMAIL missing in .env")
            if not secrets["elsevier_password"]:
                errors.append("ELSEVIER_PASSWORD missing in .env")

    if errors:
        raise ValueError("Configuration incomplete:\n" + "\n".join(f"  • {e}" for e in errors))


def get_article(config: dict, art_id: str) -> dict:
    art = config["articles"][art_id]
    author = config["author"]
    full_name = f"{author['first_name']} {author['last_name']}".strip()
    return {
        **art,
        "author_full_name": full_name,
        "author_email": author["email"],
        "author_institution": author["institution"],
        "author_orcid": config["secrets"]["orcid_id"] or author.get("orcid", ""),
        "author_country": author.get("country", "Brazil"),
        "author_phone": author.get("phone", ""),
        "journal_config": config["journals"][art["journal"]],
        "cover_letter_text": _render_cover_letter(ROOT / art["cover_letter"], author),
    }


def _render_cover_letter(path: Path, author: dict) -> str:
    if not path.exists():
        return ""
    full_name = f"{author['first_name']} {author['last_name']}".strip()
    text = path.read_text(encoding="utf-8")
    return (
        text
        .replace("{AUTHOR_FULL_NAME}", full_name)
        .replace("{INSTITUTION}", author.get("institution", ""))
        .replace("{EMAIL}", author.get("email", ""))
    )
