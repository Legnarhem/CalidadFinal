# encoding=UTF-8
"""Modulo Rango
"""
__author__ = 'Gregorio y Ángel'


class Rango:
    """Esta clase almacena y transfiere información correspondiente a rangos de notas.\n
        Args:\n
        suspensos (int): Cantidad de suspensos acontecidos\n
        aprobados (int): Cantidad de aprobados acontecidos\n
        notables (int): Cantidad de notables acontecidos\n
        sobresalientes (int): Cantidad de sobresalientes acontecidos
    """
    def __init__(self, suspensos, aprobados, notables, sobresalientes):
        self.__suspensos = suspensos
        self.__aprobados = aprobados
        self.__notables = notables
        self.__sobresalientes = sobresalientes

    def get_suspensos(self):
        """Obtiene la cantidad de suspensos acontecidos.

        :return: Cantidad de suspensos (int)
        """
        return self.__suspensos

    def get_aprobados(self):
        """Obtiene la cantidad de aprobados acontecidos.

        :return: Cantidad de aprobados (int)
        """
        return self.__aprobados

    def get_notables(self):
        """Obtiene la cantidad de notables acontecidos.

        :return: Cantidad de notables (int)
        """
        return self.__notables

    def get_sobresalientes(self):
        """Obtiene la cantidad de sobresalientes acontecidos.

        :return: Cantidad de sobresalientes (int)
        """
        return self.__sobresalientes

    def __str__(self):
        return "Suspensos: %s \r Aprobados: %s \r Notables: %s \r Sobresalientes: %s" % (
        self.get_suspensos(), self.get_aprobados(), self.get_notables(), self.get_sobresalientes())