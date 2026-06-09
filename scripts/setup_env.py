#!/usr/bin/env python3
"""Interactive setup: collects credentials and writes .env."""
import getpass
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
ENV_PATH = ROOT / ".env"


def prompt(label: str, default: str = "", secret: bool = False) -> str:
    suffix = f" [{default}]" if default and not secret else ""
    while True:
        if secret:
            value = getpass.getpass(f"{label}: ").strip()
        else:
            value = input(f"{label}{suffix}: ").strip()
        if value:
            return value
        if default:
            return default
        print("  (campo obrigatório)")


def main() -> None:
    print("\n=== Configuração de Credenciais para Submissão de Artigos ===\n")
    print("As informações serão salvas em .env (nunca commitado no git).\n")

    existing = {}
    if ENV_PATH.exists():
        with open(ENV_PATH) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, _, v = line.partition("=")
                    existing[k.strip()] = v.strip()
        print(f"Arquivo .env existente encontrado. Pressione Enter para manter valores atuais.\n")

    print("--- RAE (ScholarOne: mc04.manuscriptcentral.com/rae-scielo) ---")
    rae_user = prompt("Login ScholarOne (email)", existing.get("RAE_USERNAME", ""))
    rae_pass = prompt("Senha ScholarOne", secret=True)
    orcid = prompt("ORCID iD (ex: 0000-0002-xxxx-xxxx)", existing.get("ORCID_ID", ""))

    print("\n--- O&S (OJS UFBA: revistaoes.ufba.br) ---")
    print("Deixe em branco para criar nova conta automaticamente durante a submissão.")
    os_user = input("Login OJS UFBA (email, ou Enter para criar novo): ").strip()
    os_pass = ""
    if os_user:
        os_pass = prompt("Senha OJS UFBA", secret=True)

    print("\n--- JBR (Elsevier Editorial Manager) ---")
    print("Uma nova conta será criada com o e-mail abaixo.")
    elsevier_email = prompt("E-mail para conta Elsevier", existing.get("ELSEVIER_EMAIL", "daniela.marzagao@astrape.com.br"))
    elsevier_pass = prompt("Senha desejada para conta Elsevier", secret=True)

    lines = [
        "# Credenciais de submissão — NÃO commitar este arquivo\n",
        "\n# RAE / ScholarOne\n",
        f"RAE_USERNAME={rae_user}\n",
        f"RAE_PASSWORD={rae_pass}\n",
        f"ORCID_ID={orcid}\n",
        "\n# O&S / OJS UFBA\n",
        f"OS_USERNAME={os_user}\n",
        f"OS_PASSWORD={os_pass}\n",
        "\n# JBR / Elsevier Editorial Manager\n",
        f"ELSEVIER_EMAIL={elsevier_email}\n",
        f"ELSEVIER_PASSWORD={elsevier_pass}\n",
    ]

    with open(ENV_PATH, "w") as f:
        f.writelines(lines)

    print(f"\n✓ Credenciais salvas em {ENV_PATH}")
    print("\nPróximo passo: edite config.yaml para preencher os campos vazios")
    print("  - author.first_name, author.institution, author.phone")
    print("  - articles.A3.area_rae (seção da RAE)")
    print("\nDepois execute: python3 scripts/run_all.py --dry-run")


if __name__ == "__main__":
    main()
