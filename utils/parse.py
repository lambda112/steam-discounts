from selectolax.parser import Node

def parse_data(node: Node, selectors: list, meta_data:list[dict]):

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

