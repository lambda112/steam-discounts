from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser


def render_javascript(url, element):
    TIMEOUT = 90000

    with sync_playwright() as file:
        browser = file.chromium.launch(headless = False)
        page = browser.new_page()
        page.goto(url)

        page.wait_for_load_state("networkidle", timeout = TIMEOUT)
        page.wait_for_selector(element, timeout = TIMEOUT)
        return page.inner_html("body")


def get_element(html, element):
    tree = HTMLParser(html)
    return [i.text() for i in tree.css(element)]

def get_discount_percentage():
    html = render_javascript("https://store.steampowered.com/specials", "span > div > div:first-child")
    discount_percentage = get_element(html, "span > div > div:first-child")
    return discount_percentage

print(get_discount_percentage())
    
