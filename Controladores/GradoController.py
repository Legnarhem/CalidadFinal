# encoding=UTF-8
__author__ = 'Gregorio y Ángel'
from Almacen import *
from UtilExpedientes import *

class GradoController:

    def __init__(self, terminales):
        self.__terminales = terminales

    def getAlmacen(self):
        return Almacen.getInstance()

    def obtenerMatriculasYMenciones(self,codigo,sesion):
        grado = Grado(codigo,None,None)
        if sesion.getTipo() == "TecnicoCalidad":
            return UtilExpedientes().get_matriculas_y_menciones(self.getAlmacen().listarExpedientesGrado(grado))
        return None

    def obtenerMedia(self,codigo,sesion):
        grado = Grado(codigo,None,None)
        if sesion.getTipo() == "TecnicoCalidad":
            return UtilExpedientes().get_media_expedientes(self.getAlmacen().listarExpedientesGrado(grado))
        return None

    def obtenerRango(self,codigo,sesion):
        grado = Grado(codigo,None,None)
        if sesion.getTipo() == "TecnicoCalidad":
            return UtilExpedientes().get_rangos_expedientes(self.getAlmacen().listarExpedientesGrado(grado))
        return None

    def listar(self,sesion):
        if sesion.getTipo() == "TecnicoCalidad":
            return self.getAlmacen().listarGradosCentro()
        return None