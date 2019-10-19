import unittest
import json

import urllib.request
from Lab_1 import get_html_page
from bs4 import BeautifulSoup



class TestStructure(unittest.TestCase):
    def test_of_strucher(self):
        file = "articles.json"
        with open(file, "r", encoding="utf-8") as read_file1:
            data_set = json.load(read_file1)
        self.assertEqual(data_set["url"],"https://rozetked.me/news")
        self.assertGreaterEqual(len(data_set["articles"]), 1)
        for i in data_set["articles"]:
            c = []
            for key in i:
                self.assertIsNotNone(i[key])
                c.append(key)
            self.assertEqual(c[0],"title")
            self.assertEqual(c[1],"seconds")




class TestSearcharticles(unittest.TestCase):
    def test_of_search(self):
        url = 'https://rozetked.me/news'
        rozetked_html = get_html_page(url)
        rozetked_parsed = BeautifulSoup(rozetked_html, 'html.parser')
        rozedked_article = rozetked_parsed.find_all(class_='post_new-title')
        with open("type_page", "w", encoding="utf-8") as write_file:
            write_file.write(rozetked_html)
        self.assertEqual(rozedked_article,rozetked_parsed.find_all(class_='post_new-title'))



class TestURL(unittest.TestCase):
    def test_of_url(self):
        url = "https://rozetked.me/news"
        result = urllib.request.urlopen(url).getcode()
        self.assertTrue(result, 200)

if __name__ == '__main__':
    unittest.main()