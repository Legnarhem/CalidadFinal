# encoding=UTF-8
from Comparable import *

__author__ = 'Gregorio y Ángel'


class Alumno(Comparable):
    def __init__(self, dni, nombre, apellidos):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos

    def _cmpkey(self):
        return self.get_dni()

    def get_dni(self):
        return self.__dni

    def get_nombre(self):
        return self.__nombre

    def get_apellidos(self):
        return self.__apellidos

    def __eq__(self, other):
        return self.get_dni() == other.get_dni()

    def __str__(self):
        return "%9s \t %15s \t%s " % (self.get_dni(), self.get_nombre(), self.get_apellidos())