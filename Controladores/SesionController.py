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
        return Almacen.get_instance()

    def obtenerSesion(self, user, passw):
        dni = user[1:]
        sesion = None
        doc = self.getAlmacen().obtener_docente(Docente(None,None,dni,None, None))
        if doc is not None and doc.getPassword() == passw:
            sesion = Sesion(dni, doc.__class__.__name__)
        else:
            tec = self.getAlmacen().obtener_tecnico_calidad(TecnicoCalidad(None, None, dni, None, None))
            if tec is not None and tec.getPassword() == passw:
                sesion = Sesion(dni, tec.__class__.__name__)
        return sesion