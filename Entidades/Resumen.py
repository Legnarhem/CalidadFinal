# encoding=UTF-8
__author__ = 'Gregorio y Ángel'

class Resumen:

    def __init__(self, notaPromedio, notaAsignaturaPromedio):
        self.__notaPromedio = notaPromedio
        self.__notaAsignaturaPromedio = notaAsignaturaPromedio

    def getNotaPromedio(self):
        return self.__notaPromedio

    def getNotaAsignaturaPromedio(self):
        return self.__notaAsignaturaPromedio

    def __str__(self):
        return "Nota promedio: $f \r Nota promedio asignatura: $f" % (self.getNotaPromedio(), self.getNotaAsignaturaPromedio())
    """ No añado los setters porque supongo que solo cambiamos las nota promedios a través de la
    funcion getResumen de UtilExpediente"""
