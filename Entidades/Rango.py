# encoding=UTF-8
__author__ = 'Gregorio y Ángel'


class Rango:
    def __init__(self, suspensos, aprobados, notables, sobresalientes):
        self.__suspensos = suspensos
        self.__aprobados = aprobados
        self.__notables = notables
        self.__sobresalientes = sobresalientes

    def get_suspensos(self):
        return self.__suspensos

    def get_aprobados(self):
        return self.__aprobados

    def get_notables(self):
        return self.__notables

    def get_sobresalientes(self):
        return self.__sobresalientes

    def __str__(self):
        return "Suspensos: %s \r Aprobados: %s \r Notables: $s \r Sobresalientes: $s" % (
        self.get_suspensos(), self.get_aprobados(), self.get_notables(), self.get_sobresalientes())