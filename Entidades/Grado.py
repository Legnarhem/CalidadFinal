# encoding=UTF-8
__author__ = 'Gregorio y Ángel'
from Comparable import *


class Grado(Comparable):
    def __init__(self, codigo, nombre, asignaturas):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__asignaturas = asignaturas

    def _cmpkey(self):
        return self.get_codigo()

    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_asignaturas(self):
        return self.__asignaturas

    def set_codigo(self, codigo):
        if type(codigo) is int:
            self.__codigo = codigo
        else:
            raise TypeError("Codigo de grado debe ser numerico")

    def __str__(self):
        return "%s \t\t %s" % (self.get_codigo(), self.get_nombre())