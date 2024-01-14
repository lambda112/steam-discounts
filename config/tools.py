import json

_config = {
    "items":[
        {
            "name": "title",
            "type": "first",
            "selector": "div[class *= 'StoreSaleWidgetTitle']",
            "method": "text"
        },

        {
            "name": "old_price",
            "type": "first",
            "selector": "div[class *= 'StoreOriginalPrice']",
            "method": "text"
        },

        {
            "name": "new_price",
            "type": "first",
            "selector": "div[class *= 'StoreSalePriceBox']",
            "method": "text"
        },

        {
            "name": "review_score",
            "type": "first",
            "selector": "div[class *= 'ReviewScoreValue'] > div",
            "method": "text"
        },

        {
            "name": "review_num",
            "type": "first",
            "selector": "div[class *= 'ReviewScoreValue'] > div + div",
            "method": "text"
        },

        {
            "name": "thumbnail",
            "type": "first",
            "selector": "img[class *= 'CapsuleImage']",
            "method": "other"
        },
        
    ]
}

    # name
    # type of selector
    # selector
    # method

def generate_json():

    with open("config\config.json", "w") as f:
        json.dump(_config, f, indent = 4)


def get_config(load_from_file: bool = False):

    if load_from_file:
        with open("config\tools.py", "r") as f:
            return json.loads(f)
        
    return _config


if __name__ == "__main__":
    get_config(False)