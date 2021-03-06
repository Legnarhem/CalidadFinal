# encoding=UTF-8
"""Módulo de Test para la clase src.Controladores.AlumnoController
"""
__author__ = 'Gregorio y Ángel'

from unittest import TestCase

from src.Controladores.AlumnoController import *
from src.Entidades.Sesion import *


class TestAlumnoController(TestCase):
    """Esta clase corresponde al caso de prueba de src.Controladores.AlumnoController.
    """

    def setUp(self):
        """Este método prepara el contexto necesario para las pruebas de TestAlumnoController
        """
        print("Preparando contexto para " + self.__class__.__name__)
        self.controlador = AlumnoController(None)
        self.alumno = "13936349T"
        self.alumno_invalido = "ABCDEFGHI"
        self.sesion_tec = Sesion("10025580R", "TecnicoCalidad")
        self.sesion_doc = Sesion("49251223B", "Docente")
        self.sesion_tipo_invalido = Sesion("u77328326P", "Absurdo")
        self.grado_invalido = -1
        self.asignatura_invalida = -1

    def tearDown(self):
        """Este método elimina el contexto utilizado para las pruebas de TestAlumnoController
        """
        print("Destruyendo contexto para " + self.__class__.__name__)
        del self.controlador
        del self.sesion_tec
        del self.sesion_doc
        del self.sesion_tipo_invalido
        del self.alumno
        del self.alumno_invalido
        del self.grado_invalido
        del self.asignatura_invalida

    def test_get_almacen(self):
        """Comprueba que el controlador puede obtener una instancia de almacen.
        """
        self.assertNotEqual(self.controlador.get_almacen(), None)

    def test_obtener_alus_asignatura(self):
        """Comprueba comportamiento normal ante asignaturas inexistentes.\n
        Comprueba que una sesión extraña no puede obtener los alumnos de una asignatura, con independencia de la
        asignatura indicada.
        """
        self.assertEquals(self.controlador.obtener_alus_asignatura(self.asignatura_invalida, self.sesion_tec), None)
        self.assertEquals(self.controlador.obtener_alus_asignatura(self.asignatura_invalida, self.sesion_doc), None)

        self.assertEquals(self.controlador.obtener_alus_asignatura(1, self.sesion_tipo_invalido), None)

    def test_obtener_alus_grado(self):
        """Comprueba comportamiento normal ante grados inexistentes.\n
        Comprueba que ni un docente ni una sesión extraña puedan obtener los alumnos de un grado, con independencia
        del grado indicado.
        """
        self.assertEquals(self.controlador.obtener_alus_grado(self.grado_invalido, self.sesion_tec), None)

        self.assertEquals(self.controlador.obtener_alus_grado(1, self.sesion_doc), None)
        self.assertEquals(self.controlador.obtener_alus_grado(1, self.sesion_tipo_invalido), None)

    def test_obtener_media(self):
        """Comprueba comportamiento normal ante alumnos y asignaturas inexistentes.\n
        Comprueba que una sesión extraña no pueda obtener la media de un alumno, con independencia del
        alumno indicado.
        """
        self.assertEquals(self.controlador.obtener_media(self.alumno, self.asignatura_invalida, self.sesion_tec), None)
        self.assertEquals(self.controlador.obtener_media(self.alumno, self.asignatura_invalida, self.sesion_doc), None)

        self.assertEquals(self.controlador.obtener_media(self.alumno, "1", self.sesion_tipo_invalido), None)

    def test_obtener_media_centro(self):
        """Comprueba comportamiento normal ante alumno inexistente.\n
        Compreba que ni un docente ni una sesion extraña puedan obtener la media del centro
        con independencia del alumno indicado.
        """
        self.assertEquals(self.controlador.obtener_media_centro(self.alumno_invalido, self.sesion_tec), None)

        self.assertEquals(self.controlador.obtener_media_centro(self.alumno, self.sesion_tipo_invalido), None)

    def test_obtener_rango(self):
        """Comprueba comportamiento normal ante alumno inexistente.\n
        Comprueba ni un docente ni una sesión extraña puedan obtener el rango de notas de un alumno,
        con independencia del alumno indicado.
        """
        self.assertEquals(self.controlador.obtener_rango(self.alumno_invalido, self.sesion_tec), None)

        self.assertEquals(self.controlador.obtener_rango("1", self.sesion_doc), None)
        self.assertEquals(self.controlador.obtener_rango("1", self.sesion_tipo_invalido), None)

    def test_listar(self):
        """Comprueba que tanto un docente como un técnico pueden obtener sus alumnos mientras que una
        sesión extraña no puede.
        """
        self.assertNotEqual(self.controlador.listar(self.sesion_doc), None)
        self.assertNotEqual(self.controlador.listar(self.sesion_tec), None)

        self.assertEquals(self.controlador.listar(self.sesion_tipo_invalido), None)