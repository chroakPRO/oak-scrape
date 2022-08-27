from models.Url import Url
from engine.ScrapeEngine import ScrapeEngine
from models.ModulesEnum import ModulesEnum
from typing import List, Dict, Any


class Request:

    def __init__(self) -> None:
        self.nCount = 0
        self.countRequired = 3
        self.KEY = ""
        self.URL = ""
        self.MODULES = 0

    def setURL(self, url: str) -> bool:
        self.URL = url
        if self.URL:
            self.nCount + 1
            return True
        else:
            return False

    def setMODULES(self, modules: str) -> None:
        self.MODULES = modules
        module = ModulesEnum()
        if self.MODULES in module.Enum:
            self.nCount + 1
        else:
            self.MODULES = None
            pass

    def setKey(self, key: str) -> bool:
        self
        self.KEY = key
        if self.KEY:
            self.nCount + 1
            return True
        else:
            return False

    def sendRequest(self) -> bool:
        print("sen_requewst {}".format(self.countRequired))
        if self.nCount != self.countRequired:
            scrapObj = ScrapeEngine(self.URL, self.MODULES, self.KEY)
            print(scrapObj.get_soup())
            module = ModulesEnum()
            if self.MODULES == module.LINK:
                print(12)
                return scrapObj.get_links()
            elif self.MODULES == module.EMAIL:
                return scrapObj.get_emails()
            elif self.MODULES == module.TOKEN:
                print(1212)
                return scrapObj.get_words()
            return True
        else:
            return False
