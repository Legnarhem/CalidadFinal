# encoding=UTF-8
__author__ = 'Gregorio y Ángel'
from Almacen import *
from UtilExpedientes import *

class AsignaturaController:

    def __init__(self, terminales):
        self.__terminales = terminales

    def getAlmacen(self):
        return Almacen.getInstance()

    def obtenerAsigsGrado(self,codigo,sesion):
        if sesion.get_tipo() == "TecnicoCalidad":
            return self.getAlmacen().listarAsignaturasGrado(Grado(codigo,None,None))
        return None

    def obtenerMedia(self,codigo,sesion):
        apto = False
        asignatura = Asignatura(codigo,None)
        if sesion.get_tipo() == "TecnicoCalidad":
            apto = True
        elif sesion.get_tipo() == "Docente":
            if asignatura in self.getAlmacen().listarAsignaturasDocente(Docente(None, None, sesion.get_dni(), None, None)):
                apto = True
        return UtilExpedientes().getMediaExpedientes(self.getAlmacen().listarExpedientesAsignatura(asignatura)) if apto else None

    def obtenerRango(self,codigo,sesion):
        apto = False
        asignatura = Asignatura(codigo,None)
        if sesion.get_tipo() == "TecnicoCalidad":
            apto = True
        elif sesion.get_tipo() == "Docente":
            if asignatura in self.getAlmacen().listarAsignaturasDocente(Docente(None, None, sesion.get_dni(), None, None)):
                apto = True
        return UtilExpedientes().getRangosExpedientes(self.getAlmacen().listarExpedientesAsignatura(asignatura)) if apto else None

    def listar(self,sesion):
        if sesion.get_tipo() == "TecnicoCalidad":
            return self.getAlmacen().listarAsignaturasCentro()
        elif sesion.get_tipo() == "Docente":
            return self.getAlmacen().listarAsignaturasDocente(Docente(None, None, sesion.get_dni(), None, None))
        return None


