from typing import List
from this import d
from engine.ScrapeEngine import ScrapeEngine


class TokenizationModule():

    def __init__(self, tokens: List[str], raw_text: str) -> None:
        self.tokens = tokens
        self.raw_text = raw_text
        self.tokenized_text = self.get_tokenized_text()

    def get_tokenized_text(self) -> list:
        return [char for char in self.raw_text]

    def get_token_occurences(self) -> dict:
        token_occurences = {}
        for token in self.tokenized_text:
            token_occurences[token] = self.raw_text.count(token)
        return token_occurences
