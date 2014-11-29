__author__ = 'Gregorio y Ángel'

class Alumno:

    def __init__(self, dni, nombre, apellidos):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos

    def getDni(self):
        return self.__dni

    def getNombre(self):
        return self.__nombre

    def getApellidos(self):
        return self.__apellidos

