__author__ = 'Ángel'

from Entidades.Sesion import *
from Almacen import *
from Entidades.Docente import *
from Entidades.TecnicoCalidad import *

class SesionController:

    def __init__(self, terminales):
        self.__terminales = terminales


    def obtenerSesion(self, user, passw):
        dni = user[1:]
        doc = Docente(None,None,dni,None, None)
        tec = TecnicoCalidad(None, None, dni, None, None)
        almacen = self.getAlmacen()
        if almacen.obtenerDocente(doc) is not None:
            if doc.getPassword() is passw:
                sesion = Sesion.__init__(dni, "docente")
        elif almacen.obtenerTecnicoCalidad(tec) is not None:
            if tec.getPassword() is passw:
                sesion = Sesion.__init__(dni, "tecnico")
        else:
            print("Sesión nula")
            sesion = Sesion.__init__(None, None)

        return sesion

    def getAlmacen(self):
        return Almacen.getInstance()

