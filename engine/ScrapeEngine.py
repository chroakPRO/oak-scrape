import bs4 as bs
import requests
import urllib.request
import re

class ScrapeEngine:

    url: str

    def __init__(self, url: str, key: str) -> None:
        self.url = url
        self.key = key
        source = urllib.request.urlopen(self.url).read()
        self.soup = bs.BeautifulSoup(source, 'lxml')
    
    def get_words(self):
        return self.soup.find_all(string=re.compile(self.key))
