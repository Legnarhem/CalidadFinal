# encoding=UTF-8
"""Modulo Usuario
"""
__author__ = 'Gregorio y Ángel'


class Usuario:
    """Esta clase representa a un usuario del gestor academico.\n
        Args:\n
        username (str): Nick del usuario\n
        password (str): Contraseña del usuario
    """
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def get_username(self):
        """Obtiene el nick del usuario.

        :return: Nick del usuario (str)
        """
        return self.__username

    def get_password(self):
        """Obtiene la contraseña del usuario.

        :return: Contraseña del usuario (str)
        """
        return self.__password
