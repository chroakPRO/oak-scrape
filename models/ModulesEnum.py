import enum
from typing import List

class ModulesEnum():
    def __init__(self) -> None:
        self.EMAIL: int = 0x00
        self.LINK: int = 0x01
        self.TOKEN: int = 0x03
        self.Enum: List[int] = [self.EMAIL, self.LINK, self.TOKEN]