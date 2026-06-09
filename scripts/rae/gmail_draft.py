"""Prepares Gmail draft payload for RAE email backup.

The actual MCP create_draft tool call must be invoked by the Claude Code agent,
not from this Python subprocess. This module generates the structured payload
and prints it as JSON so the orchestrator can act on it.
"""
import json
import sys
from pathlib import Path


def build_draft_payload(art: dict) -> dict:
    title = art.get("title_pt") or art.get("title_en", "")
    journal_email = art["journal_config"].get("email_backup", "raeredacao@fgv.br")
    cover = art.get("cover_letter_text", "")

    body = (
        f"{cover}\n\n"
        "---\n"
        "NOTA: Este e-mail é um backup de comunicação. A submissão formal foi realizada "
        "pelo portal ScholarOne em mc04.manuscriptcentral.com/rae-scielo.\n"
        "Caso deseje enviar o manuscrito por este canal também, "
        "adicione o arquivo .docx como anexo antes de enviar."
    )

    return {
        "to": journal_email,
        "subject": f"Submissão de Artigo: {title}",
        "body": body,
    }


if __name__ == "__main__":
    # When called directly, print payload JSON to stdout for the agent to consume
    import os
    sys.path.insert(0, str(Path(__file__).parent.parent))
    import config_loader

    config = config_loader.load()
    art = config_loader.get_article(config, "A3")
    payload = build_draft_payload(art)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
