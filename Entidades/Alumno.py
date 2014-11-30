# encoding=UTF-8
from Comparable import *
__author__ = 'Gregorio y Ángel'

class Alumno(Comparable):

    def __init__(self, dni, nombre, apellidos):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos

    def _cmpkey(self):
        return self.getDNI()

    def getDNI(self):
        return self.__dni

    def getNombre(self):
        return self.__nombre

    def getApellidos(self):
        return self.__apellidos

    def __eq__(self, other):
        return self.getDNI() == other.getDNI()

    def __str__(self):
        return "%9s \t %15s \t%s " % (self.getDNI(),self.getNombre(),self.getApellidos())