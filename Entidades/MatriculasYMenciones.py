# encoding=UTF-8
__author__ = 'Gregorio y Ángel'


class MatriculasYMenciones:
    def __init__(self, matriculas, menciones):
        self.__matriculas = matriculas
        self.__menciones = menciones

    def get_matriculas(self):
        return self.__matriculas

    def get_menciones(self):
        return self.__menciones

    def __str__(self):
        return "%s \t\t %s" % (self.get_matriculas(), self.get_menciones())