from playwright.sync_api import sync_playwright

def crawl_kci(query: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.kci.go.kr/kciportal/po/search/poArtiSear.kci")

        page.fill("input[name=poSearchBean.keyword]", query)
        page.keyboard.press("Enter")
        page.wait_for_timeout(5000)

        titles = page.locator(".list-title").all_text_contents()
        browser.close()
        return titles[:5]
