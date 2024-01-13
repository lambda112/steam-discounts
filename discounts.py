from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
import pandas as pd


# Return Full HTML
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


# Parse HTML
def get_element(element):
    html = render_javascript(element)
    tree = HTMLParser(html)
    return tree.css(element)


# Get Game Title 
def get_game_title():
    title = [i.attrs["alt"] for i in get_element("a.Focusable > div > img")]
    print(f"Done Title {len(title)}")
    return title


# Get New Price
def get_new_price():
    new_price = [i.text() for i in get_element("a.Focusable span > div > div > div + div")]
    print(f"Done Price {len(new_price)}")
    return new_price


# Get Original Price
def get_original_price():
    original = [i.text() for i in get_element("a.Focusable span > div > div > div:first-child")]
    print(f"Done Price {len(original)}")
    return original


# Get Discount Percentage
def get_discount_percentage():
    discount_percentage = [i.text() for i in get_element("a.Focusable span > div > div:first-child")]
    print(f"Done Discount {len(discount_percentage)}")
    return discount_percentage


# Get Game Image 
def get_game_img():
    img = [i.attrs["src"] for i in get_element("a.Focusable > div + div > img")]
    print(f"Done Img {len(img)}")
    return img


# Create Pandas Dataframe with Game Data
def sale_data():

    data = {
        "Title": get_game_title(),
        "New_Price": get_new_price(),
        "Old_Price": get_original_price(),
        "Percentage": get_discount_percentage(),
        "Image": get_game_img()
    }

    sale_info = pd.DataFrame(data)
    return sale_info.to_excel("SaleData.xlsx", index = False)


url = "https://store.steampowered.com/specials"
sale_data()
