__author__ = 'Ángel'

from Almacen import *
from UtilExpedientes import *

class CentroController:

    def __init__(self, terminales):
        self.__terminales = terminales

    def getAlmacen(self):
        return Almacen.getInstance()

    def obtenerResumen(self, sesion):
        if sesion.getTipo() is "tecnico":
            almacen = self.getAlmacen()
            expedientes = almacen.listarExpedientesCentro()
            resumen = UtilExpedientes.getResumen(expedientes)
            return resumen
        else:
            print("No tienes permiso para obtener esta información")
            return None
