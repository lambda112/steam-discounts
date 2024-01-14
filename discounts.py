import pandas as pd
from utils.get_html import render_javascript
from utils.parse import parse_data
from utils.process import process_data
from config.tools import get_config

if __name__ == "__main__":
    config = get_config()
    div = render_javascript()

    for d in div:
        attrs = parse_data(d, config.get("items"))
        attrs = process_data(attrs)
        print(attrs)