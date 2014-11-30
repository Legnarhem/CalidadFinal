# encoding=UTF-8
__author__ = 'Gregorio y Ángel'
from Comparable import *
from Usuario import *
class Docente(Usuario, Comparable):
    def __init__(self, username, password, dni, nombre, apellidos):
        Usuario.__init__(self,username,password)
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos

    def _cmpkey(self):
        return self.getDNI()

    def getDNI(self):
        return str(self.__dni)

    def getNombre(self):
        return str(self.__nombre)

    def getApellidos(self):
        return str(self.__apellidos)

    def __str__(self):
        return "%s \t %9s \t %15s \t%s " % (self.getUserName(),self.getDNI(),self.getNombre(),self.getApellidos())