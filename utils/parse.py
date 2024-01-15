from selectolax.parser import Node

def parse_data(node: Node, selectors: list):
    
    parsed = {}
    for s in selectors:
        name = s.get("name")
        type = s.get("type")
        selector = s.get("selector")
        method = s.get("method")

        if type == "first":
            matched = node.css_first(selector)

            if method == "text" and matched != None:
                parsed[name] = matched.text()

            elif matched is None:
                parsed[name] = 0

            else:    
                parsed[name] = matched

        if type == "all":
            matched = node.css(selector)

            if method == "text" and matched != None:
                parsed[name] = [i.text() for i in matched]

            elif matched is None:
                parsed[name] = 0

            else:
                parsed[name] = matched


    return parsed 


    # for d in div:
    #     title = d.css_first("div[class *= 'StoreSaleWidgetTitle']").text()
    #     old_price = d.css_first("div[class *= 'StoreOriginalPrice']").text()
    #     new_price = d.css_first("div[class *= 'StoreSalePriceBox']").text()

    #     if d.css_first("div[class *= 'ReviewScoreValue'] > div"):
    #         review_score = d.css_first("div[class *= 'ReviewScoreValue'] > div").text()
    #         review_num = d.css_first("div[class *= 'ReviewScoreValue'] > div + div").text()
    #     else:
    #         review_score = 0
    #         review_num = 0

    # attrs = {
    # "title": title,
    # "new_price": new_price,
    # "old_price": old_price,
    # "review_score": review_score,
    # "review_num": review_num
    # }
