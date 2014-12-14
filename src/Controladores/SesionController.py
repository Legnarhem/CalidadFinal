# encoding=UTF-8
"""Módulo SesionController del paquete Controladores
"""
__author__ = 'Gregorio y Ángel'
from src.Entidades.Sesion import *
from src.Almacen import *
from src.Entidades.Docente import *
from src.Entidades.TecnicoCalidad import *


class SesionController:
    """Esta clase es un controlador de la entidad Sesion.\n
        Args:\n
        terminales (list<Terminal): Lista de terminales/vistas asociadas al controlador
    """
    def __init__(self, terminales):
        self.__terminales = terminales

    @staticmethod
    def get_almacen():
        """Obtiene una instancia de Almacen.

        :return: Instancia de Almacen (Almacen)
        """
        return Almacen.get_instance()

    def obtener_sesion(self, user, passw):
        """Obtiene una sesion en el gestor académico.

        :param user: Usuario del gestor académico (str)
        :param passw: Contraseña del usuario del gestor académico (str)
        :return: Sesion (Sesion) si las credenciales son validas o None en caso contrario
        """
        dni = user[1:]
        sesion = None
        doc = self.get_almacen().obtener_docente(Docente(None, None, dni, None, None))
        if doc is not None and doc.get_password() == passw:
            sesion = Sesion(dni, doc.__class__.__name__)
        else:
            tec = self.get_almacen().obtener_tecnico_calidad(TecnicoCalidad(None, None, dni, None, None))
            if tec is not None and tec.get_password() == passw:
                sesion = Sesion(dni, tec.__class__.__name__)
        return sesion