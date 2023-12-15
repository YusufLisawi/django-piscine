import sys
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://en.wikipedia.org/'

road_to_philosophy = []

def fetch_wiki(subject: str):
    try:
        res = requests.get(url=BASE_URL+subject)
        res.raise_for_status()
    except requests.HTTPError() as e:
        raise e

    parse_html(res.text)

def parse_html(html: str):
    global road_to_philosophy

    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find(id='firstHeading').find('span').contents[0]
    if title in road_to_philosophy:
        raise Exception('It leads to an infinite loop !')

    road_to_philosophy.append(title)
    print(title)

    if title == 'Philosophy': 
        return
    p_tags = soup.find(id='mw-content-text').find_all('p')
    a_tags = []
    for p in p_tags:
        if len(a_tags := p.find_all('a')) != 0:
            break
    if len(a_tags) == 0:
        raise Exception("It's a dead end !")
    if a_tags[0].get('href') is not None and a_tags[0]['href'].startswith('/wiki/') and not a_tags[0]['href'].startswith('/wiki/Wikipedia:') and not a_tags[0]['href'].startswith('/wiki/Help:'):
        return fetch_wiki(a_tags[0]['href'])
    raise Exception("It's a dead end !")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid arguments")
        exit(1)
    
    try:
        fetch_wiki('wiki/' + sys.argv[1])
        print(f'{len(road_to_philosophy)} roads from {sys.argv[1]} to philosophy !')
    except Exception as e:
        print(e)