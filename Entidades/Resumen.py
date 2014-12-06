# encoding=UTF-8
__author__ = 'Gregorio y Ángel'

class Resumen:

    def __init__(self, notaPromedioAlumno, notaPromedioAsignatura):
        self.__notaPromedioAlumno = notaPromedioAlumno
        self.__notaPromedioAsignatura = notaPromedioAsignatura

    def getNotaPromedioAlumno(self):
        return self.__notaPromedioAlumno

    def getNotaPromedioAsignatura(self):
        return self.__notaPromedioAsignatura

    def __str__(self):
        return "Nota promedio alumno: %f \r Nota promedio asignatura: %f" % (self.getNotaPromedioAlumno(), self.getNotaPromedioAsignatura())
