# encoding=UTF-8
__author__ = 'Gregorio y Ángel'
from Terminal import *
from Controladores.AlumnoController import *
from Controladores.AsignaturaController import *
from Controladores.CentroController import *
from Controladores.GradoController import *
from Controladores.SesionController import *


def main():
    terminales = list()
    terminales.append(Terminal())

    alumno_controller = AlumnoController(terminales)
    asignatura_controller = AsignaturaController(terminales)
    centro_controller = CentroController(terminales)
    grado_controller = GradoController(terminales)
    sesion_controller = SesionController(terminales)

    for terminal in terminales:
        terminal.setAlumnoController(alumno_controller)
        terminal.setAsignaturaController(asignatura_controller)
        terminal.setCentroController(centro_controller)
        terminal.setGradoController(grado_controller)
        terminal.setSesionController(sesion_controller)
        terminal.iniciar()


if __name__ == "__main__":
    main()