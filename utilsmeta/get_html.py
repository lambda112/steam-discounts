import requests as r
from time import sleep
from selectolax.parser import HTMLParser
from playwright.sync_api import sync_playwright

divs = []
url = "https://www.metacritic.com/browse/game/pc/all/all-time/metascore/?releaseYearMin=1958&releaseYearMax=2024&platform=pc&page="
def render_javascript_meta(n:int):

    for i in range(1,n):

        with sync_playwright() as file:
            print(f"PAGE{i}")
            browser = file.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto(f"{url}{i}")
            page.wait_for_load_state("networkidle")
            page.wait_for_load_state("domcontentloaded")
            sleep(1)

            html = page.inner_html("body")
            tree = HTMLParser(html)
            div = tree.css("div[class *= 'c-finderProductCard-game']")
            divs.extend(div)

    return divs