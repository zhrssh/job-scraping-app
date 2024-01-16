import requests

from bs4 import BeautifulSoup
from django.test import TestCase
from .scripts.scraper import Scraper


class ScraperTestCase(TestCase):
    def setUp(self):
        pass

    def test_scraper_can_scrape(self):
        url = "https://webscraper.io/test-sites/e-commerce/allinone"

        # Send a get request to the url
        html = requests.get(url).text
        self.assertIsInstance(html, str)

        # Pass html to Beautiful Soup
        soup = BeautifulSoup(html, "lxml")
        self.assertIsInstance(soup, BeautifulSoup)
