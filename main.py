from models.Request import Request
from models.Url import Url
from models.ModulesEnum import ModulesEnum


def main():
    print(12)

    request = Request()
    if request.setURL("https://oaksec.dev"):
        print("URL set")
    module = ModulesEnum()
    print("MODULE LINK {}".format(module.LINK))
    if request.setMODULES(module.TOKEN):
        print("MODULE set")
    if request.setKey('test'):
        print("KEY set")
    if request.sendRequest():
        print("Request sent")


if __name__ == '__main__':
    main()
