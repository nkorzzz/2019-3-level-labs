import datetime
import requests
import json
import urllib.request
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
        d = {"title": i}
        c.append(d)
    data["articles"] = c
    with open(path, "w",encoding="utf-8") as write_file:
        json.dump(data, write_file,indent = 2, ensure_ascii=False)
    return (data)


rozetked_html = get_html_page(url)
articles = find_articles(rozetked_html)
publish_report(path,articles)

def structure(file):
    flag = False
    with open(file, "r",encoding="utf-8") as read_file1:
        data_set = json.load(read_file1)
    if data_set["url"] == "https://rozetked.me/news":
            flag = True
    if len(data_set["articles"]) >= 1:
        flag = True
    for i in data_set["articles"]:
        for key in i:
            if i[key] != None:
                flag=True
                break

    return(flag)

def struc_articles(url):
    flag = False
    rozetked_html = get_html_page(url)
    rozetked_parsed = BeautifulSoup(rozetked_html, 'html.parser')
    rozedked_article = rozetked_parsed.find_all(class_='post_new-title')
    if rozedked_article == rozetked_parsed.find_all(class_='post_new-title'):
        flag= True
    return (flag)

def check_url(url):
    return(urllib.request.urlopen(url).getcode())

