# encoding=UTF-8
__author__ = 'Gregorio y Ángel'


class Ensenyanza:
    def __init__(self, docente, asignatura):
        self.__docente = docente
        self.__asignatura = asignatura

    def get_docente(self):
        return self.__docente

    def get_asignatura(self):
        return self.__asignatura

    def __str__(self):
        return "%40s \t-\t %s" % (self.get_asignatura().get_nombre(), self.get_docente().get_dni())