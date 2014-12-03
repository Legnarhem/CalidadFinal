__author__ = 'Ángel'

from Almacen import *
from UtilExpedientes import *

class GradoController:

    def __init__(self, terminales):
        self.__terminales = terminales

    def getAlmacen(self):
        return Almacen.getInstance()

    def obtenerMatriculasYMenciones(self,codigo,sesion):
        almacen = self.getAlmacen()
        grado = Grado(codigo,None,None)
        if sesion.getTipo() == "tecnico":
            return UtilExpedientes.getMatriculasYMenciones(almacen.listarExpedientesGrado(grado))
        else:
            print("No tiene permisos para conocer las Matriculas y Menciones de este grado")
            return None

    def obtenerMedia(self,codigo,sesion):
        almacen = self.getAlmacen()
        grado = Grado(codigo,None,None)
        if sesion.getTipo() == "tecnico":
            return UtilExpedientes.getMediaExpedientes(almacen.listarExpedientesGrado(grado))
        else:
            print("No tiene permisos para conocer la media de este grado")
            return None

    def obtenerRango(self,codigo,sesion):
        almacen = self.getAlmacen()
        grado = Grado(codigo,None,None)
        if sesion.getTipo() == "tecnico":
            return UtilExpedientes.getRangosExpediente(almacen.listarExpedientesGrado(grado))
        else:
            print("No tiene permisos para conocer los rangos de notas de este grado")
            return None

    #Verdaderamente no es problema que los docentes pudieses realizar este metodo
    def listar(self,sesion):
        almacen = self.getAlmacen()
        if sesion.getTipo() == "tecnico":
            return almacen.listarGradosCentro()
        else:
            print("No tiene permiso para conocer los grados del centro")
            return None

    '''
       No se si un docente que pertenezca al grado puede acceder a alguno de estos metodos, en ese caso avisame y lo
        modifico.
    '''