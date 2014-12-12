# encoding=UTF-8
"""Modulo principal que inicializa el Gestor Académico
"""
__author__ = 'Gregorio y Ángel'
from Terminal import *
from Controladores.AlumnoController import *
from Controladores.AsignaturaController import *
from Controladores.CentroController import *
from Controladores.GradoController import *
from Controladores.SesionController import *


def main():
    """
    1 - Crea un contenedor de las vistas y añade las intancias de éstas.
    2 - Inicializa los controladores de las entidades del proyecto.
    3 - Asigna los controladores anteriormente inicializados a cada vista del contenedor, y posteriormente la lanza
    :return:
    """
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