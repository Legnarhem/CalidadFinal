# encoding=UTF-8
__author__ = 'Gregorio y Ángel'


class Sesion:

    def __init__(self, dni, tipo):
        self.__dni = dni
        self.__tipo = tipo

    def getDni(self):
        return self.__dni

    def getTipo(self):
        return self.__tipo

    def __str__(self):
        return "DNI: $s \t \t Tipo de sesion: $s" % (self.getDni(), self.getTipo())


