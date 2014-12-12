# encoding=UTF-8
"""Módulo Almacen del Gestor Académico
"""
__author__ = 'Gregorio y Ángel'
import shelve


class Almacen(object):
    """Esta clase es un almacen de datos del Gestor Académico.
        Es una clase estática y para obtener una instancia debe de llamarse al método Almacen.get_instance()
    """

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
        """Obtiene una instancia de Almacen con datos precargados.
        :return:Instancia de Almacen (Almacen)
        """
        if Almacen.__store is None:
            Almacen.__store = Almacen()
            Almacen.__store.__cargar_datos()
        return Almacen.__store

    # ALUMNOS
    def obtener_alumno(self, alumno):
        """Obtiene un alumno indicado.
        :param alumno:Instancia de alumno (Alumno)
        :return:Alumno (Alumno) si existe o None en caso contrario
        """
        alu = None
        for a in self.listar_alumnos_centro():
            if a == alumno:
                alu = a
                break
        return alu

    def listar_alumnos_asignatura(self, asignatura):
        """Obtiene una lista de los alumnos expedientados en la asignatura indicada.
        :param asignatura:Instancia de asignatura (Asignatura)
        :return:Lista de Alumnos (list) si existe asignatura y alumnos en ella o None en caso contrario
        """
        alus = []
        for e in self.listar_expedientes_centro():
            if e.getAsignatura() == asignatura:
                alus.append(e.getAlumno())
        return None if (len(alus) == 0) else alus

    def listar_alumnos_centro(self):
        """Obtiene una lista de los alumnos involucrados en el centro académico.
        :return:Lista de Alumnos (list)
        """
        return self.__get_alumnos()

    def listar_alumnos_docente(self, docente):
        """Obtiene una lista de los alumnos expedientados en alguna asignatura que involucre al docente indicado.
        :param docente:Instancia de docente (Docente)
        :return:Lista de Alumnos (list) si existe docente con asignatura(s) y alumnos en ella(s)
        o None en caso contrario
        """
        alus = []
        asig_doc = self.listar_asignaturas_docente(docente)
        if asig_doc is not None:
            for a in asig_doc:
                alumnos_asig = self.listar_alumnos_asignatura(a)
                if alumnos_asig is not None:
                    alus.extend(alumnos_asig)
        return None if (len(alus) == 0) else alus

    def listar_alumnos_grado(self, grado):
        """Obtiene una lista de los alumnos involucrados en un grado/curso indicado.
        :param grado:Instancia de grado/curso (Grado)
        :return:Lista de alumnos (list) si existen o None en caso contrario
        """
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
        """Obtiene una asignatura indicada.
        :param asignatura:Instancia de asignatura (Asignatura)
        :return:Asignatura (Asignatura) si existe o None en caso contrario
        """
        asig = None
        for a in self.listar_asignaturas_centro():
            if a == asignatura:
                asig = a
                break
        return asig

    def listar_asignaturas_centro(self):
        """Obtiene una lista de los asignaturas impartidas en el centro académico.
        :return:Lista de asignaturas (list)
        """
        return self.__get_asignaturas()

    def listar_asignaturas_docente(self, docente):
        """Obtiene una lista de las asignaturas que involucra al docente indicado.
        :param docente:Instancia de docente (Docente)
        :return:Lista de asignaturas (list) si existe docente con asignatura(s) o None en caso contrario
        """
        asigs = []
        for e in self.listar_ensenyanzas_centro():
            if e.getDocente() == docente:
                asigs.append(e.getAsignatura())
                break
        return None if (len(asigs) == 0) else asigs

    def listar_asignaturas_grado(self, grado):
        """Obtiene una lista de las asignaturas que estan asociadas al grado/curso indicado.
        :param grado:Instancia de grado/curso (Grado)
        :return:Lista de asignaturas (list) si existe grado/curso con asignatura(s) o None en caso contrario
        """
        asigs = None
        for g in self.listar_grados_centro():
            if g == grado:
                asigs = g.getAsignaturas()
                break
        return asigs

    # DOCENTE

    def obtener_docente(self, docente):
        """Obtiene un docente indicado.
        :param docente:Instancia de docente (Docente)
        :return:Docente (Docente) si existe o None en caso contrario
        """
        doc = None
        for d in self.listar_docentes_centro():
            if d == docente:
                doc = d
                break
        return doc

    def listar_docentes_centro(self):
        """Obtiene una lista de los docentes involucrados en el centro académico.
        :return:Lista de docentes (list)
        """
        return self.__get_docentes()

    # GRADO
    def obtener_grado(self, grado):
        """Obtiene un grado/curso indicado.
        :param grado:Instancia de grado/curso (Grado)
        :return:Grado/curso (Grado) si existe o None en caso contrario
        """
        gra = None
        for g in self.listar_grados_centro():
            if g == grado:
                gra = g
                break
        return gra

    def listar_grados_centro(self):
        """Obtiene una lista de los grados/cursos involucrados en el centro académico.
        :return:Lista de grados/cursos (list)
        """
        return self.__get_grados()

    def listar_grados_docente(self, docente):
        """Obtiene una lista de las grados/cursos que involucra al docente indicado.
        :param docente:Instancia de docente (Docente)
        :return:Lista de grados/crusos (list) si existe docente con grados(s)/curso(s) o None en caso contrario
        """
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
        """Obtiene una lista de los tecnicos de calidad involucrados en el centro académico.
        :return:Lista de tecnicos de calidad (list)
        """
        return self.listar_grados_centro()

    # EXPEDIENTES

    def obtener_expediente(self, alumno, asignatura):
        """Obtiene el expediente de un alumno indicado en una asignatura indicada.
        :param alumno:Instancia de alumno (Alumno)
        :param asignatura:Instancia de asignatura (Asignatura)
        :return:Expediente (Expediente) si existe alumno y asignatura y este primero se encuentra
        expedientado en la asignatura o None en caso contrario
        """
        exp = None
        for e in self.listar_expedientes_centro():
            if e.getAlumno() == alumno and e.getAsignatura() == asignatura:
                exp = e
                break
        return exp

    def listar_expedientes_alumno(self, alumno):
        """Obtiene una lista de las expedientes que involucran al alumno indicado.
        :param alumno:Instancia de alumno (Alumno)
        :return:Lista de expedientes (list) si existe alumno y se encuentra expedientado en alguna asignatura o None en
        caso contrario
        """
        exps = []
        for e in self.listar_expedientes_centro():
            if e.getAlumno() == alumno:
                exps.append(e)
        return None if (len(exps) == 0) else exps

    def listar_expedientes_centro(self):
        """Obtiene una lista de los expedientes existentes en el centro académico.
        :return:Lista de expedientes (list)
        """
        return self.__get_expedientes()

    def listar_expedientes_asignatura(self, asignatura):
        """Obtiene una lista de los expedientes asociados a la asignatura indicada.
        :param asignatura:Instancia de asignatura (Asignatura)
        :return:Lista de expedientes (list) si existe asignatura y tiene asociados expedientes o None en caso contrario
        """
        exps = []
        for e in self.listar_expedientes_centro():
            if e.getAsignatura() == asignatura:
                exps.append(e)
        return None if (len(exps) == 0) else exps

    def listar_expedientes_grado(self, grado):
        """Obtiene una lista de los expedientes existentes asociados a alguna asignatura del grado/curso indicado.
        :param grado:Instancia de grado/curso (Grado)
        :return:Lista de expedientes (list) si existe grado/curso y tiene asignatura(s) con expediente(s) o None en
        caso contrario
        """
        exps = []
        for a in self.listar_asignaturas_grado(grado):
            exps_alumno = self.listar_expedientes_asignatura(a)
            if exps_alumno is not None:
                exps.extend(exps_alumno)
        return None if (len(exps) == 0) else exps

    # TecnicoCalidad

    def obtener_tecnico_calidad(self, tecnico):
        """Obtiene un tecnico indicado.
        :param tecnico:Instancia de tecnico (Tecnico)
        :return:Tecnico (Tecnico) si existe o None en caso contrario
        """
        tecn = None
        for t in self.listar_tecnicos_calidad():
            if t == tecnico:
                tecn = t
                break
        return tecn

    def listar_tecnicos_calidad(self):
        """Obtiene una lista de los tecnicos de calidad existentes en el centro académico.
        :return:Lista de tecnicos de calidad (list)
        """
        return self.__get_tecnicos_calidad()

    #Ensenyanzas

    def obtener_ensenyanza(self, docente, asignatura):
        """Obtiene la ensenyanza de un docente en una asignatura.
        :param docente:Instancia de docente (Docente)
        :param asignatura:Instancia de asignatura (Asignatura)
        :return:Ensenyanza (Ensenyanza) si existe docente y asignatura y este primero imparte
        en la asignatura o None en caso contrario
        """
        ens = None
        for e in self.listar_ensenyanzas_centro():
            if e.getDocente() == docente and e.getAsignatura() == asignatura:
                ens = e
                break
        return ens

    def listar_ensenyanzas_centro(self):
        """Obtiene una lista de las enseñanzas impartidas en el centro académico.
        :return:Lista de enseñanzas (list)
        """
        return self.__get_ensenyanzas()