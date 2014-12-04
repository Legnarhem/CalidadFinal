# encoding=UTF-8
__author__ = 'Gregorio y Ángel'
from Comparable import *

class Asignatura(Comparable):

    def __init__(self, codigo, nombre):
        self.setCodigo(codigo)
        self.__nombre = nombre

    def _cmpkey(self):
        return self.getCodigo()

    def setCodigo(self, codigo):
        self.__codigo = int(codigo)

    def getCodigo(self):
        return int(self.__codigo)

    def getNombre(self):
        return str(self.__nombre)

    def __str__(self):
        return "%s \t\t %s" % (self.getCodigo(), self.getNombre())