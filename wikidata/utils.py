import requests

def fetchData(searchQuery=""):
    url = "https://www.wikidata.org/w/api.php"

    params = {
        "action": "wbsearchentities",
        "format": "json",
        "search": searchQuery,
        "language": "en"
    }

    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET",
        "Access-Control-Allow-Headers": "Content-Type"
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    final_data = []
    for entity in data["search"]:
        item = {}
        item['label'] = entity['label']
        item['description'] = entity['description']
        item['url'] = entity['url'] 
        item['wd_id'] = entity['title']
        final_data.append(item)
    return final_data