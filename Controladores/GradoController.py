# encoding=UTF-8
__author__ = 'Gregorio y Ángel'
from Almacen import *
from UtilExpedientes import *

class GradoController:

    def __init__(self, terminales):
        self.__terminales = terminales

    def getAlmacen(self):
        return Almacen.get_instance()

    def obtenerMatriculasYMenciones(self,codigo,sesion):
        grado = Grado(codigo,None,None)
        if sesion.getTipo() == "TecnicoCalidad":
            return UtilExpedientes().getMatriculasYMenciones(self.getAlmacen().listar_expedientes_grado(grado))
        return None

    def obtenerMedia(self,codigo,sesion):
        grado = Grado(codigo,None,None)
        if sesion.getTipo() == "TecnicoCalidad":
            return UtilExpedientes().getMediaExpedientes(self.getAlmacen().listar_expedientes_grado(grado))
        return None

    def obtenerRango(self,codigo,sesion):
        grado = Grado(codigo,None,None)
        if sesion.getTipo() == "TecnicoCalidad":
            return UtilExpedientes().getRangosExpedientes(self.getAlmacen().listar_expedientes_grado(grado))
        return None

    def listar(self,sesion):
        if sesion.getTipo() == "TecnicoCalidad":
            return self.getAlmacen().listar_grados_centro()
        return None