# encoding=UTF-8
"""Módulo de Test para la clase src.Controladores.AsignaturaController
"""

from unittest import TestCase
from src.Controladores.AsignaturaController import *
from src.Entidades.Sesion import *

__author__ = 'Gregorio y Ángel'


class TestAsignaturaController(TestCase):
    def setUp(self):
        """Este método prepara el contexto necesario para las pruebas de TestAsignaturaController
        """
        print("Preparando contexto para " + self.__class__.__name__)
        self.controlador = AsignaturaController(None)
        self.sesion_tec = Sesion("10025580R", "TecnicoCalidad")
        self.sesion_doc = Sesion("49251223B", "Docente")
        self.sesion_tipo_invalido = Sesion("u77328326P", "Absurdo")

    def tearDown(self):
        """Este método elimina el contexto utilizado para las pruebas de TestAsignaturaController
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

    def test_obtener_asigs_grado(self):
        """Comprueba que una sesión extraña no pueda obtener la lista de asignaturas de un grado, con independencia del
        grado/curso indicado.
        """
        self.assertEquals(self.controlador.obtener_asigs_grado(1, self.sesion_tipo_invalido), None)

    def test_obtener_media(self):
        """Comprueba que una sesión extraña no pueda obtener la media de una asignatura, con independencia de la
        asignatura indicada.
        """
        self.assertEquals(self.controlador.obtener_media("1", self.sesion_tipo_invalido), None)

    def test_obtener_rango(self):
        """Comprueba que una sesión extraña no pueda obtener el rango de notas de una asignatura,
        con independencia de la asignatura indicada.
        """
        self.assertEquals(self.controlador.obtener_rango("1", self.sesion_tipo_invalido), None)

    def test_listar(self):
        """Comprueba que tanto un docente como un técnico pueden obtener sus asignaturas mientras que una
        sesión extraña no puede.
        """
        self.assertNotEqual(self.controlador.listar(self.sesion_doc), None)
        self.assertNotEqual(self.controlador.listar(self.sesion_tec), None)

        self.assertEquals(self.controlador.listar(self.sesion_tipo_invalido), None)