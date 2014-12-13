# encoding=UTF-8
"""Módulo de Test para la clase src.UtilExpedientes
"""
__author__ = 'Gregorio y Ángel'

from unittest import TestCase
from src.Entidades.Asignatura import *
from src.Entidades.Expediente import *
from src.UtilExpedientes import *


class TestUtilExpedientes(TestCase):
    """Esta clase corresponde al caso de prueba de src.UtilExpedientes.
    """

    def setUp(self):
        """Este método prepara el contexto necesario para las pruebas de TestUtilExpedientes
        """
        print("Preparando contexto para " + self.__class__.__name__)

        self.asignatura_1 = Asignatura(1, "Asignatura 1")
        self.asignatura_2 = Asignatura(2, "Asignatura 2")

        self.expediente_1 = Expediente(None, self.asignatura_1, [9.5 for n in range(1, 5)])
        self.expediente_2 = Expediente(None, self.asignatura_1, [9.6 for n in range(1, 6)])
        self.expediente_3 = Expediente(None, self.asignatura_2, [10 for n in range(1, 7)])

        self.expedientes = list()

        self.expedientes.append(self.expediente_1)
        self.expedientes.append(self.expediente_2)
        self.expedientes.append(self.expediente_3)

    def tearDown(self):
        """Este método elimina el contexto utilizado para las pruebas de TestUtilExpedientes
        """
        print("Destruyendo contexto para " + self.__class__.__name__)
        del self.expediente_1
        del self.expediente_2
        del self.expediente_3
        del self.expedientes

    def test_get_matriculas_y_menciones(self):
        """Comprueba que las matriculas y menciones devueltas corresponden con las que deberian
        segun el contexto de setUp()
        """
        mym = UtilExpedientes.get_matriculas_y_menciones(self.expedientes)
        self.assertEqual(mym.get_matriculas(), 1)
        self.assertEqual(mym.get_menciones(), 2)

    def test_get_media_expediente(self):
        """Comprueba que las medias calculadas de los expedientes corresponden con las que deberian
        segun el contexto de setUp()
        """
        self.assert_(UtilExpedientes.get_media_expediente(self.expediente_1) == 9.5)
        self.assert_(UtilExpedientes.get_media_expediente(self.expediente_2) == 9.6)
        self.assert_(UtilExpedientes.get_media_expediente(self.expediente_3) == 10)

    def test_get_media_expedientes(self):
        """Comprueba que la media calculada de una lista de expedientes corresponde con las que deberian
        segun el contexto de setUp()
        """
        media_expes = UtilExpedientes().get_media_expedientes(self.expedientes)
        self.assertAlmostEqual(media_expes, float(9.7), places=3)

    def test_get_rangos_expedientes(self):
        """Comprueba que el rangos obtenido de analizar los expedientes corresponde con las que deberian
        segun el contexto de setUp()
        """
        rango = UtilExpedientes().get_rangos_expedientes(self.expedientes)

        self.assertEqual(rango.get_sobresalientes(), 3)
        self.assertEqual(rango.get_aprobados(), 0)
        self.assertEqual(rango.get_notables(), 0)
        self.assertEqual(rango.get_suspensos(), 0)

    def test_get_resumen(self):
        """Comprueba que el resumen devuelto de analizar los expedientes, teniendo en cuenta la asignatura a
        la que corresponden, corresponde con el que debería ser segun el contexto de setUp()
        """
        resumen = UtilExpedientes().get_resumen(self.expedientes)

        self.assertAlmostEqual(resumen.get_nota_promedio_alumno(), float(9.7), places=3)
        self.assertAlmostEqual(resumen.get_nota_promedio_asignatura(), (9.55 + 10) / 2)