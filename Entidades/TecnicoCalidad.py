# encoding=UTF-8
from Usuario import *
from Comparable import *
__author__ = 'Gregorio y Ángel'


class TecnicoCalidad(Usuario,Comparable):
    pass
    def __init__(self, username, password, dni, nombre, apellidos):
        Usuario.__init__(self, username, password)
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

    def __str__(self):
        return "%s \t %9s \t %15s \t%s " % (self.getUserName(),self.getDNI(),self.getNombre(),self.getApellidos())