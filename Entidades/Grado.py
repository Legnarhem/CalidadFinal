# encoding=UTF-8
__author__ = 'Gregorio y Ángel'
from Comparable import *

class Grado(Comparable):

    def __init__(self, codigo, nombre, asignaturas):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__asignaturas = asignaturas

    def _cmpkey(self):
        return self.getCodigo()

    def getCodigo(self):
        return self.__codigo

    def getNombre(self):
        return self.__nombre

    def getAsignaturas(self):
        return self.__asignaturas

    def setCodigo(self, codigo):
        if type(codigo) is int:
            self.__codigo = codigo
        else:
            raise TypeError("Codigo de grado debe ser numerico")

    def __str__(self):
        return "%s \t\t %s" % (self.getCodigo(), self.getNombre())