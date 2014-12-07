# encoding=UTF-8
__author__ = 'Gregorio y Ángel'
from Comparable import *


class Asignatura(Comparable):
    def __init__(self, codigo, nombre):
        self.__nombre = nombre
        self.set_codigo(codigo)

    def _cmpkey(self):
        return self.get_codigo()

    def set_codigo(self, codigo):
        self.__codigo = int(codigo)

    def get_codigo(self):
        return int(self.__codigo)

    def get_nombre(self):
        return str(self.__nombre)

    def __str__(self):
        return "%s \t\t %s" % (self.get_codigo(), self.get_nombre())