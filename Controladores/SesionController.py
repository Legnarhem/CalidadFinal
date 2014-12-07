# encoding=UTF-8
__author__ = 'Gregorio y Ángel'
from Entidades.Sesion import *
from Almacen import *
from Entidades.Docente import *
from Entidades.TecnicoCalidad import *

class SesionController:

    def __init__(self, terminales):
        self.__terminales = terminales


    def getAlmacen(self):
        return Almacen.getInstance()

    def obtenerSesion(self, user, passw):
        dni = user[1:]
        sesion = None
        doc = self.getAlmacen().obtenerDocente(Docente(None,None,dni,None, None))
        if doc is not None and doc.get_password() == passw:
            sesion = Sesion(dni, doc.__class__.__name__)
        else:
            tec = self.getAlmacen().obtenerTecnicoCalidad(TecnicoCalidad(None, None, dni, None, None))
            if tec is not None and tec.get_password() == passw:
                sesion = Sesion(dni, tec.__class__.__name__)
        return sesion