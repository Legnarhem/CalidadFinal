# encoding=UTF-8
__author__ = 'Gregorio y Ángel'

from Almacen import *
from UtilExpedientes import *
class AlumnoController:

    def __init__(self, terminales):
        self.__terminales = terminales

    def getAlmacen(self):
        return Almacen.getInstance()

    def obtenerAlusAsignatura(self, codigo, sesion):
        apto = False
        asignatura = Asignatura(codigo,None)
        if sesion.get_tipo() == "TecnicoCalidad":
            apto = True
        elif sesion.get_tipo() == "Docente":
            lista = self.getAlmacen().listarAsignaturasDocente(Docente(None,None,sesion.get_dni(),None,None))
            if asignatura in lista:
                apto = True
        return self.getAlmacen().listarAlumnosAsignatura(self.getAlmacen().obtenerAsignatura(Asignatura(codigo, None))) if apto else None

    def obtenerAlusGrado(self, codigo, sesion):
        if sesion.get_tipo() == "TecnicoCalidad":
            return self.getAlmacen().listarAlumnosGrado(Grado(codigo,None,None))
        return None

    def obtenerMedia(self, dni, codigo, sesion):
        apto = False
        alumno = Alumno(dni, None, None)
        if sesion.get_tipo() == "TecnicoCalidad":
            apto = True
        elif sesion.get_tipo() == "Docente":
            alumnos = self.listar(sesion)
            if alumno in alumnos:
                apto = True
        return UtilExpedientes().getMediaExpediente(self.getAlmacen().obtenerExpediente(Alumno(dni,None,None), Asignatura(codigo, None))) if apto else None


    def obtenerMediaCentro(self, dni, sesion):
        apto = False
        alumno = Alumno(dni, None, None)
        if sesion.get_tipo() == "TecnicoCalidad":
            apto = True
        return UtilExpedientes().getMediaExpedientes(self.getAlmacen().listarExpedientesAlumno(Alumno(dni,None,None))) if apto else None

    def obtenerRango(self, dni, sesion):
        apto = False
        alumno = Alumno(dni, None, None)
        if sesion.get_tipo() == "TecnicoCalidad":
            apto = True
        return UtilExpedientes().getRangosExpedientes(self.getAlmacen().listarExpedientesAlumno(Alumno(dni, None, None))) if apto else None

    def listar(self, sesion):
        if sesion.get_tipo() == "TecnicoCalidad":
            return self.getAlmacen().listarAlumnosCentro()
        elif sesion.get_tipo() == "Docente":
            return self.getAlmacen().listarAlumnosDocente(Docente(None,None,sesion.get_dni(),None,None))
        return None




