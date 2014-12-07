# encoding=UTF-8
__author__ = 'Gregorio y Ángel'


class Resumen:
    def __init__(self, nota_promedio_alumno, nota_promedio_asignatura):
        self.__notaPromedioAlumno = nota_promedio_alumno
        self.__notaPromedioAsignatura = nota_promedio_asignatura

    def get_nota_promedio_alumno(self):
        return self.__notaPromedioAlumno

    def get_nota_promedio_asignatura(self):
        return self.__notaPromedioAsignatura

    def __str__(self):
        return "Nota promedio alumno: %f \r Nota promedio asignatura: %f" % (
            self.get_nota_promedio_alumno(), self.get_nota_promedio_asignatura())
