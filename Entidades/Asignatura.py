__author__ = 'Gregorio y Ángel'

class Asignatura:

    def __init__(self, codigo, nombre):
        self.__codigo = self.setCodigo(codigo)
        self.__nombre = nombre

    def setCodigo(self, codigo):
        if type(codigo)== "int":
            self.__codigo = codigo
        else:
            self.__codigo = 00000
            print "El código debe de ser numérico"

    def setNombre(self,nombre):
        self.__nombre = nombre

    def getCodigo(self):
        return self.__codigo

    def getNombre(self):
        return self.__nombre