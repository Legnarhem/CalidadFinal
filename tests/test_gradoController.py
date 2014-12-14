# encoding=UTF-8
"""Módulo de Test para la clase src.Controladores.GradoController
"""

from unittest import TestCase
from src.Controladores.GradoController import *
from src.Entidades.Sesion import *

__author__ = 'Gregorio y Ángel'


class TestGradoController(TestCase):
    def setUp(self):
        """Este método prepara el contexto necesario para las pruebas de TestGradoController
        """
        print("Preparando contexto para " + self.__class__.__name__)
        self.controlador = GradoController(None)
        self.sesion_tec = Sesion("10025580R", "TecnicoCalidad")
        self.sesion_doc = Sesion("49251223B", "Docente")
        self.sesion_tipo_invalido = Sesion("u77328326P", "Absurdo")

    def tearDown(self):
        """Este método elimina el contexto utilizado para las pruebas de TestGradoController
        """
        print("Destruyendo contexto para " + self.__class__.__name__)
        del self.controlador
        del self.sesion_tec
        del self.sesion_doc
        del self.sesion_tipo_invalido

    def test_get_almacen(self):
        """Comprueba que el controlador puede obtener una instancia de almacen.
        """
        self.assertNotEqual(self.controlador.get_almacen(), None)

    def test_obtener_matriculas_y_menciones(self):
        """Comprueba que ni un docente ni una sesión extraña puedan obtener las matriculas y menciones del grado/curso,
        independientemente del grado/curso indicado
        """
        self.assertEquals(self.controlador.obtener_matriculas_y_menciones(1, self.sesion_doc), None)
        self.assertEquals(self.controlador.obtener_matriculas_y_menciones(1, self.sesion_tipo_invalido), None)

    def test_obtener_media(self):
        """Comprueba que ni un docente ni una sesión extraña puedan obtener la media del grado/curso,
        independientemente del grado/curso indicado
        """
        self.assertEquals(self.controlador.obtener_media(1, self.sesion_doc), None)
        self.assertEquals(self.controlador.obtener_media(1, self.sesion_tipo_invalido), None)

    def test_obtener_rango(self):
        """Comprueba que ni un docente ni una sesión extraña puedan obtener los rangos del grado/curso,
        independientemente del grado/curso indicado
        """
        self.assertEquals(self.controlador.obtener_rango(1, self.sesion_doc), None)
        self.assertEquals(self.controlador.obtener_rango(1, self.sesion_tipo_invalido), None)

    def test_listar(self):
        """Comprueba que un técnico puede obtener sus grados/cursos mientras que una
        sesión extraña o un docente no pueden.
        """
        self.assertNotEqual(self.controlador.listar(self.sesion_tec), None)

        self.assertEquals(self.controlador.listar(self.sesion_tipo_invalido), None)
        self.assertEquals(self.controlador.listar(self.sesion_doc), None)