

class LinkModule():
    """_summary_

    Args:
        ScrapeEngine (_type_): _description_
    """
    def __init__(self, url: str):
        """_summary_

        Args:
            url (str): _description_
        """
        super().__init__(url)

    def get_links(self) -> list:
        """_summary_

        Returns:
            list: _description_
        """
        soup = self.get_soup()
        links = []
        for link in soup.find_all('a'):
            links.append(link.get('href'))
        return links

    def get_links_with_text(self) -> list:
        """_summary_

        Returns:
            list: _description_
        """
        soup = self.get_soup()
        links = []
        for link in soup.find_all('a'):
            links.append(link.text)
        return links
