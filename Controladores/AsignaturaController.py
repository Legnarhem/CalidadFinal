# encoding=UTF-8
__author__ = 'Gregorio y Ángel'
from Almacen import *
from UtilExpedientes import *


class AsignaturaController:
    def __init__(self, terminales):
        self.__terminales = terminales

    @staticmethod
    def get_almacen():
        return Almacen.getInstance()

    def obtener_asigs_grado(self, codigo, sesion):
        if sesion.getTipo() == "TecnicoCalidad":
            return self.get_almacen().listarAsignaturasGrado(Grado(codigo, None, None))
        return None

    def obtener_media(self, codigo, sesion):
        apto = False
        asignatura = Asignatura(codigo, None)
        if sesion.getTipo() == "TecnicoCalidad":
            apto = True
        elif sesion.getTipo() == "Docente":
            if asignatura in self.get_almacen().listarAsignaturasDocente(
                    Docente(None, None, sesion.getDNI(), None, None)):
                apto = True
        return UtilExpedientes().getMediaExpedientes(
            self.get_almacen().listarExpedientesAsignatura(asignatura)) if apto else None

    def obtener_rango(self, codigo, sesion):
        apto = False
        asignatura = Asignatura(codigo, None)
        if sesion.getTipo() == "TecnicoCalidad":
            apto = True
        elif sesion.getTipo() == "Docente":
            if asignatura in self.get_almacen().listarAsignaturasDocente(
                    Docente(None, None, sesion.getDNI(), None, None)):
                apto = True
        return UtilExpedientes().getRangosExpedientes(
            self.get_almacen().listarExpedientesAsignatura(asignatura)) if apto else None

    def listar(self, sesion):
        if sesion.getTipo() == "TecnicoCalidad":
            return self.get_almacen().listarAsignaturasCentro()
        elif sesion.getTipo() == "Docente":
            return self.get_almacen().listarAsignaturasDocente(Docente(None, None, sesion.getDNI(), None, None))
        return None


