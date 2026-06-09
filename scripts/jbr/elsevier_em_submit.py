"""Playwright automation for JBR submission via Elsevier Editorial Manager."""
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent
LOGS = ROOT / "logs"
LOGS.mkdir(exist_ok=True)

EM_URL = "https://www.editorialmanager.com/jbr/"


def submit_to_elsevier_em(art_id: str, art: dict) -> dict:
    from playwright.sync_api import sync_playwright

    manuscript_path = str(ROOT / art["file"])
    secrets = _get_secrets()
    requires_registration = art["journal_config"].get("requires_account_creation", True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        ctx = browser.new_context()
        page = ctx.new_page()
        page.set_default_timeout(120_000)

        try:
            page.goto(EM_URL)
            page.wait_for_load_state("networkidle")

            if requires_registration:
                _register_elsevier(page, art, secrets)
            else:
                _login_elsevier(page, secrets)

            # Navigate to new submission
            submit_link = page.query_selector(
                'a:has-text("Submit New Manuscript"), a:has-text("New Submission")'
            )
            if submit_link:
                submit_link.click()
            else:
                page.goto(f"{EM_URL}#author")
                page.wait_for_load_state("networkidle")
                page.click('text=Submit New Manuscript')

            page.wait_for_load_state("networkidle")

            # Step 1 — Article type
            _select_if_visible(page, 'select[name*="artType"], select[id*="artType"]', "Full Length Article")
            _click_proceed(page)

            # Step 2 — Title and abstract
            title = art.get("title_en") or art.get("title_pt", "")
            abstract = art.get("abstract_en") or art.get("abstract_pt", "")
            page.fill('input[name*="title" i]:visible, textarea[name*="title" i]:visible', title)

            abstract_el = page.query_selector(
                'textarea[name*="abstract" i]:visible, '
                'div[class*="abstract"][contenteditable="true"]:visible'
            )
            if abstract_el:
                abstract_el.click()
                abstract_el.fill(abstract.strip())

            _click_proceed(page)

            # Step 3 — Keywords
            keywords = art.get("keywords_en") or art.get("keywords_pt", [])
            for kw in keywords:
                kw_input = page.query_selector(
                    'input[name*="keyword" i]:visible, textarea[name*="keyword" i]:visible'
                )
                if kw_input:
                    kw_input.fill(kw)
                    add_btn = page.query_selector('input[value*="Add"], button:has-text("Add")')
                    if add_btn:
                        add_btn.click()
                        page.wait_for_timeout(300)

            _click_proceed(page)

            # Step 4 — File upload
            page.wait_for_load_state("networkidle")
            _upload_em_file(page, manuscript_path)
            _click_proceed(page)

            # Step 5 — Additional information / AI declaration
            page.wait_for_load_state("networkidle")
            if art.get("ai_declaration"):
                _handle_ai_declaration(page)
            _click_proceed(page)

            # Step 6 — Author information (auto-filled from account)
            page.wait_for_load_state("networkidle")
            _click_proceed(page)

            # Step 7 — APC screen
            page.wait_for_load_state("networkidle")
            _handle_apc_screen(page, art["journal_config"].get("apc_usd", 4420))

            # Final review and submit
            page.wait_for_load_state("networkidle")
            screenshot_review = str(LOGS / f"JBR_{art_id}_review.png")
            page.screenshot(path=screenshot_review)

            submit_btn = page.query_selector(
                'input[value*="Submit to Journal"]:visible, '
                'button:has-text("Submit to Journal"):visible, '
                'input[value*="Submit Manuscript"]:visible'
            )
            if submit_btn:
                submit_btn.click()
                page.wait_for_load_state("networkidle")

            # Handle confirmation dialog
            ok_btn = page.query_selector('input[value="OK"], button:has-text("OK")')
            if ok_btn:
                ok_btn.click()
                page.wait_for_load_state("networkidle")

            confirm_screenshot = str(LOGS / f"JBR_{art_id}_confirmation.png")
            page.screenshot(path=confirm_screenshot)

            submission_id = _extract_em_submission_id(page)

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
            raise RuntimeError(f"Elsevier EM submission failed: {exc}") from exc

        finally:
            browser.close()


def _get_secrets() -> dict:
    return {
        "email": os.environ.get("ELSEVIER_EMAIL", ""),
        "password": os.environ.get("ELSEVIER_PASSWORD", ""),
    }


def _register_elsevier(page, art: dict, secrets: dict) -> None:
    print("  [JBR] Criando nova conta no Elsevier Editorial Manager...")

    reg_link = page.query_selector('a:has-text("Register"), a:has-text("Create Account")')
    if reg_link:
        reg_link.click()
        page.wait_for_load_state("networkidle")

    name_parts = art["author_full_name"].split()
    first = name_parts[0] if name_parts else ""
    last = " ".join(name_parts[1:]) if len(name_parts) > 1 else first

    _fill_visible(page, 'input[name*="firstName" i], input[id*="firstName" i]', first)
    _fill_visible(page, 'input[name*="lastName" i], input[id*="lastName" i]', last)
    _fill_visible(page, 'input[name*="email" i]', secrets["email"])
    _fill_visible(page, 'input[name*="institution" i], input[name*="affiliation" i]', art["author_institution"])
    _fill_visible(page, 'input[name*="phone" i]', art.get("author_phone", ""))
    _select_if_visible(page, 'select[name*="country" i]', "Brazil")
    _fill_visible(page, 'input[name*="password" i][name*="1"], input[id*="password1" i]', secrets["password"])
    _fill_visible(page, 'input[name*="password" i][name*="2"], input[id*="password2" i]', secrets["password"])

    submit_btn = page.query_selector('input[value*="Submit"], input[value*="Register"], button[type="submit"]')
    if submit_btn:
        submit_btn.click()
        page.wait_for_load_state("networkidle")

    print("\n  ⚠ AÇÃO NECESSÁRIA: Verifique seu e-mail e confirme a conta Elsevier.")
    input("  Pressione Enter quando a verificação de e-mail estiver concluída: ")
    page.wait_for_load_state("networkidle")

    _login_elsevier(page, secrets)


def _login_elsevier(page, secrets: dict) -> None:
    page.goto(EM_URL)
    page.wait_for_load_state("networkidle")
    login_link = page.query_selector('a:has-text("Login"), a:has-text("Log In"), input[value*="Login"]')
    if login_link:
        login_link.click()
        page.wait_for_load_state("networkidle")

    _fill_visible(page, 'input[name*="login" i], input[name*="username" i], input[type="email"]', secrets["email"])
    _fill_visible(page, 'input[name*="password" i][type="password"]', secrets["password"])
    page.keyboard.press("Enter")
    page.wait_for_load_state("networkidle")


def _upload_em_file(page, file_path: str) -> None:
    file_input = page.query_selector('input[type="file"]')
    if file_input:
        file_input.set_input_files(file_path)
        page.wait_for_load_state("networkidle")
    else:
        with page.expect_file_chooser() as fc:
            page.click('text=Attach, text=Upload, input[type="file"]')
        fc.value.set_files(file_path)
        page.wait_for_load_state("networkidle")

    attach_btn = page.query_selector('input[value*="Attach"], button:has-text("Attach")')
    if attach_btn:
        attach_btn.click()
        page.wait_for_load_state("networkidle")


def _handle_ai_declaration(page) -> None:
    for selector in [
        'input[type="checkbox"][name*="ai" i]',
        'input[type="checkbox"][id*="ai" i]',
        'input[type="checkbox"][name*="artificial" i]',
        'label:has-text("Artificial Intelligence") input',
        'label:has-text("AI") input',
    ]:
        checkbox = page.query_selector(selector)
        if checkbox and not checkbox.is_checked():
            checkbox.check()
            break


def _handle_apc_screen(page, apc_usd: int = 4420) -> None:
    continue_btn = page.query_selector(
        'input[value*="Continue"], button:has-text("Continue"), '
        'input[value*="Acknowledge"], button:has-text("I Understand")'
    )
    if continue_btn:
        continue_btn.click()
        page.wait_for_load_state("networkidle")


def _click_proceed(page) -> None:
    for selector in [
        'input[value="Proceed"]:visible',
        'input[value*="Next"]:visible',
        'button:has-text("Proceed"):visible',
        'button:has-text("Next"):visible',
        'input[value*="Continue"]:visible',
    ]:
        btn = page.query_selector(selector)
        if btn and btn.is_visible():
            btn.click()
            page.wait_for_load_state("networkidle")
            return


def _select_if_visible(page, selector: str, value: str) -> None:
    el = page.query_selector(selector)
    if el and el.is_visible():
        try:
            el.select_option(label=value)
        except Exception:
            try:
                el.select_option(value=value)
            except Exception:
                pass


def _fill_visible(page, selector: str, value: str) -> None:
    if not value:
        return
    el = page.query_selector(selector)
    if el and el.is_visible():
        el.fill(value)


def _extract_em_submission_id(page) -> str:
    for selector in ['[class*="manuscript" i]', '[id*="submission" i]', 'strong', 'b']:
        for el in page.query_selector_all(selector):
            text = el.inner_text().strip()
            if len(text) < 40 and any(c.isdigit() for c in text):
                return text
    return page.url.split("=")[-1] or "unknown"
