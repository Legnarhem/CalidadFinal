__author__ = 'Ángel'

from Almacen import *
from UtilExpedientes import *
class AlumnoController:

    def __init__(self, terminales):
        self.__terminales = terminales

    def getAlmacen(self):
        return Almacen.getInstance()

    def obtenerAlusAsignatura(self, codigo, sesion):
        almacen = self.getAlmacen()
        apto = False
        if sesion.getTipo() == "tecnico":
            apto = True
        elif sesion.getTipo() == "docente":
            asignatura = Asignatura(codigo,None)
            lista = almacen.listarAsignaturasDocente(Docente(None,None,sesion.getDni(),None,None))
            if asignatura in lista:
                apto = True
        else:
            print("No tiene permiso para obtener la lista de alumnos de la asignatura")

        if apto:
            return almacen.listarAlumnosAsignatura(almacen.obtenerAsignatura(Asignatura(codigo, None)))
        else:
            return None

    def obtenerAlusGrado(self, codigo, sesion):
        almacen = self.getAlmacen()
        if sesion.getTipo() == "tecnico":
            return almacen.listarAlumnosGrado(Grado(codigo,None,None))
        else:
            print("No tiene permiso para obtener la lista de alumnos del Grado")
            return None
    '''
    Habia pensado de ver si el alumno estaba matriculado en alguna de las asignatura que impartía el profesor,
    y permitir al docente en ese caso poder acceder a esta informacion. Pero la unica forma de listar las asignaturas de
    un alumno es a traves de listarAlumnosAsignatura y para ello necesitamos el codigo de la asignatura, lo dejo comentado

    '''
    def obtenerMedia(self, dni, sesion):
        almacen = self.getAlmacen()

        apto = False
        if sesion.getTipo() == "tecnico":
            apto = True

        else:
            print("No tiene permiso para obtener la media del expediente de este alumno")
        #Iria antes del else
        '''
        elif sesion.getTipo() == "docente":
            asignatura = Asignatura(codigo,None)
            listaDocente = almacen.listarAsignaturasDocente(Docente(None,None,sesion.getDni(),None,None))
            listaAlumno = almacen.listarAlumnosAsignatura(asignatura)
            if asignatura in listaDocente and asignatura in listaAlumno:
                apto = True
        '''
        if apto:
            expediente = almacen.listarExpedientesAlumno(Alumno(dni,None,None))
            return UtilExpedientes.getMediaExpediente(expediente)
        else:
            return None

    def obtenerRango(self, dni, sesion):
        almacen = self.getAlmacen()

        apto = False
        if sesion.getTipo() == "tecnico":
            apto = True

        else:
            print("No tiene permiso para obtener el rango de notas de este alumno")
        #Iria antes del else
        '''
        elif sesion.getTipo() == "docente":
            asignatura = Asignatura(codigo,None)
            listaDocente = almacen.listarAsignaturasDocente(Docente(None,None,sesion.getDni(),None,None))
            listaAlumno = almacen.listarAlumnosAsignatura(asignatura)
            if asignatura in listaDocente and asignatura in listaAlumno:
                apto = True
        '''
        if apto:
            expediente = almacen.listarExpedientesAlumno(Alumno(dni,None,None))
            return UtilExpedientes.getRangosExpediente(expediente)
        else:
            return None

    def listar(self, sesion):
        almacen = self.getAlmacen()
        if sesion.getTipo() == "tecnico":
            return almacen.listarAlumnosCentro()
        else:
            print("No tiene permiso para ver la lista de alumnos del centro")
            return None




