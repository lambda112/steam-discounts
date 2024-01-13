from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
import pandas as pd


def render_javascript(element):
    TIMEOUT = 90000

    with sync_playwright() as file:

        browser = file.chromium.launch(headless = True)
        page = browser.new_page()
        page.goto(url)

        page.wait_for_load_state("networkidle", timeout = TIMEOUT)
        print("Loaded Browser")

        page.wait_for_selector(element, timeout = TIMEOUT)
        print("Got Selector")

        return page.inner_html("body")


def get_element(element):
    html = render_javascript(element)
    tree = HTMLParser(html)
    return tree.css(element)


def get_game_title():
    title = [i.attrs["alt"] for i in get_element("a.Focusable > div > img")]
    print(f"Done Title {len(title)}")
    return title


def get_new_price():
    new_price = [i.text() for i in get_element("a.Focusable span > div > div > div + div")]
    print(f"Done Price {len(new_price)}")
    return new_price


def get_original_price():
    original = [i.text() for i in get_element("a.Focusable span > div > div > div:first-child")]
    print(f"Done Price {len(original)}")
    return original


def get_discount_percentage():
    discount_percentage = [i.text() for i in get_element("a.Focusable span > div > div:first-child")]
    print(f"Done Discount {len(discount_percentage)}")
    return discount_percentage


def sale_data():
    
    data = {
        "Title": get_game_title(),
        "New_Price": get_new_price(),
        "Old_Price": get_original_price(),
        "Percentage": get_discount_percentage()
    }

    return pd.DataFrame(data)

url = "https://store.steampowered.com/specials"
print(sale_data())
