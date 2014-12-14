# encoding=UTF-8
"""Módulo de Test para la clase src.Almacen
"""
__author__ = 'Gregorio y Ángel'

from unittest import TestCase
from src.Almacen import *
from src.Entidades.Grado import *
from src.Entidades.Alumno import *
from src.Entidades.Asignatura import *
from src.Entidades.Docente import *


class TestAlmacen(TestCase):
    """Esta clase corresponde al caso de prueba de src.TestAlmacen.\n
    En ella solo se prueban aquellos métodos no cubiertos por los tests de src/Controladores.
    """

    def setUp(self):
        """Este método prepara el contexto necesario para las pruebas de TestTerminal
        """
        print("Preparando contexto para " + self.__class__.__name__)
        self.almacen = Almacen.get_instance()
        self.alumno_valido = Alumno("13936349T", None, None)
        self.asignatura_invalida = Asignatura(-1, None)
        self.docente_valido = Docente(None, None, "49251223B", None, None)
        self.grado_valido = Grado(1, None, None)

    def tearDown(self):
        """Este método elimina el contexto utilizado para las pruebas de TestTerminal
        """
        print("Destruyendo contexto para " + self.__class__.__name__)
        del self.almacen
        del self.alumno_valido
        del self.asignatura_invalida
        del self.docente_valido
        del self.grado_valido

    def test_obtener_alumno(self):
        """Comprueba el comportamiento normal ante un alumno válido.
        """
        self.assertNotEqual(self.almacen.obtener_alumno(self.alumno_valido), None)   

    def test_listar_alumnos_grado(self):
        """Comprueba el comportamiento normal ante un grado valido.
        """
        self.assertNotEqual(self.almacen.listar_alumnos_grado(self.grado_valido), None)

    def test_obtener_grado(self):
        """Comprueba el comportamiento normal ante un grado valido.
        """
        self.assertNotEqual(self.almacen.obtener_grado(self.grado_valido), None)

    def test_listar_grados_docente(self):
        """Comprueba el comportamiento normal ante un docente valido.
        """
        self.assertNotEqual(self.almacen.listar_grados_docente(self.docente_valido), None)

    def test_listar_expedientes_grado(self):
        """Comprueba el comportamiento normal ante un grado valido.
        """
        self.assertNotEqual(self.almacen.listar_expedientes_grado(self.grado_valido), None)

    def test_obtener_ensenyanza(self):
        """Comprueba el comportamiento normal ante un docente valido y asignatura inexistente.
        """
        self.assertEqual(self.almacen.obtener_ensenyanza(self.docente_valido, self.asignatura_invalida), None)