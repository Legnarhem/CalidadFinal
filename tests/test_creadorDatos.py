# encoding=UTF-8
"""Módulo de Test para la clase src.CreadorDatos
"""
__author__ = 'Gregorio y Ángel'

from unittest import TestCase
from src.CreadorDatos import main
import os.path


class TestCreadorDatos(TestCase):
    """Esta clase corresponde al caso de prueba de src.CreadorDatos.
    """
    def test_main(self):
        """Comprueba que el creador de datos de prueba es capaz de crearlos.
        """
        donde = "test"
        main(donde)
        self.assert_(os.path.exists(donde + ".db"))