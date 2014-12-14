# encoding=UTF-8
"""Módulo Docente
"""
__author__ = 'Gregorio y Ángel'
from src.Entidades.Comparable import *
from src.Entidades.Usuario import *


class Docente(Usuario, Comparable):
    """Esta clase representa a un docente del centro académico.\n
        Args:\n
        username (str): Usuario de acceso del docente\n
        password (str): Contraseña para el usuario del docente\n
        dni (str): DNI del docente. Es atributo comparador\n
        nombre (str): Nombre completo del docente\n
        apellidos (str): Apellidos del docente
    """

    def __init__(self, username, password, dni, nombre, apellidos):
        Usuario.__init__(self, username, password)
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos

    def _cmpkey(self):
        return self.get_dni()

    def get_dni(self):
        """Obtiene el DNI del docente.

        :return: DNI del docente (str)
        """
        return str(self.__dni)

    def get_nombre(self):
        """Obtiene el nombre completo del docente.

        :return: Nombre completo del docente (str)
        """
        return str(self.__nombre)

    def get_apellidos(self):
        """Obtiene los apellidos del docente.

        :return: Apellidos del docente (str)
        """
        return str(self.__apellidos)

    def __str__(self):
        return "%s \t %9s \t %15s \t%s " % (
            self.get_username(), self.get_dni(), self.get_nombre(), self.get_apellidos())