from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser

def render_javascript(url):
    TIMEOUT = 90000

    with sync_playwright() as file:
        browser = file.chromium.launch(headless = False)
        page = browser.new_page()
        page.goto(url)

        page.wait_for_load_state("networkidle", timeout = TIMEOUT)
        page.wait_for_selector("span > div > div", timeout = TIMEOUT)
        return page.inner_html("body")
    
