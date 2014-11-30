# encoding=UTF-8
__author__ = 'Gregorio y Ángel'

class Ensenyanza:

    def __init__(self,docente,asignatura):
        self.__docente = docente
        self.__asignatura = asignatura

    def getDocente(self):
        return self.__docente

    def getAsignatura(self):
        return self.__asignatura

    def __str__(self):
        return "%40s \t-\t %s" % (self.getAsignatura().getNombre(),self.getDocente().getDNI())