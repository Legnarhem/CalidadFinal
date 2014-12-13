# encoding=UTF-8
"""Módulo UtilExpedientes
"""
__author__ = 'Gregorio y Ángel'
from src.Entidades.Resumen import *
from src.Entidades.Rango import *
from src.Entidades.MatriculasYMenciones import *


class UtilExpedientes:
    """En esta clase se gestionan los expedientes de los alumnos
    """
    NOTA_MATRICULAS = 10
    NOTA_MENCION = 9.5

    NOTA_APROBADOS = 5
    NOTA_NOTABLES = 7
    NOTA_SOBRESALIENTES = 9
    NOTA_LIMITE = 10

    def __init__(self):
        pass

    @staticmethod
    def get_matriculas_y_menciones(expedientes):
        """Obtiene el número de matrículas y menciones
        :param expedientes: Listas de expedientes
        :return: Las matrículas y menciones (MatriculasYMenciones)
        """
        mat = 0
        men = 0
        for e in expedientes:
            m = UtilExpedientes.get_media_expediente(e)
            if UtilExpedientes.NOTA_MENCION <= m < UtilExpedientes.NOTA_MATRICULAS:
                men += 1
            elif m == UtilExpedientes.NOTA_MATRICULAS:
                mat += 1
        return MatriculasYMenciones(mat, men)

    @staticmethod
    def get_media_expediente(expediente):
        """Obtiene la nota media de un expediente
        :param expediente: El expediente de un alumno (Expediente)
        :return: media de las notas del expediente (float)
        """
        nota_acumulada = 0
        n_notas = 0
        for n in expediente.get_notas():
            nota_acumulada += float(n)
            n_notas += 1
        return float(nota_acumulada / n_notas)

    def get_media_expedientes(self, expedientes):
        """Obtiene la nota media de varios expedientes
        :param expedientes: Lista de expedientes (list)
        :return: media de las notas de los expedientes (float)
        """
        media_acumulada = 0
        n_expedientes = 0
        for e in expedientes:
            media_acumulada += self.get_media_expediente(e)
            n_expedientes += 1
        return float(media_acumulada / n_expedientes)

    def get_rangos_expedientes(self, expedientes):
        """Clasifica las notas de varios expedientes en los diferentes rangos de notas
        :param expedientes: Lista de expedientes (list)
        :return: Rango de notas (Rango)
        """
        suspensos = 0
        aprobados = 0
        notables = 0
        sobresalientes = 0
        for e in expedientes:
            media = self.get_media_expediente(e)
            if media <= self.NOTA_APROBADOS:
                suspensos += 1
            elif self.NOTA_APROBADOS <= media < self.NOTA_NOTABLES:
                aprobados += 1
            elif self.NOTA_NOTABLES <= media < self.NOTA_SOBRESALIENTES:
                notables += 1
            elif self.NOTA_SOBRESALIENTES <= media <= self.NOTA_LIMITE:
                sobresalientes += 1
        return Rango(suspensos, aprobados, notables, sobresalientes)

    def get_resumen(self, expedientes):
        """Obtiene un resumen estadístico de un conjunto de expedientes
        :param expedientes: Lista de expedientes (list)
        :return: Resumen estadístico de los expedientes (Resumen)
        """
        asignaturas = dict()
        nota_alumno_acumulada = 0
        nota_asignatura_acumulada = 0
        n_expedientes = 0
        for e in expedientes:
            asig = e.get_asignatura().get_codigo()
            if asig not in asignaturas:
                asignaturas[asig] = []
            asignaturas[asig].append(e)
        for asig in asignaturas.keys():
            l = list(asignaturas.get(asig))
            for exp in l:
                nota_alumno_acumulada += self.get_media_expediente(exp)
            nota_asignatura_acumulada += self.get_media_expedientes(l)
            n_expedientes += len(l)
        return Resumen(float(nota_alumno_acumulada / n_expedientes),
                       float(nota_asignatura_acumulada / len(asignaturas.keys())))