# encoding=UTF-8
"""Módulo Asignatura
"""
__author__ = 'Gregorio y Ángel'
from src.Entidades.Comparable import *


class Asignatura(Comparable):
    """Esta clase representa una asignatura del centro academico.
    Args:
        codigo (str): Identificador único de la asignatura
        nombre (str): Título de la asignatura
    """
    def __init__(self, codigo, nombre):
        self.__nombre = nombre
        self.__codigo = None
        self.set_codigo(codigo)

    def _cmpkey(self):
        return self.get_codigo()

    def set_codigo(self, codigo):
        """Actualiza el identificador de la asignatura.
        :param codigo:Identificador de la asignatura (int)
        """
        self.__codigo = int(codigo)

    def get_codigo(self):
        """Obtiene el identificador de la asignatura.
        :return: Identificador de la asignatura (int)
        """
        return int(self.__codigo)

    def get_nombre(self):
        """Obtiene el nombre de la asignatura.
        :return: Nombre de la asignatura (str)
        """
        return str(self.__nombre)

    def __str__(self):
        return "%s \t\t %s" % (self.get_codigo(), self.get_nombre())