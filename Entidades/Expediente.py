# encoding=UTF-8
__author__ = 'Gregorio y Ángel'

class Expediente:

    def __init__(self,alumno,asignatura,notas):
        self.__alumno = alumno
        self.__asignatura = asignatura
        self.__notas = notas

    def getAlumno(self):
        return self.__alumno

    def getAsignatura(self):
        return self.__asignatura

    def getNotas(self):
        return self.__notas

    def __str__(self):
        return "%s \t %s \n%s" % (self.getAlumno().getDNI(), self.getAsignatura().getCodigo(), self.getNotas())