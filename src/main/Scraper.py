import requests
import json
from bs4 import BeautifulSoup
from Discussion import Discussion
from Discussion import Comment

def request_page_html(url):
    header = {
    }

    response = None
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


def get_discussion_title(soup):
    # get title, strip of suffix
    title = soup.title.string
    title = title.removesuffix(' \u2014 ALZConnected')
    return title

def get_discussion_content(soup):
    # get class=discussion, then get class=message, userCOntent
    text = []

    div_content = soup.find('div', class_="Message userContent")   
    for paragraph in div_content.find_all('p'):
        text.append(paragraph.string)

    if len(text) == 0:
        return text

    text = [t for t in text if t is not None] # get rid of None before joining
    text = '\n'.join(text)

    return text

# return comments object list
def get_discussion_comments(soup):
    comments = []

    for div_comment in soup.find_all('div', class_='Comment'):
        comment = div_comment.find('div', class_='Message userContent')
        comment_text = []
        if comment:
            for paragraph in comment.find_all('p'):
                comment_text.append(paragraph.string)


        # join comment text
        if len(comment_text) == 0:
            continue

        # join comment text to one string
        comment_text = [t for t in comment_text if t is not None] # get rid of None before joining
        comment_text = '\n'.join(comment_text)
        comment_obj = Comment(comment_text)

        # add to comment array
        comments.append(comment_obj)

    return comments


    



def get_ad_connect_discussion(url):
    # get response text
    response_text = request_page_html(url)
    #DEBUG
    print(f'sucesfully gotten response text for {url}')

    # get soup object
    soup = BeautifulSoup(response_text, 'html.parser')
    print(f'sucesfully gotten soup obj text for {url}')

    # get title
    title = get_discussion_title(soup)

    # get content: list of strings
    content = get_discussion_content(soup)
    #DEBUG
    print(f'succesfully gotten title and content for {url}')

    # get comments object list
    comments = get_discussion_comments(soup)
    #DEBUG
    print(f'succesfully gotten comments for {url}')

    # get discusson object
    discussion = Discussion(url, title, content, comments)
    #DEBUG
    print(f'succesfully gotten discussion obj for {url}')

    return discussion

def scrape_ad_connect(fpath, limit=None):
    # init list of discussion obj
    discussions = []

    # load file
    with open(fpath, 'r') as f:
        data_dict = json.load(f)
    
    # convert to list
    links = list(data_dict.values()) 

    num_scraped = 0
    for link in links:
        if limit:
            if num_scraped >= limit:
                break
        
        num_scraped += 1
        print(num_scraped)

        discussion = get_ad_connect_discussion(link)
        discussions.append(discussion)

    return discussions

# save as jsonl
def save_scraped_ad_connect(discussions, save_destination):
    with open(save_destination, 'w', encoding='utf-8') as f:
        for discussion in discussions:
            discussion_dict = discussion.to_dict()
            json.dump(discussion_dict, f)
            f.write('\n')


