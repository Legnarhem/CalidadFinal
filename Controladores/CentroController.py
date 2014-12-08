# encoding=UTF-8
__author__ = 'Gregorio y Ángel'
from Almacen import *
from UtilExpedientes import *


class CentroController:
    def __init__(self, terminales):
        self.__terminales = terminales

    @staticmethod
    def get_almacen():
        return Almacen.getInstance()

    def obtener_resumen(self, sesion):
        if sesion.getTipo() == "TecnicoCalidad":
            return UtilExpedientes().getResumen(self.get_almacen().listarExpedientesCentro())
        return None
