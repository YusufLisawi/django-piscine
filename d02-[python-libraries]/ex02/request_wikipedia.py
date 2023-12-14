import requests
import sys
import json
import dewiki

BASE_API = "https://en.wikipedia.org/w/api.php"

def fetch_wiki(subject: str) -> str:
    PARAMS = {
            'action': 'parse',
            'format': 'json',
            'page': subject,
            'prop': 'wikitext',
        }

    try:
        res = requests.get(url=BASE_API, params=PARAMS)
        res.raise_for_status()
    except requests.HTTPError() as e:
        raise e

    data = res.json()
    if 'error' in data.keys():
        raise Exception(data['error']['info'])
    return dewiki.from_string(data["parse"]["wikitext"]["*"])

def write_to_file(filename: str, data: str) -> str:
    with open(filename + '.wiki', 'w') as f:
        f.write(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid arguments")
        exit(1)
    
    try:
        data = fetch_wiki(sys.argv[1])
        write_to_file(sys.argv[1], data)
    except Exception as e:
        print(e)

