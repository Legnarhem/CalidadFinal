__author__ = 'Ángel'

from Almacen import *
from UtilExpedientes import *

class AsignaturaController:

    def __init__(self, terminales):
        self.__terminales = terminales

    def getAlmacen(self):
        return Almacen.getInstance()

    def obtenerAsigsGrado(self,codigo,sesion):
        almacen = self.getAlmacen()
        if sesion.getTipo() == "tecnico":
            return almacen.listarAsignaturasGrado(Grado(codigo,None,None))
        else:
            print("No tiene permiso para ver las asignaturas que se imparten en este grado")
            return None

    def obtenerMedia(self,codigo,sesion):
        almacen = self.getAlmacen()
        apto = False
        asignatura = Asignatura(codigo,None)
        if sesion.getTipo() == "tecnico":
            apto = True
        elif sesion.getTipo() == "docente":
            doc = Docente(None,None,sesion.getDni(),None,None)
            if asignatura in almacen.listarAsignaturasDocente(doc):
                apto = True
        else:
            print("No tiene permiso para obtener la media de la asignatura")

        if apto:
            return UtilExpedientes.getMediaExpedientes(almacen.listarExpedientesAsignatura(asignatura))
        else:
            return None

    def obtenerRango(self,codigo,sesion):
        almacen = self.getAlmacen()
        asignatura = Asignatura(codigo,None)
        apto = False
        if sesion.getTipo() == "tecnico":
            apto = True
        elif sesion.getTipo() == "docente":
            doc = Docente(None,None,sesion.getDni(),None,None)
            if asignatura in almacen.listarAsignaturasDocente(doc):
                apto = True
        else:
            print("No tiene permiso para obtener los rangos de notas de la asignatura")

        if apto:
            return UtilExpedientes.getRangosExpediente(almacen.listarExpedientesAsignatura(asignatura))
        else:
            return None

    def listar(self,sesion):
        almacen = self.getAlmacen()
        if sesion.getTipo() == "tecnico":
            return almacen.listarAsignaturasCentro()
        else:
            print("No tiene los permisos para obtener las asignaturas del centro")
            return None


