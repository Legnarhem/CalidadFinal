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
        if sesion.getTipo() == "TecnicoCalidad":
            return self.getAlmacen().listarAsignaturasGrado(Grado(codigo,None,None))
        return None

    def obtenerMedia(self,codigo,sesion):
        apto = False
        asignatura = Asignatura(codigo,None)
        if sesion.getTipo() == "TecnicoCalidad":
            apto = True
        elif sesion.getTipo() == "Docente":
            if asignatura in self.getAlmacen().listarAsignaturasDocente(Docente(None, None, sesion.getDNI(), None, None)):
                apto = True
        return UtilExpedientes().get_media_expedientes(self.getAlmacen().listarExpedientesAsignatura(asignatura)) if apto else None

    def obtenerRango(self,codigo,sesion):
        apto = False
        asignatura = Asignatura(codigo,None)
        if sesion.getTipo() == "TecnicoCalidad":
            apto = True
        elif sesion.getTipo() == "Docente":
            if asignatura in self.getAlmacen().listarAsignaturasDocente(Docente(None, None, sesion.getDNI(), None, None)):
                apto = True
        return UtilExpedientes().get_rangos_expedientes(self.getAlmacen().listarExpedientesAsignatura(asignatura)) if apto else None

    def listar(self,sesion):
        if sesion.getTipo() == "TecnicoCalidad":
            return self.getAlmacen().listarAsignaturasCentro()
        elif sesion.getTipo() == "Docente":
            return self.getAlmacen().listarAsignaturasDocente(Docente(None, None, sesion.getDNI(), None, None))
        return None


