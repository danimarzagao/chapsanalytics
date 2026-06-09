"""Playwright automation for O&S (Organizações & Sociedade) OJS submission."""
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent
LOGS = ROOT / "logs"
LOGS.mkdir(exist_ok=True)

OJS_URL = "https://www.revistaoes.ufba.br"


def submit_to_ojs(art_id: str, art: dict) -> dict:
    from playwright.sync_api import sync_playwright

    manuscript_path = str(ROOT / art["file"])
    secrets = _get_secrets()
    username = secrets["username"]
    password = secrets["password"]
    create_account = not username

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=120)
        ctx = browser.new_context()
        page = ctx.new_page()
        page.set_default_timeout(120_000)

        try:
            page.goto(OJS_URL)
            page.wait_for_load_state("networkidle")

            if create_account:
                _register_account(page, art)
                username = art["author_email"]
            else:
                _login(page, username, password)

            # Navigate to new submission
            page.goto(f"{OJS_URL}/index.php/revistaoes/submission/wizard")
            page.wait_for_load_state("networkidle")

            # Step 1 — Start submission / select section
            _select_section(page, art.get("article_type", "Artigo"))
            _accept_checklist(page)
            _click_save_continue(page)

            # Step 2 — Upload file
            page.wait_for_load_state("networkidle")
            _upload_file(page, manuscript_path, "article-text")
            _click_save_continue(page)

            # Step 3 — Metadata
            page.wait_for_load_state("networkidle")
            title = art.get("title_pt") or art.get("title_en", "")
            abstract = art.get("abstract_pt") or art.get("abstract_en", "")
            keywords = art.get("keywords_pt") or art.get("keywords_en", [])

            page.fill('input[name*="title"], input[id*="title"]', title)

            abstract_field = page.query_selector(
                'textarea[name*="abstract"], div[class*="ck-content"][contenteditable="true"]'
            )
            if abstract_field:
                abstract_field.click()
                abstract_field.fill(abstract.strip())

            for kw in keywords:
                kw_input = page.query_selector(
                    'input[name*="keyword"], input[class*="keyword"], input[placeholder*="palavra" i]'
                )
                if kw_input:
                    kw_input.fill(kw)
                    page.keyboard.press("Enter")

            _click_save_continue(page)

            # Step 4 — Contributors (confirm existing author)
            page.wait_for_load_state("networkidle")
            _click_save_continue(page)

            # Step 5 — Review & submit
            page.wait_for_load_state("networkidle")
            screenshot_review = str(LOGS / f"OS_{art_id}_review.png")
            page.screenshot(path=screenshot_review)

            submit_btn = page.query_selector(
                'button:has-text("Submit"), input[value*="Submit"], button:has-text("Submeter")'
            )
            if submit_btn:
                submit_btn.click()
                page.wait_for_load_state("networkidle")

            # Confirm modal if present
            confirm_btn = page.query_selector('button:has-text("OK"), button:has-text("Confirmar")')
            if confirm_btn:
                confirm_btn.click()
                page.wait_for_load_state("networkidle")

            confirm_screenshot = str(LOGS / f"OS_{art_id}_confirmation.png")
            page.screenshot(path=confirm_screenshot)

            manuscript_id = _extract_submission_id(page)

            return {
                "success": True,
                "manuscript_id": manuscript_id,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "screenshot": confirm_screenshot,
            }

        except Exception as exc:
            error_screenshot = str(LOGS / f"OS_{art_id}_error.png")
            try:
                page.screenshot(path=error_screenshot)
            except Exception:
                pass
            raise RuntimeError(f"OJS submission failed: {exc}") from exc

        finally:
            browser.close()


def _get_secrets() -> dict:
    return {
        "username": os.environ.get("OS_USERNAME", ""),
        "password": os.environ.get("OS_PASSWORD", ""),
    }


def _register_account(page, art: dict) -> None:
    print("  [O&S] Criando nova conta OJS...")
    page.goto(f"{OJS_URL}/index.php/revistaoes/user/register")
    page.wait_for_load_state("networkidle")

    name_parts = art["author_full_name"].split()
    first = name_parts[0] if name_parts else ""
    last = " ".join(name_parts[1:]) if len(name_parts) > 1 else first

    page.fill('input[name="givenName"]', first)
    page.fill('input[name="familyName"]', last)
    page.fill('input[name="email"]', art["author_email"])
    page.fill('input[name="username"]', art["author_email"].split("@")[0])

    password = os.environ.get("OS_PASSWORD", "")
    if not password:
        import getpass
        password = getpass.getpass("  Escolha uma senha para a conta OJS UFBA: ")
        os.environ["OS_PASSWORD"] = password

    page.fill('input[name="password"]', password)
    page.fill('input[name="password2"]', password)

    affiliation = page.query_selector('input[name*="affiliation"], input[name*="institution"]')
    if affiliation:
        affiliation.fill(art["author_institution"])

    country_sel = page.query_selector('select[name*="country"]')
    if country_sel:
        try:
            country_sel.select_option(label="Brazil")
        except Exception:
            try:
                country_sel.select_option(value="BR")
            except Exception:
                pass

    reviewer_checkbox = page.query_selector('input[name*="reviewer"], input[id*="reviewer"]')
    if reviewer_checkbox and reviewer_checkbox.is_checked():
        reviewer_checkbox.uncheck()

    register_btn = page.query_selector('button[type="submit"], input[value*="Register"]')
    if register_btn:
        register_btn.click()
        page.wait_for_load_state("networkidle")

    print("  [O&S] Conta criada. Verifique o e-mail se necessário para ativação.")


def _login(page, username: str, password: str) -> None:
    page.goto(f"{OJS_URL}/index.php/revistaoes/login")
    page.wait_for_load_state("networkidle")
    page.fill('input[name="username"]', username)
    page.fill('input[name="password"]', password)
    page.click('button[type="submit"], input[type="submit"]')
    page.wait_for_load_state("networkidle")


def _select_section(page, section_name: str) -> None:
    sel = page.query_selector('select[name*="sectionId"], select[id*="section"]')
    if sel:
        try:
            sel.select_option(label=section_name)
        except Exception:
            pass


def _accept_checklist(page) -> None:
    checkboxes = page.query_selector_all('input[type="checkbox"][name*="checklist"]')
    for cb in checkboxes:
        if not cb.is_checked():
            cb.check()


def _upload_file(page, file_path: str, genre: str = "article-text") -> None:
    upload_btn = page.query_selector('button:has-text("Upload"), a:has-text("Upload"), input[type="file"]')
    if not upload_btn:
        return

    if upload_btn.get_attribute("type") == "file":
        upload_btn.set_input_files(file_path)
    else:
        with page.expect_file_chooser() as fc:
            upload_btn.click()
        fc.value.set_files(file_path)

    page.wait_for_load_state("networkidle")

    genre_sel = page.query_selector('select[name*="genre"], select[id*="genre"]')
    if genre_sel:
        try:
            genre_sel.select_option(value=genre)
        except Exception:
            pass

    continue_btn = page.query_selector('button:has-text("Continue"), button:has-text("Continuar")')
    if continue_btn:
        continue_btn.click()
        page.wait_for_load_state("networkidle")

    complete_btn = page.query_selector('button:has-text("Complete"), button:has-text("Concluir")')
    if complete_btn:
        complete_btn.click()
        page.wait_for_load_state("networkidle")


def _click_save_continue(page) -> None:
    for selector in [
        'button:has-text("Save and Continue")',
        'button:has-text("Salvar e Continuar")',
        'button:has-text("Continue")',
        'button:has-text("Continuar")',
        'button[type="submit"]',
    ]:
        btn = page.query_selector(selector)
        if btn and btn.is_visible():
            btn.click()
            page.wait_for_load_state("networkidle")
            return


def _extract_submission_id(page) -> str:
    for selector in ['[class*="submission"], [id*="submission"]', 'strong', 'h3', 'h2']:
        elements = page.query_selector_all(selector)
        for el in elements:
            text = el.inner_text().strip()
            if any(c.isdigit() for c in text) and len(text) < 40:
                return text
    return page.url.split("/")[-1] or "unknown"
