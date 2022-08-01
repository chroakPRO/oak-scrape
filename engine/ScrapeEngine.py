import bs4 as bs
import requests

from typing import List
from modules.EmailModule import EmailModule
from modules.LinkModule import LinkModule


class ScrapeEngine:

    url: str

    def __init__(self, url: str, module: str, key: str) -> None:
        self.url = url
        self.module = module
        self.key = key

    def get_soup(self) -> bs.BeautifulSoup:
        response = requests.get(self.url)
        return bs.BeautifulSoup(response.text, 'lxml')

    def get_links(self) -> List[str]:
        x = LinkModule(self.url)
        return x.get_links()

    def get_links_with_text(self) -> List[str]:
        x = LinkModule(self.url)
        return x.get_links_with_text()

    def get_emails(self) -> List[str]:
        x = EmailModule(self.url)
        return x.get_emails()

    def run(self, permission: List[str], module: int):
