from playwright.sync_api import sync_playwright

def crawl_dbpia(query: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.dbpia.co.kr/")

        page.fill("#query", query)
        page.keyboard.press("Enter")
        page.wait_for_selector(".thesis__title", timeout=5000)

        titles = page.locator(".thesis__title").all_text_contents()
        browser.close()
        return titles[:5]
