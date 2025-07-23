from playwright.sync_api import sync_playwright

def crawl_riss(query: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.riss.kr/")

        page.fill("input[name=query]", query)
        page.keyboard.press("Enter")
        page.wait_for_selector(".title", timeout=5000)

        titles = page.locator(".title").all_text_contents()
        browser.close()
        return titles[:5]
