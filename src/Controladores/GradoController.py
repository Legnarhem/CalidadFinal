# encoding=UTF-8
"""Módulo GradoController del paquete Controladores
"""
__author__ = 'Gregorio y Ángel'
from src.Almacen import *
from src.UtilExpedientes import *
from src.Entidades.Grado import *


class GradoController:
    """Esta clase es un controlador de la entidad Grado.\n
        Args:\n
        terminales (list<Terminal): Lista de terminales/vistas asociadas al controlador
    """
    def __init__(self, terminales):
        self.__terminales = terminales

    @staticmethod
    def get_almacen():
        """Obtiene una instancia de Almacen.

        :return: Instancia de Almacen (Almacen)
        """
        return Almacen.get_instance()

    def obtener_matriculas_y_menciones(self, codigo, sesion):
        """Obtiene una representación estadística del número de matrículas y menciones logradas en el grado/curso
        indicado, si el usuario conectado al gestor académico tiene acceso.

        :param codigo: Codigo de grado/curso (int)
        :param sesion: Sesion del usuario conectado al gestor académico (Sesion)
        :return: Representación estadística (MatriculasYMenciones) o None en caso de carencia de privilegios
        """
        grado = Grado(codigo, None, None)
        if sesion.get_tipo() == "TecnicoCalidad":
            return UtilExpedientes().get_matriculas_y_menciones(self.get_almacen().listar_expedientes_grado(grado))
        return None

    def obtener_media(self, codigo, sesion):
        """Obtiene la media global de un grado/curso indicado, si el usuario conectado al gestor académico tiene acceso.

        :param codigo: Codigo de grado/curso (int)
        :param sesion: Sesion del usuario conectado al gestor académico (Sesion)
        :return: Media global de grado (float) si existe o None en caso contrario o de carencia de privilegios
        """
        grado = Grado(codigo, None, None)
        if sesion.get_tipo() == "TecnicoCalidad":
            return UtilExpedientes().get_media_expedientes(self.get_almacen().listar_expedientes_grado(grado))
        return None

    def obtener_rango(self, codigo, sesion):
        """Obtiene el rango de notas de los distintos expedientes asociados al grado/curso indicado
        que es accesible por el usuario conectado al gestor academico.

        :param codigo: Codigo de grado/curso (int)
        :param sesion: Sesion del usuario conectado al gestor académico (Sesion)
        :return: Rango de notas (Rango) si existe o None en caso contrario o de carencia de privilegios
        """
        grado = Grado(codigo, None, None)
        if sesion.get_tipo() == "TecnicoCalidad":
            return UtilExpedientes().get_rangos_expedientes(self.get_almacen().listar_expedientes_grado(grado))
        return None

    def listar(self, sesion):
        """Obtiene una lista de todos los grados/cursos a los que el usuario conectado al gestor académico tiene acceso.

        :param sesion: Sesion del usuario conectado al gestor académico (Sesion)
        :return: Lista de grados/cursos (list) si existen o None en caso contrario o de carencia de privilegios
        """
        if sesion.get_tipo() == "TecnicoCalidad":
            return self.get_almacen().listar_grados_centro()
        return None