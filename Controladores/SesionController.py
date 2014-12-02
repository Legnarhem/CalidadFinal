__author__ = 'Ángel'

from Entidades.Sesion import *
from Almacen import *
from Entidades.Docente import *
from Entidades.TecnicoCalidad import *

class SesionController:

    def __init__(self, terminales):
        self.__terminales = terminales


    def obtenerSesion(self, user, passw):
        if Almacen.obtenerDocente(user) is not None:
            doc = Almacen.obtenerDocente(user)
            dni = doc.getDNI()
            if doc.getPassword() is passw:
                sesion = Sesion.__init__(dni, "docente")
        elif Almacen.obtenerTecnicoCalidad(user) is not None:
            tec = Almacen.obtenerTecnicoCalidad(user)
            dni = tec.getDNI()
            if tec.getPassword() is passw:
                sesion = Sesion.__init__(dni, "tecnico")
        else:
            print("Sesión nula")
            sesion = Sesion.__init__(None, None)

        return sesion

