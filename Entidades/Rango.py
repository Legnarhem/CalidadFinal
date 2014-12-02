# encoding=UTF-8
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

    def __str__(self):
        return "Suspensos: %s \r Aprobados: %s \r Notables: $s \r Sobresalientes: $s" % (self.getSuspensos(), self.getAprobados(), self.getNotables(), self.getSobresalientes())