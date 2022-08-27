from typing import List


class TokenizationModule():

    def __init__(self, tokens: List[str], raw_text: str) -> None:
        self.tokens = tokens
        self.raw_text = raw_text
        self.tokenized_text = self.get_tokenized_text_by_words()

    def get_tokenized_text_by_letters(self) -> List[str]:
        return [char for char in self.raw_text]


    def get_tokenized_text_by_words(self) -> List[str]:
        print(self.raw_text.split(" "))
        return self.raw_text.split(" ") 

    def get_token_occurences(self) -> dict:
        token_occurences = {}
        for token in self.tokenized_text:
            token_occurences[token] = self.raw_text.count(token)
        return token_occurences
