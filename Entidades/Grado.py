# encoding=UTF-8
"""Modulo Grado
"""
__author__ = 'Gregorio y Ángel'
from Comparable import *


class Grado(Comparable):
    """Esta clase representa un grado/curso concreto del centro académico.
    Args:
        codigo (int): Identificado único del grado/curso
        nombre (str): Título del grado/curso
        asignaturas (list<Asignatura>): Asignaturas asociadas al grado/curso
    """
    def __init__(self, codigo, nombre, asignaturas):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__asignaturas = asignaturas

    def _cmpkey(self):
        return self.get_codigo()

    def get_codigo(self):
        """Obtiene el identificador único del grado/curso.
        :return: Identificador único del grado/curso (int)
        """
        return self.__codigo

    def get_nombre(self):
        """Obtiene el título del grado/curso.
        :return: Título del grado/curso (str)
        """
        return self.__nombre

    def get_asignaturas(self):
        """Obtiene las asignaturas del grado/curso.
        :return: Lista de asignaturas del grado/curso (list)
        """
        return self.__asignaturas

    def set_codigo(self, codigo):
        """Actualiza el identificador úncico del grado/curso.
        Lanza una excepcion si no es de tipo int.
        :param codigo:Identificador del grado/curso (int)
        """
        if type(codigo) is int:
            self.__codigo = codigo
        else:
            raise TypeError("Codigo de grado debe ser numerico")

    def __str__(self):
        return "%s \t\t %s" % (self.get_codigo(), self.get_nombre())