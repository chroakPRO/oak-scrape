from typing import List

class Url:

    def __init__(self, url: str) -> None:
        self.url = url

    def get_url(self) -> str:
        return self.get_url
    
    def set_url(self, url: str) -> bool:
        self.url = url
        if self.url:
            return True
        else:
            return False