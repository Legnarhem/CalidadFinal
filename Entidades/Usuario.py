__author__ = 'Gregorio y Ángel'

class Usuario:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def getUserName (self):
        return self.__username

    def setPassword (self, password):
        self.__password = password

