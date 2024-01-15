import pandas as pd
from utils.get_html import render_javascript
from utils.parse import parse_data
from utils.process import process_data
from utils.process import create_excel
from config.tools import get_config
from utilsmeta.get_html import render_javascript_meta


if __name__ == "__main__":

    config = get_config()
    game_in_meta = False

    div_steam = render_javascript(200)
    steam_data = []

    div_meta = render_javascript_meta(200)
    meta_data = []

    for d in div_meta:
        title = d.css_first("div[data-title] > h3 > span + span").text()
        meta_score = d.css_first("div[class *= 'ReviewScore'] > span").text()
        meta_page = f'https://www.metacritic.com{d.css_first("a").attributes.get("href")}'

        meta_game = {
            "title": title,
            "meta_score": meta_score,
            "meta_page": meta_page
        }

        meta_data.append(meta_game)
        

    for d in div_steam:
        attrs = parse_data(d, config.get("items"), meta_data)
        attrs = process_data(attrs)

        if attrs["title"] in [meta_game["title"] for meta_game in meta_data]:
            for meta_game in meta_data:
                
                if meta_game["title"] == attrs["title"]:
                    attrs["meta_score"] = meta_game["meta_score"]
                    attrs["meta_page"] = meta_game["meta_page"]
                    steam_data.append(attrs)
                    break  

            print(attrs["title"])
    

create_excel(steam_data, "Sales")


# pos = list(attrs.keys()).index('old_price')
# items = list(attrs.items())
# items.insert(pos, ('Phone', '123-456-7890'))
# mydict = dict(items)

# print(mydict)