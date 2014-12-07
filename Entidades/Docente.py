# encoding=UTF-8
"""Módulo Docente
"""
__author__ = 'Gregorio y Ángel'
from Comparable import *
from Usuario import *


class Docente(Usuario, Comparable):
    """Esta clase representa a un docente del centro académico.
    Args:
        username (str): Usuario de acceso del docente
        password (str): Contraseña para el usuario del docente
        dni (str): DNI del docente. Es atributo comparador
        nombre (str): Nombre completo del docente
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
        :return:DNI del docente (str)
        """
        return str(self.__dni)

    def get_nombre(self):
        """Obtiene el nombre completo del docente.
        :return:Nombre completo del docente (str)
        """
        return str(self.__nombre)

    def get_apellidos(self):
        """Obtiene los apellidos del docente.
        :return:Apellidos del docente (str)
        """
        return str(self.__apellidos)

    def __str__(self):
        return "%s \t %9s \t %15s \t%s " % (
            self.get_username(), self.get_dni(), self.get_nombre(), self.get_apellidos())