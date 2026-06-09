#!/usr/bin/env python3
"""
Orchestrates submission of 3 articles to 3 journals.

  A3 → RAE   (ScholarOne)     + Gmail draft backup
  A1 → O&S   (OJS UFBA)
  A2 → JBR   (Elsevier EM)

Usage:
  python3 scripts/run_all.py [--dry-run] [--only A1|A2|A3]
"""
import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import config_loader

STATE_PATH = ROOT / "state" / "submission_state.json"


def load_state() -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text())
    return {}


def save_state(state: dict) -> None:
    STATE_PATH.write_text(json.dumps(state, indent=2, ensure_ascii=False))


def mark(state: dict, art_id: str, status: str, **kwargs) -> None:
    entry = state.setdefault(art_id, {})
    entry["status"] = status
    entry.setdefault("journal", "")
    for k, v in kwargs.items():
        entry[k] = v
    save_state(state)


def ensure_playwright() -> None:
    try:
        import playwright  # noqa: F401
    except ImportError:
        print("Installing playwright...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
    result = subprocess.run(
        [sys.executable, "-m", "playwright", "install", "chromium"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0 and "already installed" not in result.stderr.lower():
        print(result.stdout)
        print(result.stderr)


def run_rae(art_config: dict, state: dict, dry_run: bool) -> bool:
    art_id = "A3"
    if state.get(art_id, {}).get("status") == "submitted":
        print(f"[A3→RAE] Já submetido. Pulando.")
        return True

    print(f"\n[A3→RAE] Submetendo ao ScholarOne...")
    if dry_run:
        print("  DRY-RUN: scholarone_submit.py seria executado aqui.")
        return True

    mark(state, art_id, "in_progress")
    try:
        from rae.scholarone_submit import submit_to_scholarone
        result = submit_to_scholarone(art_id, art_config)
        mark(state, art_id, "submitted",
             manuscript_id=result.get("manuscript_id"),
             submitted_at=result.get("timestamp"),
             portal_screenshot=result.get("screenshot"))
        print(f"  ✓ RAE: manuscrito ID = {result.get('manuscript_id')}")
        return True
    except Exception as exc:
        mark(state, art_id, "failed", notes=str(exc))
        print(f"  ✗ RAE falhou: {exc}")
        return False


def run_os(art_config: dict, state: dict, dry_run: bool) -> bool:
    art_id = "A1"
    if state.get(art_id, {}).get("status") == "submitted":
        print(f"[A1→O&S] Já submetido. Pulando.")
        return True

    print(f"\n[A1→O&S] Submetendo ao OJS UFBA...")
    if dry_run:
        print("  DRY-RUN: ojs_submit.py seria executado aqui.")
        return True

    mark(state, art_id, "in_progress")
    try:
        from os_ufba.ojs_submit import submit_to_ojs
        result = submit_to_ojs(art_id, art_config)
        mark(state, art_id, "submitted",
             manuscript_id=result.get("manuscript_id"),
             submitted_at=result.get("timestamp"),
             portal_screenshot=result.get("screenshot"))
        print(f"  ✓ O&S: ID = {result.get('manuscript_id')}")
        return True
    except Exception as exc:
        mark(state, art_id, "failed", notes=str(exc))
        print(f"  ✗ O&S falhou: {exc}")
        return False


def run_jbr(art_config: dict, state: dict, dry_run: bool) -> bool:
    art_id = "A2"
    if state.get(art_id, {}).get("status") == "submitted":
        print(f"[A2→JBR] Já submetido. Pulando.")
        return True

    print(f"\n[A2→JBR] Submetendo ao Elsevier Editorial Manager...")
    if dry_run:
        print("  DRY-RUN: elsevier_em_submit.py seria executado aqui.")
        return True

    mark(state, art_id, "in_progress")
    try:
        from jbr.elsevier_em_submit import submit_to_elsevier_em
        result = submit_to_elsevier_em(art_id, art_config)
        mark(state, art_id, "submitted",
             submission_id=result.get("submission_id"),
             submitted_at=result.get("timestamp"),
             portal_screenshot=result.get("screenshot"))
        print(f"  ✓ JBR: submission ID = {result.get('submission_id')}")
        return True
    except Exception as exc:
        mark(state, art_id, "failed", notes=str(exc))
        print(f"  ✗ JBR falhou: {exc}")
        return False


def print_summary(state: dict) -> None:
    print("\n" + "=" * 50)
    print("RESUMO DE SUBMISSÕES")
    print("=" * 50)
    labels = {"A3": "A3 → RAE (ScholarOne)", "A1": "A1 → O&S (OJS UFBA)", "A2": "A2 → JBR (Elsevier EM)"}
    for art_id, label in labels.items():
        entry = state.get(art_id, {})
        status = entry.get("status", "not_started")
        ms_id = entry.get("manuscript_id") or entry.get("submission_id") or "-"
        icon = "✓" if status == "submitted" else ("✗" if status == "failed" else "○")
        print(f"  {icon} {label}: {status} (ID: {ms_id})")
    print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Submit academic articles to journals.")
    parser.add_argument("--dry-run", action="store_true", help="Validate config and print plan without opening any browser.")
    parser.add_argument("--only", choices=["A1", "A2", "A3"], help="Submit only one article.")
    args = parser.parse_args()

    config = config_loader.load()
    articles_to_run = [args.only] if args.only else ["A3", "A1", "A2"]

    try:
        config_loader.validate(config, articles_to_run)
    except ValueError as e:
        print(f"\n{e}\n")
        print("Execute 'python3 scripts/setup_env.py' para configurar credenciais.")
        print("Edite config.yaml para preencher os campos de metadados.")
        sys.exit(1)

    if args.dry_run:
        print("\n=== DRY-RUN: Configuração válida. Plano de submissão: ===")
        for art_id in articles_to_run:
            art = config_loader.get_article(config, art_id)
            title = art.get("title_pt") or art.get("title_en")
            print(f"  • {art_id} → {art['journal']}: {title[:70]}...")
        print()

    if not args.dry_run:
        ensure_playwright()

    state = load_state()

    results = {}
    for art_id in articles_to_run:
        art_config = config_loader.get_article(config, art_id)
        if art_id == "A3":
            results["A3"] = run_rae(art_config, state, args.dry_run)
        elif art_id == "A1":
            results["A1"] = run_os(art_config, state, args.dry_run)
        elif art_id == "A2":
            results["A2"] = run_jbr(art_config, state, args.dry_run)

    print_summary(load_state())

    if not args.dry_run:
        failed = [k for k, v in results.items() if not v]
        if failed:
            print(f"Atenção: submissões com erro: {', '.join(failed)}")
            print("Verifique os screenshots em logs/ e o state file para detalhes.")
            sys.exit(1)


if __name__ == "__main__":
    main()
