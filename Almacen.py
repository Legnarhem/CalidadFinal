# encoding=UTF-8
__author__ = 'Gregorio y Ángel'
import shelve


class Almacen(object):
    __filename = "data"
    __store = None

    def __init__(self):
        if self.__store is not None:
            raise Exception("Ya existe una instancia de Almacen.")

    def __cargar_datos(self):
        shelf = shelve.open(self.__filename)

        self.__docentes = shelf["docentes"]
        self.__tecnicosCalidad = shelf["tecnicosCalidad"]
        self.__alumnos = shelf["alumnos"]
        self.__asignaturas = shelf["asignaturas"]
        self.__grados = shelf["grados"]
        self.__expedientes = shelf["expedientes"]
        self.__ensenyanzas = shelf["ensenyanzas"]

    def __get_docentes(self):
        return self.__docentes

    def __get_tecnicos_calidad(self):
        return self.__tecnicosCalidad

    def __get_alumnos(self):
        return self.__alumnos

    def __get_asignaturas(self):
        return self.__asignaturas

    def __get_grados(self):
        return self.__grados

    def __get_expedientes(self):
        return self.__expedientes

    def __get_ensenyanzas(self):
        return self.__ensenyanzas

    @staticmethod
    def get_instance():
        if Almacen.__store is None:
            Almacen.__store = Almacen()
            Almacen.__store.__cargar_datos()
        return Almacen.__store

    # ALUMNOS
    def obtener_alumno(self, alumno):
        alu = None
        for a in self.listar_alumnos_centro():
            if a == alumno:
                alu = a
                break
        return alu

    def listar_alumnos_asignatura(self, asignatura):
        alus = []
        for e in self.listar_expedientes_centro():
            if e.getAsignatura() == asignatura:
                alus.append(e.getAlumno())
        return None if (len(alus) == 0) else alus

    def listar_alumnos_centro(self):
        return self.__get_alumnos()

    def listar_alumnos_docente(self, docente):
        alus = []
        asig_doc = self.listar_asignaturas_docente(docente)
        if asig_doc is not None:
            for a in asig_doc:
                alumnos_asig = self.listar_alumnos_asignatura(a)
                if alumnos_asig is not None:
                    alus.extend(alumnos_asig)
        return None if (len(alus) == 0) else alus

    def listar_alumnos_grado(self, grado):
        alus = None
        for g in self.listar_grados_centro():
            if g == grado:
                alus = []
                for a in g.getAsignaturas():
                    alumnos_asig = self.listar_alumnos_asignatura(a)
                    if alumnos_asig is not None:
                        alus.extend(alumnos_asig)
                break
        return alus

    # ASIGNATURAS

    def obtener_asignatura(self, asignatura):
        asig = None
        for a in self.listar_asignaturas_centro():
            if a == asignatura:
                asig = a
                break
        return asig

    def listar_asignaturas_centro(self):
        return self.__get_asignaturas()

    def listar_asignaturas_docente(self, docente):
        asigs = []
        for e in self.listar_ensenyanzas_centro():
            if e.getDocente() == docente:
                asigs.append(e.getAsignatura())
                break
        return None if (len(asigs) == 0) else asigs

    def listar_asignaturas_grado(self, grado):
        asigs = None
        for g in self.listar_grados_centro():
            if g == grado:
                asigs = g.getAsignaturas()
                break
        return asigs

    # DOCENTE

    def obtener_docente(self, docente):
        doc = None
        for d in self.listar_docentes_centro():
            if d == docente:
                doc = d
                break
        return doc

    def listar_docentes_centro(self):
        return self.__get_docentes()

    # GRADO
    def obtener_grado(self, grado):
        gra = None
        for g in self.listar_grados_centro():
            if g == grado:
                gra = g
                break
        return gra

    def listar_grados_centro(self):
        return self.__get_grados()

    def listar_grados_docente(self, docente):
        grads = []
        asignaturas_doc = self.listar_asignaturas_docente(docente)
        if asignaturas_doc is not None:
            for a in asignaturas_doc:
                for g in self.listar_grados_centro():
                    if g.getAsignaturas().count(a) > 0:
                        if grads.count(g) == 0:
                            grads.append(g)
        return None if (len(grads) == 0) else grads

    def listar_grados_tecnico_calidad(self):
        return self.listar_grados_centro()

    # EXPEDIENTES

    def obtener_expediente(self, alumno, asignatura):
        exp = None
        for e in self.listar_expedientes_centro():
            if e.getAlumno() == alumno and e.getAsignatura() == asignatura:
                exp = e
                break
        return exp

    def listar_expedientes_alumno(self, alumno):
        exps = []
        for e in self.listar_expedientes_centro():
            if e.getAlumno() == alumno:
                exps.append(e)
        return None if (len(exps) == 0) else exps

    def listar_expedientes_centro(self):
        return self.__get_expedientes()

    def listar_expedientes_asignatura(self, asignatura):
        exps = []
        for e in self.listar_expedientes_centro():
            if e.getAsignatura() == asignatura:
                exps.append(e)
        return None if (len(exps) == 0) else exps

    def listar_expedientes_grado(self, grado):
        exps = []
        for a in self.listar_asignaturas_grado(grado):
            exps_alumno = self.listar_expedientes_asignatura(a)
            if exps_alumno is not None:
                exps.extend(exps_alumno)
        return None if (len(exps) == 0) else exps

    # TecnicoCalidad

    def obtener_tecnico_calidad(self, tecnico):
        tecn = None
        for t in self.listar_tecnicos_calidad():
            if t == tecnico:
                tecn = t
                break
        return tecn

    def listar_tecnicos_calidad(self):
        return self.__get_tecnicos_calidad()

    #Ensenyanzas

    def obtener_ensenyanza(self, docente, asignatura):
        ens = None
        for e in self.listar_ensenyanzas_centro():
            if e.getDocente() == docente and e.getAsignatura() == asignatura:
                ens = e
                break
        return ens

    def listar_ensenyanzas_centro(self):
        return self.__get_ensenyanzas()