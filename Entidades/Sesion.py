# encoding=UTF-8
"""Modulo Sesion
"""
__author__ = 'Gregorio y Ángel'


class Sesion:
    """Esta clase almacena y transfiere información relacionada con la sesion del usuario conectado al sistema.
    Args:
        dni: DNI del usuario conectado (String)
        tipo: Tipo de usuario conectado (String)
    """
    def __init__(self, dni, tipo):
        self.__dni = dni
        self.__tipo = tipo

    def get_dni(self):
        """Obtiene el DNI del usurio conectado al gestor académico.
        :returns:DNI del usuario conectado al gestor académico (str)
        """
        return self.__dni

    def get_tipo(self):
        """Obtiene el tipo de usuario conectado al gestor académico.
        :return: Tipo de usuario conectado al gestor académico (str)
        """
        return self.__tipo

    def __str__(self):
        return "DNI: %s \t \t Tipo de sesion: %s" % (self.get_dni(), self.get_tipo())
