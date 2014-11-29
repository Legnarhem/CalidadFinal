__author__ = 'Gregorio y Ángel'

class Rango:

    def __init__(self, suspensos, aprobados, notables, sobresalientes):
        self.__suspensos = suspensos
        self.__aprobados = aprobados
        self.__notables = notables
        self.__sobresalientes = sobresalientes

    def getSuspensos(self):
        return self.__suspensos

    def getAprobados(self):
        return self.__aprobados

    def getNotables(self):
        return self.__notables

    def getSobresalientes(self):
        return self.__sobresalientes