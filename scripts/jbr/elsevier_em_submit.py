"""Playwright automation for JBR via Elsevier's new submission portal (submit.elsevier.com)."""
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent
LOGS = ROOT / "logs"
LOGS.mkdir(exist_ok=True)

SUBMIT_URL = "https://submit.elsevier.com/JOBR"
LOGIN_URL = "https://id.elsevier.com/as/authorization.oauth2"


def submit_to_elsevier_em(art_id: str, art: dict) -> dict:
    from playwright.sync_api import sync_playwright

    manuscript_path = str(ROOT / art["file"])
    email = os.environ.get("ELSEVIER_EMAIL", "")
    password = os.environ.get("ELSEVIER_PASSWORD", "")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=150)
        ctx = browser.new_context()
        page = ctx.new_page()
        page.set_default_timeout(120_000)

        try:
            # Step 1 — Navigate to journal portal
            print("  [JBR] Acessando submit.elsevier.com/JOBR...")
            page.goto(SUBMIT_URL)
            page.wait_for_load_state("networkidle")

            # Step 2 — Login
            _login(page, email, password)

            # Step 3 — Start new submission
            print("  [JBR] Iniciando nova submissão...")
            page.wait_for_load_state("networkidle")
            _click_any(page, [
                'button:has-text("Submit new manuscript")',
                'button:has-text("New submission")',
                'a:has-text("Submit new manuscript")',
                'a:has-text("New submission")',
                '[data-testid="new-submission"]',
            ])
            page.wait_for_load_state("networkidle")

            # Step 4 — Article type
            _select_article_type(page, art.get("article_type", "Full Length Article"))
            page.wait_for_load_state("networkidle")

            # Step 5 — Title
            title = art.get("title_en") or art.get("title_pt", "")
            print(f"  [JBR] Preenchendo título...")
            _fill_any(page, [
                'input[name*="title" i]',
                'textarea[name*="title" i]',
                '[data-testid*="title"]',
                'input[placeholder*="title" i]',
            ], title)
            _click_next(page)

            # Step 6 — Abstract
            abstract = art.get("abstract_en") or art.get("abstract_pt", "")
            print("  [JBR] Preenchendo abstract...")
            _fill_rich_text(page, abstract.strip())
            _click_next(page)

            # Step 7 — Keywords
            keywords = art.get("keywords_en") or art.get("keywords_pt", [])
            print("  [JBR] Adicionando keywords...")
            _add_keywords(page, keywords)
            _click_next(page)

            # Step 8 — Upload manuscript
            print("  [JBR] Fazendo upload do manuscrito...")
            page.wait_for_load_state("networkidle")
            _upload_file(page, manuscript_path)
            _click_next(page)

            # Step 9 — Author information
            page.wait_for_load_state("networkidle")
            print("  [JBR] Verificando dados do autor...")
            _fill_author_info(page, art)
            _click_next(page)

            # Step 10 — AI declaration
            page.wait_for_load_state("networkidle")
            if art.get("ai_declaration"):
                print("  [JBR] Marcando declaração de uso de IA...")
                _handle_ai_declaration(page)
            _click_next(page)

            # Step 11 — Review and submit
            page.wait_for_load_state("networkidle")
            screenshot_review = str(LOGS / f"JBR_{art_id}_review.png")
            page.screenshot(path=screenshot_review)
            print("  [JBR] Revisando e submetendo...")

            _click_any(page, [
                'button:has-text("Submit")',
                'button:has-text("Submit manuscript")',
                'button:has-text("Submit to journal")',
                '[data-testid*="submit"]',
            ])
            page.wait_for_load_state("networkidle")

            # Confirm dialog if present
            _click_any(page, [
                'button:has-text("Confirm")',
                'button:has-text("OK")',
                'button:has-text("Yes")',
            ], required=False)
            page.wait_for_load_state("networkidle")

            confirm_screenshot = str(LOGS / f"JBR_{art_id}_confirmation.png")
            page.screenshot(path=confirm_screenshot)

            submission_id = _extract_submission_id(page)
            print(f"  [JBR] ✓ Submetido. ID: {submission_id}")

            return {
                "success": True,
                "submission_id": submission_id,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "screenshot": confirm_screenshot,
            }

        except Exception as exc:
            error_screenshot = str(LOGS / f"JBR_{art_id}_error.png")
            try:
                page.screenshot(path=error_screenshot)
            except Exception:
                pass
            raise RuntimeError(f"JBR submission failed: {exc}") from exc

        finally:
            browser.close()


def _login(page, email: str, password: str) -> None:
    print("  [JBR] Fazendo login na Elsevier...")

    # Look for login/sign-in button on the portal
    login_clicked = _click_any(page, [
        'button:has-text("Sign in")',
        'button:has-text("Log in")',
        'a:has-text("Sign in")',
        'a:has-text("Log in")',
        '[data-testid*="login"]',
        '[data-testid*="signin"]',
    ], required=False)

    page.wait_for_load_state("networkidle")

    # Fill email/username
    _fill_any(page, [
        'input[type="email"]',
        'input[name*="email" i]',
        'input[name*="username" i]',
        'input[id*="email" i]',
        'input[placeholder*="email" i]',
    ], email)

    # Some portals have a two-step login (email first, then password)
    _click_any(page, [
        'button:has-text("Continue")',
        'button:has-text("Next")',
        'input[type="submit"]',
    ], required=False)
    page.wait_for_load_state("networkidle")

    # Fill password
    _fill_any(page, [
        'input[type="password"]',
        'input[name*="password" i]',
        'input[id*="password" i]',
    ], password)

    _click_any(page, [
        'button[type="submit"]',
        'button:has-text("Sign in")',
        'button:has-text("Log in")',
        'input[type="submit"]',
    ])
    page.wait_for_load_state("networkidle")

    # Handle "create account" scenario
    if page.query_selector('text=Create account, text=Register, text=New user'):
        print("\n  ⚠ Conta não encontrada. Criando nova conta Elsevier...")
        _register_new_account(page, email, password)


def _register_new_account(page, email: str, password: str) -> None:
    _click_any(page, [
        'button:has-text("Create account")',
        'a:has-text("Register")',
        'button:has-text("Register")',
    ], required=False)
    page.wait_for_load_state("networkidle")

    _fill_any(page, ['input[name*="firstName" i], input[id*="firstName" i]'], "Daniela")
    _fill_any(page, ['input[name*="lastName" i], input[id*="lastName" i]'], "Marzagão")
    _fill_any(page, ['input[type="email"]'], email)
    _fill_any(page, ['input[type="password"]', 'input[name*="password"]'], password)

    _click_any(page, ['button[type="submit"]', 'button:has-text("Create")'])
    page.wait_for_load_state("networkidle")

    print("\n  ⚠ AÇÃO NECESSÁRIA: Verifique o e-mail e confirme a conta Elsevier.")
    input("  Pressione Enter quando a verificação estiver concluída: ")
    page.reload()
    page.wait_for_load_state("networkidle")


def _select_article_type(page, article_type: str) -> None:
    selectors = [
        'select[name*="type" i]',
        '[data-testid*="article-type"]',
        'button:has-text("Article type")',
    ]
    for sel in selectors:
        el = page.query_selector(sel)
        if el and el.is_visible():
            tag = el.evaluate("el => el.tagName.toLowerCase()")
            if tag == "select":
                try:
                    el.select_option(label=article_type)
                except Exception:
                    el.select_option(index=1)
            else:
                el.click()
                page.wait_for_load_state("networkidle")
                option = page.query_selector(f'li:has-text("{article_type}"), option:has-text("{article_type}")')
                if option:
                    option.click()
            return

    _click_next(page)


def _fill_rich_text(page, text: str) -> None:
    selectors = [
        'div[contenteditable="true"]',
        'textarea[name*="abstract" i]',
        '.ql-editor',
        '[data-testid*="abstract"]',
        '.ProseMirror',
    ]
    for sel in selectors:
        el = page.query_selector(sel)
        if el and el.is_visible():
            el.click()
            el.fill(text)
            return


def _add_keywords(page, keywords: list) -> None:
    for kw in keywords:
        input_el = page.query_selector(
            'input[name*="keyword" i], input[placeholder*="keyword" i], '
            'input[data-testid*="keyword"], input[placeholder*="Add keyword" i]'
        )
        if input_el and input_el.is_visible():
            input_el.fill(kw)
            page.keyboard.press("Enter")
            page.wait_for_timeout(300)


def _upload_file(page, file_path: str) -> None:
    # Try direct file input
    file_input = page.query_selector('input[type="file"]')
    if file_input:
        file_input.set_input_files(file_path)
        page.wait_for_load_state("networkidle")
        return

    # Try upload button
    with page.expect_file_chooser(timeout=10_000) as fc:
        _click_any(page, [
            'button:has-text("Upload")',
            'button:has-text("Add file")',
            'button:has-text("Choose file")',
            'label:has-text("Upload")',
        ])
    fc.value.set_files(file_path)
    page.wait_for_load_state("networkidle")


def _fill_author_info(page, art: dict) -> None:
    name_parts = art["author_full_name"].split()
    first = name_parts[0] if name_parts else ""
    last = " ".join(name_parts[1:]) if len(name_parts) > 1 else first

    _fill_any(page, ['input[name*="firstName" i]', 'input[id*="firstName" i]'], first, required=False)
    _fill_any(page, ['input[name*="lastName" i]', 'input[id*="lastName" i]'], last, required=False)
    _fill_any(page, ['input[name*="affiliation" i]', 'input[name*="institution" i]'], art["author_institution"], required=False)
    orcid_input = page.query_selector('input[name*="orcid" i], input[placeholder*="orcid" i]')
    if orcid_input and orcid_input.is_visible():
        orcid_input.fill(art.get("author_orcid", ""))


def _handle_ai_declaration(page) -> None:
    for selector in [
        'input[type="checkbox"][name*="ai" i]',
        'input[type="checkbox"][id*="ai" i]',
        'label:has-text("Artificial Intelligence") >> input[type="checkbox"]',
        'label:has-text("AI tools") >> input[type="checkbox"]',
        'label:has-text("generative AI") >> input[type="checkbox"]',
    ]:
        try:
            cb = page.query_selector(selector)
            if cb and not cb.is_checked():
                cb.check()
                return
        except Exception:
            pass


def _click_next(page) -> None:
    _click_any(page, [
        'button:has-text("Next")',
        'button:has-text("Continue")',
        'button:has-text("Save and continue")',
        '[data-testid*="next"]',
        '[data-testid*="continue"]',
    ], required=False)
    page.wait_for_load_state("networkidle")


def _click_any(page, selectors: list, required: bool = True) -> bool:
    for sel in selectors:
        try:
            el = page.query_selector(sel)
            if el and el.is_visible():
                el.click()
                return True
        except Exception:
            pass
    if required:
        raise RuntimeError(f"Could not find any of: {selectors}")
    return False


def _fill_any(page, selectors: list, value: str, required: bool = True) -> bool:
    if not value:
        return False
    for sel in selectors:
        try:
            el = page.query_selector(sel)
            if el and el.is_visible():
                el.fill(value)
                return True
        except Exception:
            pass
    if required:
        raise RuntimeError(f"Could not find field for: {selectors}")
    return False


def _extract_submission_id(page) -> str:
    for selector in ['[class*="confirmation" i]', '[class*="submission" i]', 'h1', 'h2', 'strong']:
        for el in page.query_selector_all(selector):
            try:
                text = el.inner_text().strip()
                if any(c.isdigit() for c in text) and len(text) < 60:
                    return text
            except Exception:
                pass
    return page.url.split("/")[-1] or "unknown"
