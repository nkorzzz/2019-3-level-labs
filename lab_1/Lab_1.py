print("helo")
import datetime
now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")
print(date)
url = 'https://rozetked.me/news'
data = {

    "url": url,
    "creationDate": date,
    "articles": ["None"]
}
print(data)

import requests
import json
from bs4 import BeautifulSoup


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


def publish_report(articles):
    c = []
    for i in articles:
        d = {"title": i}
        c.append(d)
    data["articles"] = c
    with open("data_file.json", "w",encoding="utf-8") as write_file:
        json.dump(data, write_file)
    return (data)


rozetked_html = get_html_page(url)
articles = find_articles(rozetked_html)
publish_report(articles)
with open("data_file.json", "r") as read_file:
    data1 = json.load(read_file)
print(data1)

def structure(file):
    flag = 0
    with open(file, "r") as read_file:
        data_set = json.load(read_file)
    if data_set["url"] == "https://rozetked.me/news":
            flag = 1
    if len(data_set["articles"]) >= 1 :
        flag = 1
    for i in data_set["articles"]:
        for key in i:
            if i[key] != None:
                flag=1
                break

    return(flag)

