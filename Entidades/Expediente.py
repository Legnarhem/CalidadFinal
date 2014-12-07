# encoding=UTF-8
"""Modulo Expediente
"""
__author__ = 'Gregorio y Ángel'


class Expediente:
    """Esta clase representa una relación entre un alumno, una asignatura y sus notas en la misma.
    Args:
        alumno (Alumno): Alumno involucrado en la asignatura
        asignatura (Asignatura): Asignatura en la que el alumno expedienta
        notas (list<float>): Lista de notas reales del alumno en la asignatura
    """
    def __init__(self, alumno, asignatura, notas):
        self.__alumno = alumno
        self.__asignatura = asignatura
        self.__notas = notas

    def get_alumno(self):
        """Obtiene el alumno involucrado.
        :return: Alumno involucrado (Alumno)
        """
        return self.__alumno

    def get_asignatura(self):
        """Obtiene la asignatura en la que se expedienta.
        return: Asignatura que expedienta (Asignatura)
        """
        return self.__asignatura

    def get_notas(self):
        """Obtiene las notas del alumno en la asignatura.
        :return: Lista de notas del alumno (List<Float>)
        """
        return self.__notas

    def __str__(self):
        return "%s \t %s \n%s" % (self.get_alumno().get_dni(), self.get_asignatura().get_codigo(), self.get_notas())