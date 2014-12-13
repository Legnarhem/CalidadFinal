# encoding=UTF-8
"""Módulo creados de datos de prueba
"""
__author__ = 'Gregorio y Ángel'
import shelve
import random

from faker import Factory

from src.Entidades.Asignatura import *
from src.Entidades.Expediente import *
from src.Entidades.TecnicoCalidad import *
from src.Entidades.Docente import *
from src.Entidades.Ensenyanza import *
from src.Entidades.Grado import *
from src.Entidades.Alumno import *


def new_dni(fake, dnis):
    """Obtiene una DNI no existente en el conjutno de entrada.
    :param fake:Instancia de Faker.Factory (Factory)
    :param dnis:Instancia de lista (list)
    :return:DNI (str)
    """
    dni = None
    while True:
        dni = str(fake.random_int(min=10000000, max=99999999)) + fake.random_letter().upper()
        if dnis.count(dni) == 0:
            break
    return dni


def save_data(doces, tecns, alums, asigs, grads, expes, enses):
    """Guarda los datos en un fichero mediante shelve.
    :param doces:Instancia de lista (list)
    :param tecns:Instancia de lista (list)
    :param alums:Instancia de lista (list)
    :param asigs:Instancia de lista (list)
    :param grads:Instancia de lista (list)
    :param expes:Instancia de lista (list)
    :param enses:Instancia de lista (list)
    """
    shelf = shelve.open("data")
    shelf["docentes"] = doces
    shelf["tecnicosCalidad"] = tecns
    shelf["alumnos"] = alums
    shelf["asignaturas"] = asigs
    shelf["grados"] = grads
    shelf["expedientes"] = expes
    shelf["ensenyanzas"] = enses


def mostrar_lista(lista):
    """Imprime los elementos de una lista.
    :param lista:Instancia de lista (list)
    """
    for elemento in lista:
        print(elemento)


def main():
    """Crea y guarda las instancias de prueba.
    """
    asigs = list()
    grads = list()
    doces = list()
    enses = list()
    alums = list()
    expes = list()
    tecns = list()
    dnis = list()

    fake = Factory.create('es_ES')

    asigs.append(Asignatura(1, 'Quimica general'))
    asigs.append(Asignatura(2, 'Fisica'))
    asigs.append(Asignatura(3, 'Algebra y fundamentos de analisis'))
    asigs.append(Asignatura(4, 'Informatica'))
    asigs.append(Asignatura(5, 'Biologia celular'))
    asigs.append(Asignatura(6, 'Bioquimica: biomoleculas'))
    asigs.append(Asignatura(7, 'Biologia animal y vegetal'))
    asigs.append(Asignatura(8, 'Quimica organica'))
    asigs.append(Asignatura(9, 'Genetica'))
    asigs.append(Asignatura(10, 'Analisis matematico'))

    print("\nAsignaturas:")
    mostrar_lista(asigs)

    print("\nAlumnos:")
    print("%9s \t %15s \t%s " % ('DNI', 'Nombre', 'Apellidos'))
    for i in range(0, 200):
        alu = Alumno(new_dni(fake, dnis),
                     fake.first_name().encode('utf8'), fake.last_name().encode('utf8'))
        alums.append(alu)
        for a in asigs:
            exp = Expediente(alu, a, ["%.2f" % float(int(10 * random.random() / 0.05) * 0.05) for i in range(10)])
            expes.append(exp)
        print(alu)

    print("\nExpedientes:")
    mostrar_lista(expes)

    print("\nProfesores:")
    print("%10s \t %9s \t %15s \t%s " % ('Usuario', 'DNI', 'Nombre', 'Apellidos'))
    for i in range(0, 50):
        dni = new_dni(fake, dnis)
        doc = Docente('u' + dni, 'docente' + str(i + 1), dni, fake.first_name().encode('utf8'),
                      fake.last_name().encode('utf8'))
        doces.append(doc)
        ens = Ensenyanza(doc, asigs[random.randint(0, len(asigs) - 1)])
        enses.append(ens)
        print(doc)

    print("\nEnseñanzas:")
    mostrar_lista(enses)

    dni = new_dni(fake, dnis)
    tecns.append(TecnicoCalidad('u' + dni, 'tecnico', dni,
                                fake.first_name().encode('utf8'), fake.last_name().encode('utf8')))
    dni = new_dni(fake, dnis)
    tecns.append(TecnicoCalidad('u' + dni, 'tecnico', dni,
                                fake.first_name().encode('utf8'), fake.last_name().encode('utf8')))

    print("\nTecnicos de calidad:")
    print("%10s \t %9s \t %15s \t%s " % ('Usuario', 'DNI', 'Nombre', 'Apellidos'))
    mostrar_lista(tecns)

    grads.append(Grado(1, "Grado en Biotecnologia", asigs))

    print("\nGrados:")
    for g in grads:
        print(g)
        for a in g.getAsignaturas():
            print("\t" + str(a))

    save_data(doces, tecns, alums, asigs, grads, expes, enses)


if __name__ == '__main__':
    main()