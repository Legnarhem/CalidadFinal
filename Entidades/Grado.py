__author__ = 'Gregorio y Ángel'


import Asignatura.py

class Grado:

    def __init__(self, codigo, nombre, asignaturas):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__asignaturas = asignaturas

    def getCodigo(self):
        return self.__codigo

    def getNombre(self):
        return self.__nombre

    def getAsignaturas(self):
        return self.__asignaturas

    def setCodigo(self, codigo):
        if type(codigo)== "int":
            self.__codigo = codigo
        else:
            self.__codigo = 00000
            print "El código debe de ser numérico"

    def setNombre(self,nombre):
        self.__nombre = nombre

    def setAsignaturas(self, asignaturas):
        self.__asignaturas = asignaturas

    def addAsignatura(self, asignatura):
        self.__asignaturas.append(asignatura)

    def removeAsignatura(self,asignatura):
        self.__asignaturas.remove(asignatura)

    def buscarAsignatura(self, asignatura):
        self.__asignaturas.index(asignatura)