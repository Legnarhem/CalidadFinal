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

    alumnoController = AlumnoController(terminales)
    asignaturaController = AsignaturaController(terminales)
    centroController = CentroController(terminales)
    gradoController = GradoController(terminales)
    sesionController = SesionController(terminales)

    for terminal in terminales:
        terminal.set_alumno_controller(alumnoController)
        terminal.set_asignatura_controller(asignaturaController)
        terminal.set_centro_controller(centroController)
        terminal.set_grado_controller(gradoController)
        terminal.set_sesion_controller(sesionController)
        terminal.iniciar()

if __name__ == "__main__":
    main()