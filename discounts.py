from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
from time import sleep
import pandas as pd

url = "https://store.steampowered.com/specials/"

# Return Full HTML
def render_javascript():

    with sync_playwright() as file:

        browser = file.chromium.launch(headless = True)
        page = browser.new_page()
        page.goto(url)

        page.wait_for_load_state("networkidle", timeout = 90000)
        print("Loaded Browser")

        for i in range(0,10):
            page.evaluate("() => window.scroll(0, document.body.scrollHeight)")
            page.evaluate("() => window.scroll(0, document.body.scrollHeight)")
            page.locator('button:text("Show more")').click()
            page.evaluate("() => window.scroll(0, document.body.scrollHeight)")
            print("Scrolled")
            sleep(1)

        page.wait_for_selector("div[class *= 'StoreSaleWidgetContainer']", timeout = 90000)
        print("Got Selector")

        tree = HTMLParser(page.inner_html("body"))
        divs = tree.css("div[class *= 'StoreSaleWidgetContainer']")

        return divs

div = render_javascript()
data = []

for d in div:
    title = d.css_first("div[class *= 'StoreSaleWidgetTitle']").text()
    old_price = d.css_first("div[class *= 'StoreOriginalPrice']").text()
    new_price = d.css_first("div[class *= 'StoreSalePriceBox']").text()
    
    if d.css_first("div[class *= 'ReviewScoreValue'] > div"):
        review_score = d.css_first("div[class *= 'ReviewScoreValue'] > div").text()
        review_num = d.css_first("div[class *= 'ReviewScoreValue'] > div + div").text()
    else:
        review_score = 0
        review_num = 0

    attrs = {
        "title": title,
        "new_price": new_price,
        "old_price": old_price,
        "review_score": review_score,
        "review_num": review_num
    }

    data.append(attrs)

pd.DataFrame(data).to_excel("SaleData.xlsx")