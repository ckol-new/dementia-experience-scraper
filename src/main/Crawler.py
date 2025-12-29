import requests
from bs4 import BeautifulSoup
import json

# alzhiemer's connected crawler: https://alzconnected.org/categories/i-have-younger-onset-alzheimers

# return text of response
def request_page_html(url):
    header = {
    }
    try:

        response = requests.get(url, headers=header)
        if response.status_code == 200:
            pass
        else:
            code = response.status_code
            print(f'Request failed, status code: {code}')
    except requests.exceptions.RequestException as e:
        print(f'Request Error {e}')

    return response.text
    ...

def save_link_array(links, destination):
    link_dict = dict(enumerate(links))

    with open(destination, 'w') as f:
        json.dump(link_dict, f, indent=2)

    print(f'saved data to {destination}')

# crawl to find all /discussion/ containing hrefs
def crawl_ad_connect(starts, limit=None):
    discussion_links = set()
    distance_crawled = 0

    # from each starting point
    for base_url in starts:

        # access page html text
        response_txt = request_page_html(base_url)
        print(f'request for {base_url} was succesful')

        # get soup object
        soup = BeautifulSoup(response_txt, 'html.parser')
        print(f'soup object succesfully obtained')

        # get all /discussion/ containing links

        for link in soup.find_all('a'):
            if limit is None:
                pass
            elif distance_crawled > limit:
                break

            link_txt = link.get('href')

            if "/discussion/" not in link_txt:
                continue
                
            discussion_links.add(link_txt)
            distance_crawled += 1
            print(distance_crawled)
    
    # convert to array
    discussion_links = list(discussion_links)

    return discussion_links



def crawl_ad_connect_early_onset():
    STARTS = [
        'https://alzconnected.org/categories/i-have-younger-onset-alzheimers',
        'https://alzconnected.org/categories/i-have-younger-onset-alzheimers/p2',
        'https://alzconnected.org/categories/i-have-younger-onset-alzheimers/p3',
        'https://alzconnected.org/categories/i-have-younger-onset-alzheimers/p4',
        'https://alzconnected.org/categories/i-have-younger-onset-alzheimers/p5',
        'https://alzconnected.org/categories/i-have-younger-onset-alzheimers/p6',
        'https://alzconnected.org/categories/i-have-younger-onset-alzheimers/p7',
        'https://alzconnected.org/categories/i-have-younger-onset-alzheimers/p8',
        'https://alzconnected.org/categories/i-have-younger-onset-alzheimers/p9',
        'https://alzconnected.org/categories/i-have-younger-onset-alzheimers/p10',
              ]
    SAVE_DESTINATION = r'C:\Users\wslam\Everything\machine-learning\dementia-bot\src\data\crawler_output\ad_connect\crawled_ad_connect_early_onset.json'

    # crawl early onset
    links = crawl_ad_connect(STARTS)
    save_link_array(links, SAVE_DESTINATION)

def crawl_ad_connect_ad_or_others():
    STARTS = [
        'https://alzconnected.org/categories/i-have-alzheimers-or-other-dementia',
        'https://alzconnected.org/categories/i-have-alzheimers-or-other-dementia/p2',
        'https://alzconnected.org/categories/i-have-alzheimers-or-other-dementia/p3',
        'https://alzconnected.org/categories/i-have-alzheimers-or-other-dementia/p4',
        'https://alzconnected.org/categories/i-have-alzheimers-or-other-dementia/p5',
        'https://alzconnected.org/categories/i-have-alzheimers-or-other-dementia/p6',
        'https://alzconnected.org/categories/i-have-alzheimers-or-other-dementia/p7',
        'https://alzconnected.org/categories/i-have-alzheimers-or-other-dementia/p8',
        'https://alzconnected.org/categories/i-have-alzheimers-or-other-dementia/p9',
        'https://alzconnected.org/categories/i-have-alzheimers-or-other-dementia/p10',
        'https://alzconnected.org/categories/i-have-alzheimers-or-other-dementia/p11',
    ]

    SAVE_DESTINATION = r'C:\Users\wslam\Everything\machine-learning\dementia-bot\src\data\crawler_output\ad_connect\crawled_ad_connect_ad_or_others.json'

    # crawl early onset
    links = crawl_ad_connect(STARTS)
    save_link_array(links, SAVE_DESTINATION)