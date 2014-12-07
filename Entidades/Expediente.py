# encoding=UTF-8
__author__ = 'Gregorio y Ángel'


class Expediente:
    def __init__(self, alumno, asignatura, notas):
        self.__alumno = alumno
        self.__asignatura = asignatura
        self.__notas = notas

    def get_alumno(self):
        return self.__alumno

    def get_asignatura(self):
        return self.__asignatura

    def get_notas(self):
        return self.__notas

    def __str__(self):
        return "%s \t %s \n%s" % (self.get_alumno().get_dni(), self.get_asignatura().get_codigo(), self.get_notas())