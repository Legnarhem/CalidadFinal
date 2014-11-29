__author__ = 'Gregorio y Ángel'

import Usuario.py

class TecnicoCalidad(Usuario):
    pass
    def __init__(self, username, password, dni, nombre, apellidos):
        Usuario.__init__(self, username, password)
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos

    def getDni(self):
        return self.__dni

    def getNombre(self):
        return self.__nombre

    def getApellidos(self):
        return self.__apellidos
