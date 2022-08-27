from typing import List
from models.Url import Url
import re


class EmailModule:

    blacklisted_emails: str

    def __init__(self, blacklisted_emails: List[str]) -> None:
        self.bl_email = blacklisted_emails

    # Modules for email scraping
    def get_emails(self) -> bool:
        gmail = (c for c in soup.find_all(string=re.compile('@gmail')))
        hotmail = (c for c in soup.find_all(string=re.compile('@hotmail')))
        if not 'https' in Url.url:
            new_string = Url.url[7:9]
        else:
            new_string = Url.url[8:10]
        soup = self.get_soup()
        private = (c for c in soup.find_all(
            string=re.compile('@{}'.format(new_string))))
        with open('emails.txt', 'w', newline='') as f:
            f.write(''.join(['Gmail\t', str(list(gmail)), '\n\n']))
            f.write(''.join(['Hotmail\t', str(list(hotmail)), '\n\n']))
            f.write(''.join(['Other\t', str(list(private)), '\n\n']))
        return True

        # print(emails)
