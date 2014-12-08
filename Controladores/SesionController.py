# encoding=UTF-8
"""Módulo SesionController del paquete Controladores
"""
__author__ = 'Gregorio y Ángel'
from Entidades.Sesion import *
from Almacen import *
from Entidades.Docente import *
from Entidades.TecnicoCalidad import *


class SesionController:
    """Esta clase es un controlador de la entidad Sesion.
    Args:
        terminales (list<Terminal): Lista de terminales/vistas asociadas al controlador
    """
    def __init__(self, terminales):
        self.__terminales = terminales

    @staticmethod
    def get_almacen():
        """Obtiene una instancia de Almacen.
        :return:Instancia de Almacen (Almacen)
        """
        return Almacen.getInstance()

    def obtener_sesion(self, user, passw):
        """Obtiene una sesion en el gestor académico.
        :param user:Usuario del gestor académico (str)
        :param passw:Contraseña del usuario del gestor académico (str)
        :return:Sesion (Sesion) si las credenciales son validas o None en caso contrario
        """
        dni = user[1:]
        sesion = None
        doc = self.get_almacen().obtenerDocente(Docente(None, None, dni, None, None))
        if doc is not None and doc.getPassword() == passw:
            sesion = Sesion(dni, doc.__class__.__name__)
        else:
            tec = self.get_almacen().obtenerTecnicoCalidad(TecnicoCalidad(None, None, dni, None, None))
            if tec is not None and tec.getPassword() == passw:
                sesion = Sesion(dni, tec.__class__.__name__)
        return sesion