# encoding=UTF-8
"""Módulo AlumnoController del paquete Controladores
"""
__author__ = 'Gregorio y Ángel'

from Almacen import *
from UtilExpedientes import *
from Entidades.Asignatura import *


class AlumnoController:
    """Esta clase es un controlador de la entidad Alumno.
    Args:
        terminales (list<Terminal): Lista de terminales/vistas asociadas al controlador
    """
    def __init__(self, terminales):
        self.__terminales = terminales

    @staticmethod
    def get_almacen():
        """Obtiene una instancia de Almacen.
        :return:Instancia de Almacen (Almacen)
        """
        return Almacen.get_instance()

    def obtener_alus_asignatura(self, codigo, sesion):
        """Obtiene una lista de los alumnos expedientados en la asignatura indicada, si el usuario
        conectado al gestor académico tiene acceso.
        :param codigo:Codigo de asignatura (int)
        :param sesion:Sesion del usuario conectado al gestor académico (Sesion)
        :return:Lista de alumnos (list) si existen o None en caso contrario o de carencia de privilegios
        """
        apto = False
        asignatura = Asignatura(codigo, None)
        if sesion.get_tipo() == "TecnicoCalidad":
            apto = True
        elif sesion.get_tipo() == "Docente":
            lista = self.get_almacen().listar_asignaturas_docente(Docente(None, None, sesion.get_dni(), None, None))
            if asignatura in lista:
                apto = True
        return self.get_almacen().listar_alumnos_asignatura(
            self.get_almacen().obtener_asignatura(Asignatura(codigo, None))) if apto else None

    def obtener_alus_grado(self, codigo, sesion):
        """Obtiene una lista de los alumnos involucrados en un grado/curso indicado, si el usuario
        conectado al gestor académico tiene acceso.
        :param codigo:Codigo de grado/curso (int)
        :param sesion:Sesion del usuario conectado al gestor académico (Sesion)
        :return:Lista de alumnos (list) si existen o None en caso contrario o de carencia de privilegios
        """
        if sesion.get_tipo() == "TecnicoCalidad":
            return self.get_almacen().listar_alumnos_grado(Grado(codigo, None, None))
        return None

    def obtener_media(self, dni, codigo, sesion):
        """Obtiene la media de un alumno expedientados en la asignatura indicada, si el usuario
        conectado al gestor académico tiene acceso.
        :param dni:DNI de alumno (str)
        :param codigo:Codigo de asignatura (int)
        :param sesion:Sesion del usuario conectado al gestor académico (Sesion)
        :return:Media de alumno (float) si existe o None en caso contrario o de carencia de privilegios
        """
        apto = False
        alumno = Alumno(dni, None, None)
        if sesion.get_tipo() == "TecnicoCalidad":
            apto = True
        elif sesion.get_tipo() == "Docente":
            alumnos = self.listar(sesion)
            if alumno in alumnos:
                apto = True
        return UtilExpedientes().get_media_expediente(
            self.get_almacen().obtener_expediente(Alumno(dni, None, None), Asignatura(codigo, None))) if apto else None

    def obtener_media_centro(self, dni, sesion):
        """Obtiene la media global de un alumno en el centro académico, si el usuario
        conectado al gestor académico tiene acceso.
        :param dni:DNI de alumno (str)
        :param sesion:Sesion del usuario conectado al gestor académico (Sesion)
        :return:Media global de alumno (float) si existe o None en caso contrario o de carencia de privilegios
        """
        apto = False
        if sesion.get_tipo() == "TecnicoCalidad":
            apto = True
        return UtilExpedientes().get_media_expedientes(
            self.get_almacen().listar_expedientes_alumno(Alumno(dni, None, None))) if apto else None

    def obtener_rango(self, dni, sesion):
        """Obtiene el rango de notas de los distintos expedientes asociados al alumno indicado
        que son accesibles por el usuario conectado al gestor academico.
        :param dni:DNI de alumno (str)
        :param sesion:Sesion del usuario conectado al gestor académico (Sesion)
        :return:Rango de notas (Rango) si existe o None en caso contrario o de carencia de privilegios
        """
        apto = False
        if sesion.get_tipo() == "TecnicoCalidad":
            apto = True
        return UtilExpedientes().get_rangos_expedientes(
            self.get_almacen().listar_expedientes_alumno(Alumno(dni, None, None))) if apto else None

    def listar(self, sesion):
        """Obtiene una lista de todos los alumnos a los que el usuario conectado al gestor académico tiene acceso.
        :param sesion:Sesion del usuario conectado al gestor académico (Sesion)
        :return:Lista de alumnos (list) si existen o None en caso contrario o de carencia de privilegios
        """
        if sesion.get_tipo() == "TecnicoCalidad":
            return self.get_almacen().listar_alumnos_centro()
        elif sesion.get_tipo() == "Docente":
            return self.get_almacen().listar_alumnos_docente(Docente(None, None, sesion.get_dni(), None, None))
        return None