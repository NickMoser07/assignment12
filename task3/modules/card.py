from modules.gronkyutil import TITLE, GANG

class Card:
    def __init__(self, id):
        self.__id = id

    def getTitle(self):
        return TITLE[self.__id % len(TITLE)] # Do not use a numeric literal

    def getGang(self):
        return GANG[self.__id // len(TITLE)] # Do not use a numeric literal

    def getID(self):
        return self.__id

    # Add two dunder methods below to meet assignment requirements

    def __str__(self):
        return str(self.getTitle() + " of " + self.getGang())