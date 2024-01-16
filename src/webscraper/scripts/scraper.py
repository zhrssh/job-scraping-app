import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, url) -> BeautifulSoup:
        self.url = url

        if self.url:
            # Send a get request to the url
            html = requests.get(url).text

            # Pass html to beautiful soup
            soup = BeautifulSoup(html, "lxml")
            return soup

        else:
            return None
