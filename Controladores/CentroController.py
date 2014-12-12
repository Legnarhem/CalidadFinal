# encoding=UTF-8
"""Módulo CentroController del paquete Controladores
"""
__author__ = 'Gregorio y Ángel'
from Almacen import *
from UtilExpedientes import *


class CentroController:
    """Esta clase es un controlador de la entidad Centro.
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

    def obtener_resumen(self, sesion):
        """Obtiene un resumen estadístico del estado de la calidad del centro académico, si el usuario
        conectado al gestor académico tiene acceso.
        :param sesion:Sesion del usuario conectado al gestor académico (Sesion)
        :return:Resumen estadístico del estado del centro académico (Resumen), si existe,
        o None en caso contrario o de carencia de privilegios
        """
        if sesion.get_tipo() == "TecnicoCalidad":
            return UtilExpedientes().get_resumen(self.get_almacen().listarExpedientesCentro())
        return None
