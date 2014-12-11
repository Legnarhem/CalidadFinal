# encoding=UTF-8
__author__ = 'Gregorio y Ángel'

from Almacen import *
from UtilExpedientes import *
class AlumnoController:

    def __init__(self, terminales):
        self.__terminales = terminales

    def getAlmacen(self):
        return Almacen.get_instance()

    def obtenerAlusAsignatura(self, codigo, sesion):
        apto = False
        asignatura = Asignatura(codigo,None)
        if sesion.getTipo() == "TecnicoCalidad":
            apto = True
        elif sesion.getTipo() == "Docente":
            lista = self.getAlmacen().listar_asignaturas_docente(Docente(None,None,sesion.getDNI(),None,None))
            if asignatura in lista:
                apto = True
        return self.getAlmacen().listar_alumnos_asignatura(self.getAlmacen().obtener_asignatura(Asignatura(codigo, None))) if apto else None

    def obtenerAlusGrado(self, codigo, sesion):
        if sesion.getTipo() == "TecnicoCalidad":
            return self.getAlmacen().listar_alumnos_grado(Grado(codigo,None,None))
        return None

    def obtenerMedia(self, dni, codigo, sesion):
        apto = False
        alumno = Alumno(dni, None, None)
        if sesion.getTipo() == "TecnicoCalidad":
            apto = True
        elif sesion.getTipo() == "Docente":
            alumnos = self.listar(sesion)
            if alumno in alumnos:
                apto = True
        return UtilExpedientes().getMediaExpediente(self.getAlmacen().obtener_expediente(Alumno(dni,None,None), Asignatura(codigo, None))) if apto else None


    def obtenerMediaCentro(self, dni, sesion):
        apto = False
        alumno = Alumno(dni, None, None)
        if sesion.getTipo() == "TecnicoCalidad":
            apto = True
        return UtilExpedientes().getMediaExpedientes(self.getAlmacen().listar_expedientes_alumno(Alumno(dni,None,None))) if apto else None

    def obtenerRango(self, dni, sesion):
        apto = False
        alumno = Alumno(dni, None, None)
        if sesion.getTipo() == "TecnicoCalidad":
            apto = True
        return UtilExpedientes().getRangosExpedientes(self.getAlmacen().listar_expedientes_alumno(Alumno(dni, None, None))) if apto else None

    def listar(self, sesion):
        if sesion.getTipo() == "TecnicoCalidad":
            return self.getAlmacen().listar_alumnos_centro()
        elif sesion.getTipo() == "Docente":
            return self.getAlmacen().listar_alumnos_docente(Docente(None,None,sesion.getDNI(),None,None))
        return None




