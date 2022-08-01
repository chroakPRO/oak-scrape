from models.Request import Request
from models.Url import Url
from models.ModulesEnum import ModulesEnum


def main():
    print(12)

    request = Request()
    step01 = request.setURL("https://www.google.com")
    if step01:
        print("URL set")
        step01 = None

    module = ModulesEnum()
    print("M;ODULE LINK {}".format(module.LINK))
    if request.setMODULES(module.LINK):
        print("MODULE set")
    if request.setKey('test'):
        print("KEY set")
    if request.sendRequest():
        print("Request sent")


if __name__ == '__main__':
    main()
