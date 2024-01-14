from selectolax.parser import Node

def process_data(attrs:dict):

    processed_data = {
        "thumbnail": lambda x: x.attributes.get("src")
    }

    for k,v in processed_data.items():
        
        if k in attrs:
            attrs[k] = v(attrs[k])

    return attrs