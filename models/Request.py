import Url
from engine.ScrapeEngine import ScrapeEngine
from models.ModulesEnum import ModulesEnum
from typing import List, Dict, Any

class Request:

    # URL
    URL: str
    # Enum of modules
    MODULES: str
    # Search value
    KEY: str
    nCount: int
    countRequired: int

    def __init__(self) -> None:
        pass

    def setURL(self, url: str) -> bool:
        self.URL = url
        if self.URL:
            self.nCount + 1
            return True
        else:
            return False
    
    def setMODULES(self, modules: str) -> bool:
        self.MODULES = modules
        if self.MODULES in ModulesEnum:
            self.nCount + 1
            return True
        else:
            return False
    
    def setKey(self, key: str) -> bool:
        self
        self.KEY = key
        if self.KEY:
            self.nCount + 1
            return True
        else:
            return False

    def sendRequest(self) -> bool:
        if self.nCount == self.countRequired:
            scrapObj = ScrapeEngine(self.URL, self.MODULES, self.KEY)
            scrapObj.get_soup()
            if self.MODULES == ModulesEnum.LINK:
                return scrapObj.get_links()
            elif self.MODULES == ModulesEnum.EMAIL:
                return scrapObj.get_emails()
            elif self.MODULES == ModulesEnum.LINK_WITH_TEXT:
                return scrapObj.get_links_with_text()
            return True
        else:
            return False