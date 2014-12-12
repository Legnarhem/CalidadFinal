# encoding=UTF-8
__author__ = 'Gregorio y Ángel'
from Entidades.Resumen import *
from Entidades.Rango import *
from Entidades.MatriculasYMenciones import *


class UtilExpedientes:
    NOTA_MATRICULAS = 10
    NOTA_MENCION = 9.5

    NOTA_APROBADOS = 5
    NOTA_NOTABLES = 7
    NOTA_SOBRESALIENTES = 9
    NOTA_LIMITE = 10

    def get_matriculas_y_menciones(self, expedientes):
        mat = 0
        men = 0
        for e in expedientes:
            m = self.get_media_expediente(e)
            if self.NOTA_MENCION <= m <= self.NOTA_MATRICULAS:
                men += 1
            elif m == self.NOTA_MATRICULAS:
                mat += 1
        return MatriculasYMenciones(mat, men)

    def get_media_expediente(self, expediente):
        nota_acumulada = 0
        n_notas = 0
        for n in expediente.getNotas():
            nota_acumulada += float(n)
            n_notas += 1
        return float(nota_acumulada / n_notas)

    def get_media_expedientes(self, expedientes):
        media_acumulada = 0
        n_expedientes = 0
        for e in expedientes:
            media_acumulada += self.get_media_expediente(e)
            n_expedientes += 1
        return float(media_acumulada / n_expedientes)

    def get_rangos_expedientes(self, expedientes):
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
        asignaturas = dict()
        nota_alumno_acumulada = 0
        nota_asignatura_acumulada = 0
        n_expedientes = 0
        for e in expedientes:
            asig = e.getAsignatura().getCodigo()
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