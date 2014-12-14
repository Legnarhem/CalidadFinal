# encoding=UTF-8
"""Módulo de Test para la clase src.Terminal
"""
__author__ = 'Gregorio y Ángel'

from unittest import TestCase
from src.Entidades.Sesion import *
from src.Terminal import *


class TestTerminal(TestCase):
    """Esta clase corresponde al caso de prueba de src.Terminal.\n
    En ella solo se prueban aquellos métodos que no requieren de la interaccion del usuario.
    """

    def setUp(self):
        """Este método prepara el contexto necesario para las pruebas de TestTerminal
        """
        print("Preparando contexto para " + self.__class__.__name__)
        self.terminal = Terminal()
        self.sesion_tec = Sesion("10025580R", "TecnicoCalidad")
        self.sesion_doc = Sesion("49251223B", "Docente")

    def tearDown(self):
        """Este método elimina el contexto utilizado para las pruebas de TestTerminal
        """
        print("Destruyendo contexto para " + self.__class__.__name__)
        del self.terminal
        del self.sesion_tec
        del self.sesion_doc

    def test_set_alumno_controller(self):
        """Comprueba comportamiento normal de metodo setter.
        """
        self.terminal.set_alumno_controller("Controlador")
        self.assertEquals(self.terminal.get_alumno_controller(), "Controlador")

    def test_set_asignatura_controller(self):
        """Comprueba comportamiento normal de metodo setter.
        """
        self.terminal.set_asignatura_controller("Controlador")
        self.assertEquals(self.terminal.get_asignatura_controller(), "Controlador")

    def test_set_centro_controller(self):
        """Comprueba comportamiento normal de metodo setter.
        """
        self.terminal.set_centro_controller("Controlador")
        self.assertEquals(self.terminal.get_centro_controller(), "Controlador")

    def test_set_grado_controller(self):
        """Comprueba comportamiento normal de metodo setter.
        """
        self.terminal.set_grado_controller("Controlador")
        self.assertEquals(self.terminal.get_grado_controller(), "Controlador")

    def test_set_sesion_controller(self):
        """Comprueba comportamiento normal de metodo setter.
        """
        self.terminal.set_sesion_controller("Controlador")
        self.assertEquals(self.terminal.get_sesion_controller(), "Controlador")

    def test_set_sesion(self):
        """Comprueba comportamiento normal de metodo setter.
        """
        self.terminal.set_sesion(self.sesion_doc)
        self.assertEquals(self.terminal.get_sesion(), self.sesion_doc)