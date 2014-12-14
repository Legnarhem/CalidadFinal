# encoding=UTF-8
"""Modulo enseñanza
"""
__author__ = 'Gregorio y Ángel'


class Ensenyanza:
    """Esta clase representa una relacion de enseñanza entre un docente y una asignatura.\n
        Args:\n
        docente (Docente): Docente que imparte\n
        asignatura (Asignatura): Asignatura impartida
    """
    def __init__(self, docente, asignatura):
        self.__docente = docente
        self.__asignatura = asignatura

    def get_docente(self):
        """Obtiene el docente que imparte enseñanza.

        :return: Docente que imparte la enseñanza (Docente)
        """
        return self.__docente

    def get_asignatura(self):
        """Obtiene la asignatura que es impartida.

        :return: Asignatura impartida (Asignatura)
        """
        return self.__asignatura

    def __str__(self):
        return "%40s \t-\t %s" % (self.get_asignatura().get_nombre(), self.get_docente().get_dni())