import datetime
import requests
import json
from bs4 import BeautifulSoup

now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")
url = 'https://rozetked.me/news'
path = "articles.json"
data = {

    "url": url,
    "creationDate": date,
    "articles": ["None"]
}



def get_html_page(url):
    rozetked = requests.get(url)
    rozetked_html = rozetked.text
    return (rozetked_html)


def find_articles(rozetked_html):
    titles = []
    rozetked_parsed = BeautifulSoup(rozetked_html,'html.parser')
    rozedked_article = rozetked_parsed.find_all(class_='post_new-title')
    for title in rozedked_article:
        titles.append(title.text.strip())
    return (titles)


def publish_report(path, articles):
    c = []
    for i in articles:
        d = {"title": i,
             "seconds": now.strftime("%S")}
        c.append(d)
    data["articles"] = c
    with open(path, "w",encoding="utf-8") as write_file:
        json.dump(data, write_file,indent = 2, ensure_ascii=False)
    return (data)


rozetked_html = get_html_page(url)
articles = find_articles(rozetked_html)
publish_report(path,articles)







