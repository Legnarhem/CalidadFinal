# encoding=UTF-8
__author__ = 'Gregorio y Ángel'
import shelve
import random
from faker import Factory
from Entidades.Asignatura import *
from Entidades.Docente import *
from Entidades.Ensenyanza import *
from Entidades.Alumno import *
from Entidades.Expediente import *
from Entidades.TecnicoCalidad import *
from Entidades.Grado import *

def newDNI(fake,dnis):
    exists = True
    while True:
        dni = str(fake.random_int(min=10000000, max=99999999)) + fake.random_letter().upper()
        if dnis.count(dni) == 0:
            break
    return dni

def saveData(doces, tecns, alums, asigs, grads, expes, enses):
    shelf = shelve.open("data")
    shelf["docentes"] = doces
    shelf["tecnicosCalidad"] = tecns
    shelf["alumnos"] =  alums
    shelf["asignaturas"] = asigs
    shelf["grados"] = grads
    shelf["expedientes"] = expes
    shelf["ensenyanzas"] = enses

def main():
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

    print "\nAsignaturas:"
    for a in asigs:
        print a

    print "\nAlumnos:"
    print "%9s \t %15s \t%s " % ('DNI', 'Nombre', 'Apellidos')
    for i in range(0, 200):
        alu = Alumno(newDNI(fake,dnis),
                      fake.first_name().encode('utf8'), fake.last_name().encode('utf8'))
        alums.append(alu)
        for a in asigs:
            exp = Expediente(alu,a,["%.2f" % float(int(10*random.random()/0.05)*0.05) for i in range(10)])
            expes.append(exp)
        print alu

    print "\nExpedientes:"
    for e in expes:
        print e

    print "\nProfesores:"
    print "%s \t %9s \t %15s \t%s " % ('Usuario', 'DNI', 'Nombre', 'Apellidos')
    for i in range(0, 50):
        doc = Docente('docente' + str(i + 1), 'docente' + str(i + 1),
                      newDNI(fake,dnis),
                      fake.first_name().encode('utf8'), fake.last_name().encode('utf8'))
        doces.append(doc)
        ens = Ensenyanza(doc, asigs[random.randint(0,len(asigs)-1)])
        enses.append(ens)
        print doc

    print "\nEnseñanzas:"
    for e in enses:
        print e

    tecns.append(TecnicoCalidad('tecnico2','tecnico2',
                                newDNI(fake,dnis),
                                fake.first_name().encode('utf8'),fake.last_name().encode('utf8')))
    tecns.append(TecnicoCalidad('tecnico2','tecnico2',
                                newDNI(fake,dnis),
                                fake.first_name().encode('utf8'),fake.last_name().encode('utf8')))

    print "\nTecnicos de calidad:"
    for t in tecns:
        print t

    grads.append(Grado(1,"Grado en Biotecnologia",asigs))

    print "\nGrados:"
    for g in grads:
        print g
        for a in g.getAsignaturas():
            print "\t" + str(a)

    saveData(doces,tecns,alums,asigs,grads,expes,enses)

class Almacen(object):
    __filename = "data"
    __store = None

    def __init__(self):
        if self.__store is not None:
            raise Exception("Ya existe una instancia de Almacen.")


    def __cargarDatos(self):
        shelf = shelve.open(self.__filename)

        self.__docentes = shelf["docentes"]
        self.__tecnicosCalidad = shelf["tecnicosCalidad"]
        self.__alumnos = shelf["alumnos"]
        self.__asignaturas = shelf["asignaturas"]
        self.__grados = shelf["grados"]
        self.__expedientes = shelf["expedientes"]
        self.__ensenyanzas = shelf["ensenyanzas"]

    def __getDocentes(self):
        return self.__docentes

    def __getTecnicosCalidad(self):
        return self.__tecnicosCalidad

    def __getAlumnos(self):
        return self.__alumnos

    def __getAsignaturas(self):
        return self.__asignaturas

    def __getGrados(self):
        return self.__grados

    def __getExpedientes(self):
        return self.__expedientes

    def __getEnsenyanzas(self):
        return self.__ensenyanzas

    @staticmethod
    def getInstance():
        if Almacen.__store is None:
            Almacen.__store = Almacen()
            Almacen.__store.__cargarDatos()
        return Almacen.__store


#ALUMNOS

    def obtenerAlumno(self,alumno):
        alu = None
        for a in self.listarAlumnosCentro():
            if a==alumno:
                alu = a
                break
        return alu

    def listarAlumnosAsignatura(self,asignatura):
        alus = []
        for e in self.listarExpedientesCentro():
            if e.getAsignatura() == asignatura:
                alus.append(e.getAlumno())
        return None if(len(alus)==0) else alus

    def listarAlumnosCentro(self):
        return self.__getAlumnos()

    def listarAlumnosGrado(self,grado):
        alus = None
        for g in self.listarGradosCentro():
            if g == grado:
                alus = []
                for a in g.getAsignaturas():
                    alusA = self.listarAlumnosAsignatura(a)
                    if alusA is not None:
                        alus.extend(alusA)
                break
        return alus

# ASIGNATURAS

    def obtenerAsignatura(self,asignatura):
        asig = None
        for a in self.listarAsignaturasCentro():
            if a==asignatura:
                asig = a
                break
        return asig

    def listarAsignaturasCentro(self):
        return self.__getAsignaturas()

    def listarAsignaturasDocente(self,docente):
        asigs = []
        for e in self.listarEnsenyanzasCentro():
            if e.getDocente() == docente:
                asigs.append(e.getAsignatura())
                break
        return None if (len(asigs)==0) else asigs

    def listarAsignaturasGrado(self,grado):
        asigs = None
        for g in self.listarGradosCentro():
            if g == grado:
                asigs = g.getAsignaturas()
                break
        return asigs

# DOCENTE

    def obtenerDocente(self,docente):
        doc = None
        for d in self.listarDocentesCentro():
            if d==docente:
                doc = d
                break
        return doc

    def listarDocentesCentro(self):
        return self.__getDocentes()


# GRADO

    def obtenerGrado(self,grado):
        gra = None
        for g in self.listarGradosCentro():
            if g == grado:
                gra = g
                break
        return gra

    def listarGradosCentro(self):
        return self.__getGrados()

    def listarGradosDocente(self,docente):
        grads = []
        asigD = self.listarAsignaturasDocente(docente)
        if asigD is not None:
            for a in asigD:
                for g in self.listarGradosCentro():
                    if g.getAsignaturas().count(a)>0:
                        if grads.count(g)==0:
                            grads.append(g)
        return None if (len(grads)==0) else grads

    def listarGradosTecnicoCalidad(self):
        return self.listarGradosCentro()

# EXPEDIENTES

    def obtenerExpediente(self, alumno, asignatura):
        exp = None
        for e in self.listarExpedientesCentro():
            if e.getAlumno() == alumno and e.getAsignatura() == asignatura:
                exp = e
                break
        return exp

    def listarExpedientesAlumno(self,alumno):
        exps = []
        for e in self.listarExpedientesCentro():
            if e.getAlumno() == alumno:
                exps.append(e)
        return None if(len(exps)==0) else exps

    def listarExpedientesCentro(self):
        return self.__getExpedientes()

    def listarExpedientesAsignatura(self,asignatura):
        exps = []
        for e in self.listarExpedientesCentro():
            if e.getAsignatura() == asignatura:
                exps.append(e)
        return None if(len(exps)==0) else exps


    def listarExpedientesGrado(self,grado):
        exps = []
        for a in self.listarAsignaturasGrado(grado):
            expsA = self.listarExpedientesAsignatura(a)
            if expsA is not None:
                exps.extend(expsA)
        return None if(len(exps)==0) else exps

#TecnicoCalidad

    def obtenerTecnicoCalidad(self,tecnico):
        tecn = None
        for t in self.listarTecnicosCalidad():
            if t == tecnico:
                tecn = t
                break
        return tecn

    def listarTecnicosCalidad(self):
        return self.__getTecnicosCalidad()

#Ensenyanzas

    def obtenerEnsenyanza(self, docente, asignatura):
        ens = None
        for e in self.listarEnsenyanzasCentro():
            if e.getDocente() == docente and e.getAsignatura() == asignatura:
                ens = e
                break
        return ens

    def listarEnsenyanzasCentro(self):
        return self.__getEnsenyanzas()

if __name__ == '__main__':
    # main()
    #almacen = Almacen.getInstance()
    #print len(almacen.listarAlumnosAsignatura(almacen.obtenerAsignatura(Asignatura(1,None))))
    #for i in almacen.listarAsignaturasDocente(almacen.obtenerDocente(Docente(None,None,"83913575E",None, None))):
    #    print i
    pass