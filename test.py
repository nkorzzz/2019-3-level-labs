import unittest
from Lab_1 import structure
from Lab_1 import struc_articles
from Lab_1 import check_url

class TestStructure(unittest.TestCase):
    def test_of_strucher(self):
        file = "articles.json"
        result = structure(file)  # Act
        self.assertEqual(result, True)  # Assert

class TestSearcharticles(unittest.TestCase):
    def test_of_search(self):
        url = "https://rozetked.me/news"
        result = struc_articles(url)
        self.assertEqual(result, True)

class TestURL(unittest.TestCase):
    def test_of_url(self):
        url = "https://rozetked.me/news"
        result = check_url(url)
        self.assertEqual(result, 200)

if __name__ == '__main__':
    unittest.main()