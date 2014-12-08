# encoding=UTF-8
__author__ = 'Gregorio y Ángel'

from Almacen import *
from UtilExpedientes import *


class AlumnoController:
    def __init__(self, terminales):
        self.__terminales = terminales

    @staticmethod
    def get_almacen():
        return Almacen.getInstance()

    def obtener_alus_asignatura(self, codigo, sesion):
        apto = False
        asignatura = Asignatura(codigo, None)
        if sesion.getTipo() == "TecnicoCalidad":
            apto = True
        elif sesion.getTipo() == "Docente":
            lista = self.get_almacen().listarAsignaturasDocente(Docente(None, None, sesion.getDNI(), None, None))
            if asignatura in lista:
                apto = True
        return self.get_almacen().listarAlumnosAsignatura(
            self.get_almacen().obtenerAsignatura(Asignatura(codigo, None))) if apto else None

    def obtener_alus_grado(self, codigo, sesion):
        if sesion.getTipo() == "TecnicoCalidad":
            return self.get_almacen().listarAlumnosGrado(Grado(codigo, None, None))
        return None

    def obtener_media(self, dni, codigo, sesion):
        apto = False
        alumno = Alumno(dni, None, None)
        if sesion.getTipo() == "TecnicoCalidad":
            apto = True
        elif sesion.getTipo() == "Docente":
            alumnos = self.listar(sesion)
            if alumno in alumnos:
                apto = True
        return UtilExpedientes().getMediaExpediente(
            self.get_almacen().obtenerExpediente(Alumno(dni, None, None), Asignatura(codigo, None))) if apto else None

    def obtener_media_centro(self, dni, sesion):
        apto = False
        if sesion.getTipo() == "TecnicoCalidad":
            apto = True
        return UtilExpedientes().getMediaExpedientes(
            self.get_almacen().listarExpedientesAlumno(Alumno(dni, None, None))) if apto else None

    def obtener_rango(self, dni, sesion):
        apto = False
        if sesion.getTipo() == "TecnicoCalidad":
            apto = True
        return UtilExpedientes().getRangosExpedientes(
            self.get_almacen().listarExpedientesAlumno(Alumno(dni, None, None))) if apto else None

    def listar(self, sesion):
        if sesion.getTipo() == "TecnicoCalidad":
            return self.get_almacen().listarAlumnosCentro()
        elif sesion.getTipo() == "Docente":
            return self.get_almacen().listarAlumnosDocente(Docente(None, None, sesion.getDNI(), None, None))
        return None