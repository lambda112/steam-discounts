from utilsmeta.get_html import render_javascript_meta


divs = render_javascript_meta(5)
for d in divs:
    title = d.css_first("div[data-title] > h3 > span + span").text()
    meta_score = d.css_first("div[class *= 'ReviewScore'] > span").text()
    meta_page = f'https://www.metacritic.com{d.css_first("a").attributes.get("href")}'

    meta_game = {
        "title": title,
        "meta_score": meta_score,
        "meta_page": meta_page
    }

    print(meta_game)