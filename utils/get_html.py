from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
from time import sleep


url = "https://store.steampowered.com/specials/"

# Return Full HTML
def render_javascript():

    with sync_playwright() as file:

        browser = file.chromium.launch(headless = True)
        page = browser.new_page()
        page.goto(url)

        page.wait_for_load_state("networkidle", timeout = 90000)
        print("Loaded Browser")

        for i in range(0, 2):
            page.evaluate("() => window.scroll(0, document.body.scrollHeight)")
            page.evaluate("() => window.scroll(0, document.body.scrollHeight)")
            page.locator(selector="button[class *= 'saleitembrowser']", has_text="Show more").click()
            page.evaluate("() => window.scroll(0, document.body.scrollHeight)")
            print(f"Scrolled {i}")
            sleep(1)

        page.wait_for_selector("div[class *= 'StoreSaleWidgetContainer']", timeout = 90000)
        print("Got Selector")

        tree = HTMLParser(page.inner_html("body"))
        divs = tree.css("div[class *= 'StoreSaleWidgetContainer']")

        return divs
