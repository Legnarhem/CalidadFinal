# encoding=UTF-8
""" Modulo Alumno
"""
from src.Entidades.Comparable import *

__author__ = 'Gregorio y Ángel'


class Alumno(Comparable):
    """Esta clase representa a un alumno del centro académico.
    Args:
        dni (str): DNI del alumno
        nombre (str): Nombre del alumno
        apellidos (str): Apellidos del alumno
    """
    def __init__(self, dni, nombre, apellidos):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos

    def _cmpkey(self):
        return self.get_dni()

    def get_dni(self):
        """Obtiene el DNI del alumno.
        :return:DNI del alumno (str)
        """
        return self.__dni

    def get_nombre(self):
        """Obtiene el nombre del alumno.
        :return:Nombre del alumno (str)
        """
        return self.__nombre

    def get_apellidos(self):
        """Obtiene los apellidos del alumno.
        :return:Apellidos del alumno (str)
        """
        return self.__apellidos

    def __eq__(self, other):
        return self.get_dni() == other.get_dni()

    def __str__(self):
        return "%9s \t %15s \t%s " % (self.get_dni(), self.get_nombre(), self.get_apellidos())