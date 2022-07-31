from engine.ScrapeEngine import ScrapeEngine
from modules.EmailModule import EmailModule
from modules.LinkModule import LinkModule
from modules.TokenizationModule import TokenizationModule
from models.Request import Request
from models.Url import Url


def main():
    request = Request()
    request.setURL(Url('https://www.google.com'))
    request.setMODULES(ModulesEnum.LINK)
    request.setKey('test')
    request.sendRequest()



if __name__ == '__main__':
    main()