# encoding=UTF-8
__author__ = 'Gregorio y Ángel'


class Sesion:
    def __init__(self, dni, tipo):
        self.__dni = dni
        self.__tipo = tipo

    def get_dni(self):
        return self.__dni

    def get_tipo(self):
        return self.__tipo

    def __str__(self):
        return "DNI: $s \t \t Tipo de sesion: $s" % (self.get_dni(), self.get_tipo())
