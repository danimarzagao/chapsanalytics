"""Playwright automation for RAE ScholarOne submission."""
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent
LOGS = ROOT / "logs"
LOGS.mkdir(exist_ok=True)


def submit_to_scholarone(art_id: str, art: dict) -> dict:
    from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

    url = art["journal_config"]["url"]
    manuscript_path = str(ROOT / art["file"])
    supplemental_path = str(ROOT / art["journal_config"].get("supplemental", ""))
    secrets = _get_secrets()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=120)
        ctx = browser.new_context()
        page = ctx.new_page()
        page.set_default_timeout(120_000)

        try:
            # Step 1 — Login
            page.goto(url)
            page.wait_for_load_state("networkidle")
            page.fill('input[name="login"]', secrets["username"])
            page.fill('input[name="password"]', secrets["password"])
            page.click('input[type="submit"][value*="Log"]')
            page.wait_for_load_state("networkidle")

            # Step 2 — Navigate to Author Center → Start New Submission
            page.click('text=Author Center')
            page.wait_for_load_state("networkidle")
            page.click('text=Start New Submission')
            page.wait_for_load_state("networkidle")

            # Step 3 — Manuscript type and title
            title = art.get("title_pt") or art.get("title_en", "")
            _select_if_visible(page, 'select[name*="manuscriptType"]', art.get("article_type", "Ensaio Teórico"))
            page.fill('input[name*="title"], textarea[name*="title"]', title)
            _click_next(page)

            # Step 4 — File upload
            with page.expect_file_chooser() as fc_info:
                page.click('text=Browse, text=Choose File, input[type="file"]')
            fc_info.value.set_files(manuscript_path)
            _select_if_visible(page, 'select[name*="fileDesignation"]', "Main Document")
            _click_add_file(page)

            if os.path.exists(supplemental_path):
                with page.expect_file_chooser() as fc_info2:
                    page.click('text=Browse, text=Choose File, input[type="file"]')
                fc_info2.value.set_files(supplemental_path)
                _select_if_visible(page, 'select[name*="fileDesignation"]', "Supplemental File for Review")
                _click_add_file(page)

            _click_next(page)

            # Step 5 — Keywords + subject area
            keywords = art.get("keywords_pt") or art.get("keywords_en", [])
            for kw in keywords:
                kw_input = page.query_selector('input[name*="keyword"], input[placeholder*="keyword" i]')
                if kw_input:
                    kw_input.fill(kw)
                    add_btn = page.query_selector('input[value*="Add"], button:has-text("Add")')
                    if add_btn:
                        add_btn.click()

            area = art.get("area_rae", "")
            if area:
                _select_if_visible(page, 'select[name*="subjectArea"], select[name*="category"]', area)

            _click_next(page)

            # Step 6 — Author + ORCID
            orcid_input = page.query_selector('input[name*="orcid" i], input[placeholder*="orcid" i]')
            if orcid_input:
                orcid_input.fill(art.get("author_orcid", ""))
            _fill_if_empty(page, 'input[name*="firstName"], input[name*="first_name"]', art["author_full_name"].split()[0])
            _fill_if_empty(page, 'input[name*="lastName"], input[name*="last_name"]', art["author_full_name"].split()[-1])
            _fill_if_empty(page, 'input[name*="email"]', art["author_email"])
            _fill_if_empty(page, 'input[name*="institution"], input[name*="affiliation"]', art["author_institution"])
            _click_next(page)

            # Step 7 — Abstract
            abstract = art.get("abstract_pt") or art.get("abstract_en", "")
            abstract_field = page.query_selector('textarea[name*="abstract"], div[contenteditable="true"]')
            if abstract_field:
                abstract_field.fill(abstract.strip())
            _click_next(page)

            # Final step — Review and submit
            screenshot_path = str(LOGS / f"RAE_{art_id}_review.png")
            page.screenshot(path=screenshot_path)

            submit_btn = page.query_selector(
                'input[value*="Submit"][type="submit"], button:has-text("Submit Manuscript")'
            )
            if submit_btn:
                submit_btn.click()
                page.wait_for_load_state("networkidle")

            confirm_screenshot = str(LOGS / f"RAE_{art_id}_confirmation.png")
            page.screenshot(path=confirm_screenshot)

            # Extract manuscript ID from confirmation page
            manuscript_id = _extract_manuscript_id(page)

            return {
                "success": True,
                "manuscript_id": manuscript_id,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "screenshot": confirm_screenshot,
            }

        except Exception as exc:
            error_screenshot = str(LOGS / f"RAE_{art_id}_error.png")
            try:
                page.screenshot(path=error_screenshot)
            except Exception:
                pass
            raise RuntimeError(f"ScholarOne submission failed: {exc}") from exc

        finally:
            browser.close()


def _get_secrets() -> dict:
    return {
        "username": os.environ.get("RAE_USERNAME", ""),
        "password": os.environ.get("RAE_PASSWORD", ""),
    }


def _click_next(page) -> None:
    from playwright.sync_api import TimeoutError as PWTimeout
    for selector in [
        'input[value="Next >"]',
        'input[value*="Next"]',
        'button:has-text("Next")',
        'a:has-text("Next")',
    ]:
        btn = page.query_selector(selector)
        if btn and btn.is_visible():
            btn.click()
            page.wait_for_load_state("networkidle")
            return
    page.keyboard.press("Tab")


def _click_add_file(page) -> None:
    for selector in ['input[value*="Add"]', 'button:has-text("Add to List")', 'button:has-text("Upload")']:
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


def _fill_if_empty(page, selector: str, value: str) -> None:
    el = page.query_selector(selector)
    if el and el.is_visible():
        current = el.input_value() or ""
        if not current.strip():
            el.fill(value)


def _extract_manuscript_id(page) -> str:
    for selector in ['[class*="manuscript"], [id*="manuscript"]', 'strong', 'b']:
        elements = page.query_selector_all(selector)
        for el in elements:
            text = el.inner_text().strip()
            if "RAE" in text or "-" in text and len(text) < 30:
                return text
    return page.title()
