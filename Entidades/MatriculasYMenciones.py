# encoding=UTF-8
"""Modulo MatriculasYMenciones
"""
__author__ = 'Gregorio y Ángel'


class MatriculasYMenciones:
    """Esta clase transfiere informacion correspondiente a cantidad de matriculas y menciones.
    Args:
        matriculas (int): Cantidad de matriculas logradas
        menciones (int): Cantidad de menciones logradas
    """
    def __init__(self, matriculas, menciones):
        self.__matriculas = matriculas
        self.__menciones = menciones

    def get_matriculas(self):
        """Obtiene la cantidad de matrículas logradas.
        :return: Cantidad de mátriculas (int)
        """
        return self.__matriculas

    def get_menciones(self):
        """Obtiene la cantidad de menciones logradas.
        :return: Cantidad de menciones (int)
        """
        return self.__menciones

    def __str__(self):
        return "%s \t\t %s" % (self.get_matriculas(), self.get_menciones())