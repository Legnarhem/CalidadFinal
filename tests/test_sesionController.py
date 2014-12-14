# encoding=UTF-8
"""Módulo de Test para la clase src.Controladores.SesionController
"""

from unittest import TestCase
from src.Controladores.SesionController import *

__author__ = 'Gregorio y Ángel'


class TestSesionController(TestCase):
    def setUp(self):
        """Este método prepara el contexto necesario para las pruebas de TestSesionController
        """
        print("Preparando contexto para " + self.__class__.__name__)
        self.controlador = SesionController(None)

    def tearDown(self):
        """Este método elimina el contexto utilizado para las pruebas de TestSesionController
        """
        print("Destruyendo contexto para " + self.__class__.__name__)
        del self.controlador

    def test_get_almacen(self):
        """Comprueba que el controlador puede obtener una instancia de almacen.
        """
        self.assertNotEqual(self.controlador.get_almacen(), None)

    def test_obtener_sesion(self):
        """Comprueba que no devulve ninguna sesión cuando se introducen credenciales erróneas,
        y que se devuelva una sesión cuando las credenciales son correctas.
        """
        self.assertEquals(self.controlador.obtener_sesion("upepito", "pepito"), None)

        self.assertNotEqual(self.controlador.obtener_sesion("u10025580R", "tecnico"), None)
        self.assertNotEqual(self.controlador.obtener_sesion("u49251223B", "docente1"), None)