# encoding=UTF-8
"""Módulo de Test para la clase src.Controladores.CentroController
"""

from unittest import TestCase
from src.Controladores.CentroController import *
from src.Entidades.Sesion import *

__author__ = 'Gregorio y Ángel'


class TestCentroController(TestCase):
    """Esta clase corresponde al caso de prueba de src.Controladores.CentroController.
    """

    def setUp(self):
        """Este método prepara el contexto necesario para las pruebas de TestCentroController
        """
        print("Preparando contexto para " + self.__class__.__name__)
        self.controlador = CentroController(None)
        self.sesion_tec = Sesion("10025580R", "TecnicoCalidad")
        self.sesion_doc = Sesion("49251223B", "Docente")
        self.sesion_tipo_invalido = Sesion("u77328326P", "Absurdo")

    def tearDown(self):
        """Este método elimina el contexto utilizado para las pruebas de TestCentroController
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

    def test_obtener_resumen(self):
        """Compreba que ni un docente ni una sesion extraña puedan obtener el resumen del centro,
        y que el técnico de calidad lo reciba.
        """
        self.assertEquals(self.controlador.obtener_resumen(self.sesion_doc), None)
        self.assertEquals(self.controlador.obtener_resumen(self.sesion_tipo_invalido), None)

        self.assertNotEqual(self.controlador.obtener_resumen(self.sesion_tec), None)