from selectolax.parser import Node
import pandas as pd
import re


def clean_review(text:str, pattern):

    if isinstance(text, int):
        return text
    
    return int("".join(re.findall(pattern, text)))


def process_data(attrs:dict):

    processed_data = {
        "thumbnail": lambda link: link.attributes.get("src"),
        "review_num": lambda raw: clean_review(raw, r"\d+"),
        "steam_page": lambda link: link.attributes.get("href")
    }

    for k,v in processed_data.items():
        if k in attrs:
            attrs[k] = v(attrs[k])

    return attrs

def create_excel(data:list[dict], filename: str = "SteamData"):
    df = pd.DataFrame(data)
    df.to_excel(f"{filename}.xlsx", index = False)