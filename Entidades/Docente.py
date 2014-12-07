# encoding=UTF-8
__author__ = 'Gregorio y Ángel'
from Comparable import *
from Usuario import *


class Docente(Usuario, Comparable):
    def __init__(self, username, password, dni, nombre, apellidos):
        Usuario.__init__(self, username, password)
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos

    def _cmpkey(self):
        return self.get_dni()

    def get_dni(self):
        return str(self.__dni)

    def get_nombre(self):
        return str(self.__nombre)

    def get_apellidos(self):
        return str(self.__apellidos)

    def __str__(self):
        return "%s \t %9s \t %15s \t%s " % (self.get_username(), self.get_dni(), self.get_nombre(), self.get_apellidos())