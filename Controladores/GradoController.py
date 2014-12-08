# encoding=UTF-8
__author__ = 'Gregorio y Ángel'
from Almacen import *
from UtilExpedientes import *


class GradoController:
    def __init__(self, terminales):
        self.__terminales = terminales

    @staticmethod
    def get_almacen():
        return Almacen.getInstance()

    def obtener_matriculas_y_menciones(self, codigo, sesion):
        grado = Grado(codigo, None, None)
        if sesion.getTipo() == "TecnicoCalidad":
            return UtilExpedientes().getMatriculasYMenciones(self.get_almacen.listarExpedientesGrado(grado))
        return None

    def obtener_media(self, codigo, sesion):
        grado = Grado(codigo, None, None)
        if sesion.getTipo() == "TecnicoCalidad":
            return UtilExpedientes().getMediaExpedientes(self.get_almacen.listarExpedientesGrado(grado))
        return None

    def obtener_rango(self, codigo, sesion):
        grado = Grado(codigo, None, None)
        if sesion.getTipo() == "TecnicoCalidad":
            return UtilExpedientes().getRangosExpedientes(self.get_almacen.listarExpedientesGrado(grado))
        return None

    def listar(self, sesion):
        if sesion.getTipo() == "TecnicoCalidad":
            return self.get_almacen.listarGradosCentro()
        return None