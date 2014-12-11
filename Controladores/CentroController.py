# encoding=UTF-8
__author__ = 'Gregorio y Ángel'
from Almacen import *
from UtilExpedientes import *

class CentroController:

    def __init__(self, terminales):
        self.__terminales = terminales

    def getAlmacen(self):
        return Almacen.get_instance()

    def obtenerResumen(self, sesion):
        if sesion.getTipo() == "TecnicoCalidad":
            return UtilExpedientes().getResumen(self.getAlmacen().listar_expedientes_centro())
        return None
