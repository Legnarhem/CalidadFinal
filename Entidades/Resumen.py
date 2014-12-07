# encoding=UTF-8
"""Modulo Resumen
"""
__author__ = 'Gregorio y Ángel'


class Resumen:
    """Esta clase almacena y transfiere información correspondiente a notas promedio de alumnos y asignaturas.
    Args:
        nota_promedio_alumno (float): Nota promedio de alumno
        nota_promedio_asignatura (float): Nota promedio de asignatura
    """
    def __init__(self, nota_promedio_alumno, nota_promedio_asignatura):
        self.__notaPromedioAlumno = nota_promedio_alumno
        self.__notaPromedioAsignatura = nota_promedio_asignatura

    def get_nota_promedio_alumno(self):
        """Obtiene la nota promedio de alumno.
        :return: Nota promedio de alumno (float)
        """
        return self.__notaPromedioAlumno

    def get_nota_promedio_asignatura(self):
        """Obtiene la nota promedio de asignatura.
        :return: NOta promedio de asignatura (float)
        """
        return self.__notaPromedioAsignatura

    def __str__(self):
        return "Nota promedio alumno: %f \r Nota promedio asignatura: %f" % (
            self.get_nota_promedio_alumno(), self.get_nota_promedio_asignatura())
