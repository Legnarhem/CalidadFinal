# encoding=UTF-8
"""Modulo TecnicoCalidad
"""
from src.Entidades.Usuario import *
from src.Entidades.Comparable import *

__author__ = 'Gregorio y Ángel'


class TecnicoCalidad(Usuario, Comparable):
    """Esta clase representa a un técnico de calidad del centro académico.\n
        Args:\n
        username (str): Usuario de acceso del técnico de calidad\n
        password (str): Contraseña para el usuario del técnico de calidad\n
        dni (str): DNI del técnico de calidad. Es atributo comparador\n
        nombre (str): Nombre completo del técnico de calidad\n
        apellidos (str): Apellidos del técnico de calidad
    """

    def __init__(self, username, password, dni, nombre, apellidos):
        Usuario.__init__(self, username, password)
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos

    def _cmpkey(self):
        return self.get_dni()

    def get_dni(self):
        """Obtiene el DNI del técnico de calidad.

        :return: DNI del técnico de calidad (str)
        """
        return self.__dni

    def get_nombre(self):
        """Obtiene el nombre completo del técnico de calidad.

        :return: Nombre completo del técnico de calidad (str)
        """
        return self.__nombre

    def get_apellidos(self):
        """Obtiene los apellidos del técnico de calidad.

        :return: Apellidos del técnico de calidad (str)
        """
        return self.__apellidos

    def __str__(self):
        return "%s \t %9s \t %15s \t%s " % (
            self.get_username(), self.get_dni(), self.get_nombre(), self.get_apellidos())