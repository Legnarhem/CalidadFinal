# encoding=UTF-8
__author__ = 'Gregorio y Ángel'


class Usuario:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password
