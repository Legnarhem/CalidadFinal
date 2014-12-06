# encoding=UTF-8

__author__ = 'Gregorio y Ángel'
import os
class Terminal:

    def __init__(self):
        self.setAlumnoController(None)
        self.setAsignaturaController(None)
        self.setCentroController(None)
        self.setGradoController(None)
        self.setSesionController(None)
        self.setSesion(None)

    def getAlumnoController(self):
        return self.__alumnoController

    def getAsignaturaController(self):
        return self.__asignaturaController

    def getCentroController(self):
        return self.__centroController

    def getGradoController(self):
        return self.__gradoController

    def getSesionController(self):
        return self.__sesionController

    def getSesion(self):
        return self.__sesion

    def setAlumnoController(self, alumnoController):
        self.__alumnoController = alumnoController

    def setAsignaturaController(self, asignaturaController):
        self.__asignaturaController = asignaturaController

    def setCentroController(self, centroController):
        self.__centroController = centroController

    def setGradoController(self, gradoController):
        self.__gradoController = gradoController

    def setSesionController(self, sesionController):
        self.__sesionController = sesionController

    def setSesion(self,sesion):
        self.__sesion = sesion

    def iniciar(self):

        strLogo1 = """
   _____           _
  / ____|         | |
 | |  __  ___  ___| |_ ___  _ __
 | | |_ |/ _ \/ __| __/ _ \| '__|
 | |__| |  __/\__ \ || (_) | |
  \_____|\___||___/\__\___/|_|
"""
        strLogo2 = """
                        _                _
     /\                | |              (_)
    /  \   ___ __ _  __| | ___ _ __ ___  _  ___ ___
   / /\ \ / __/ _` |/ _` |/ _ \ '_ ` _ \| |/ __/ _ \\
  / ____ \ (_| (_| | (_| |  __/ | | | | | | (_| (_) |
 /_/    \_\___\__,_|\__,_|\___|_| |_| |_|_|\___\___/ ®

"""
        strCopy1 =  "\tAngel Crujera & Gregorio L. Mármol"
        strCopy2 = "\tCopyright 2015 – Todos los derechos reservados"

        print strLogo1
        print strLogo2
        print strCopy1
        print strCopy2
        print

        raw_input("Presione una tecla para continuar...")

        while self.getSesion() is None:
            self.__clear()
            self.__login()

        if self.getSesion().getTipo() == "Docente":
            while True:
                self.__menuDocente()
        elif self.getSesion().getTipo() == "TecnicoCalidad":
            while True:
                self.__menuTecnico()


    def __clear(self):
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")

    def __login(self):
        strLogin = "Por favor, identifiquese."
        print strLogin
        print
        usr = raw_input("Usuario: \t")
        pwd = raw_input("Contraseña: \t")
        self.setSesion(self.getSesionController().obtenerSesion(usr,pwd))
        if self.getSesion() is None:
            print "Credenciales incorrectos."
            raw_input(" Presione cualquier tecla... ")

    def __welcome(self):
        self.__clear()
        print "-----------------------o--------------------------"
        print "         Bienvenido de nuevo, %s" % (self.getSesion().getDNI())
        print "-----------------------o--------------------------"

    def __menuDocente(self):

        self.__welcome()

        print " Elija opcion:"
        print "\t 1) Gestionar asignaturas"
        print "\t 0) Salir"

        opc = -1

        while not (0 <= opc <= 3):
            opc = int(raw_input(" >> "))

        if opc == 1:
            asignatura = self.__menuAsignaturas()
            self.__subMenuAsignaturas(asignatura)
        else:
            exit()

    def __subMenuAlumnos(self, alumno):
        if alumno is not None:
            self.__clear()

            print " Elija opcion:"
            print "\t 1) Mostrar media de alumno"
            print "\t 2) Mostrar rangos de alumno"
            print "\t 0) Volver"

            opc = -1

            while not (0 <= opc <= 2):
                opc = int(raw_input(" >> "))

            if opc == 1:
                self.__subMenuMediaAlumnoCentro(alumno)
            elif opc == 2:
                self.__subMenuRangosAlumnoCentro(alumno)
            else:
                pass

    def __subMenuAsignaturas(self, asignatura):
        if asignatura is not None:
            self.__clear()

            print " Elija opcion:"
            print "\t 1) Mostrar media de alumno"
            print "\t 2) Mostrar media de asignatura"
            print "\t 3) Mostrar rangos de asignatura"
            print "\t 0) Volver"

            opc = -1

            while not (0 <= opc <= 3):
                opc = int(raw_input(" >> "))

            if opc == 1:
                alumno = self.__subMenuAlumnosAsignatura(asignatura)
                self.__subMenuMediaAlumnoAsignatura(alumno, asignatura)
            elif opc == 2:
                self.__subMenuMediaAsignatura(asignatura)
            elif opc == 3:
                self.__subMenuRangosAsignatura(asignatura)
            else:
                pass

    def __subMenuGrados(self, grado):
        if grado is not None:
            self.__clear()

            print " Elija opcion:"
            print "\t 1) Mostrar media grado"
            print "\t 2) Mostrar rangos grado"
            print "\t 3) Mostrar matriculas y menciones"
            print "\t 0) Volver"

            opc = -1

            while not (0 <= opc <= 3):
                opc = int(raw_input(" >> "))

            if opc == 1:
                self.__subMenuMediaGrado(grado)
            elif opc == 2:
                self.__subMenuRangosGrado(grado)
            elif opc == 3:
                self.__subMenuMatriculasYMencionesGrado(grado)
            else:
                pass

    def __subMenuAlumnosAsignatura(self, asignatura):
        if asignatura is not None:
            self.__clear()
            i = 0
            opc = -1
            misAlumnos = self.getAlumnoController().obtenerAlusAsignatura(asignatura.getCodigo(), self.getSesion())
            if len(misAlumnos) > 0:
                print " Elija alumno:"
                while i < len(misAlumnos):
                    print "\t%d) %s, %s" % (i+1, misAlumnos[i].getApellidos(), misAlumnos[i].getNombre())
                    i += 1
                while not (1 <= opc <= len(misAlumnos)):
                    opc = int(raw_input(" >> "))
                return misAlumnos[opc-1]
            else:
                print "Usted no tiene acceso a alumno alguno"
                raw_input(" Presione cualquier tecla... ")
                return None
        else:
            return None

    def __subMenuMediaAlumnoAsignatura(self, alumno, asignatura):
        if alumno is not None:
            self.__clear()
            media = self.getAlumnoController().obtenerMedia(alumno.getDNI(), asignatura.getCodigo(), self.getSesion())
            if  media is not None:
                print " La media de %s %s en la asignatura es %f" % (alumno.getNombre(), alumno.getApellidos(), media)
            else:
                print "Usted no tiene acceso a la media del alumno"
            raw_input(" Presione cualquier tecla... ")

    def __subMenuMediaAlumnoCentro(self, alumno):
        if alumno is not None:
            self.__clear()
            media = self.getAlumnoController().obtenerMediaCentro(alumno.getDNI(), self.getSesion())
            if  media is not None:
                print " La media global de %s %s en el centro es %f" % (alumno.getNombre(), alumno.getApellidos(), media)
            else:
                print "Usted no tiene acceso a la media global del alumno"
            raw_input(" Presione cualquier tecla... ")

    def __subMenuMediaGrado(self, grado):
        if grado is not None:
            self.__clear()
            media = self.getGradoController().obtenerMedia(grado.getCodigo(), self.getSesion())
            if  media is not None:
                print " La media del grado de \"%s\" es de %f" % (grado.getNombre(), media)
            else:
                print "Usted no tiene acceso a la media global del grado"
            raw_input(" Presione cualquier tecla... ")

    def __subMenuMediaAsignatura(self, asignatura):
        if asignatura is not None:
            self.__clear()
            media = self.getAsignaturaController().obtenerMedia(asignatura.getCodigo(),self.getSesion())
            if  media is not None:
                print " El promedio de nota de la asignatura de %s es %f" % (asignatura.getNombre(), media)
            else:
                print "Usted no tiene acceso a la media de la asignatura"
            raw_input(" Presione cualquier tecla... ")

    def __subMenuRangosAlumnoCentro(self, alumno):
        if alumno is not None:
            self.__clear()
            rango = self.getAlumnoController().obtenerRango(alumno.getDNI(), self.getSesion())
            if rango is not None:
                print " Estadisticas del alumno %s %s." % (alumno.getNombre(), alumno.getApellidos())
                print "\tNumero de suspensos totales: %d" % rango.getSuspensos()
                print "\tNumero de aprobados totales: %d" % rango.getAprobados()
                print "\tNumero de notables totales: %d" % rango.getNotables()
                print "\tNumero de sobresalientes totales: %d" % rango.getSobresalientes()
            else:
                print "Usted no tiene acceso a los rangos del alumno"
            raw_input(" Presione cualquier tecla... ")

    def __subMenuRangosAsignatura(self, asignatura):
        if asignatura is not None:
            self.__clear()
            rango = self.getAsignaturaController().obtenerRango(asignatura.getCodigo(), self.getSesion())
            if rango is not None:
                print " Estadisticas de la asignatura %s." % asignatura.getNombre()
                print "\tNumero de suspensos totales: %d" % rango.getSuspensos()
                print "\tNumero de aprobados totales: %d" % rango.getAprobados()
                print "\tNumero de notables totales: %d" % rango.getNotables()
                print "\tNumero de sobresalientes totales: %d" % rango.getSobresalientes()
            else:
                print "Usted no tiene acceso a los rangos de la asignatura"
            raw_input(" Presione cualquier tecla... ")

    def __subMenuRangosGrado(self, grado):
        if grado is not None:
            self.__clear()
            rango = self.getGradoController().obtenerRango(grado.getCodigo(), self.getSesion())
            if rango is not None:
                print " Estadisticas del grado de \"%s\"." % grado.getNombre()
                print "\tNumero de suspensos totales: %d" % rango.getSuspensos()
                print "\tNumero de aprobados totales: %d" % rango.getAprobados()
                print "\tNumero de notables totales: %d" % rango.getNotables()
                print "\tNumero de sobresalientes totales: %d" % rango.getSobresalientes()
            else:
                print "Usted no tiene acceso a los rangos del grado"
            raw_input(" Presione cualquier tecla... ")

    def __subMenuMatriculasYMencionesGrado(self, grado):
        if grado is not None:
            self.__clear()
            matriculasYMenciones = self.getGradoController().obtenerMatriculasYMenciones(grado.getCodigo(), self.getSesion())
            if matriculasYMenciones is not None:
                print " Estadisticas del grado de \"%s\"." % grado.getNombre()
                print "\tNumero de menciones totales: %d" % matriculasYMenciones.getMenciones()
                print "\tNumero de matriculas totales: %d" % matriculasYMenciones.getMatriculas()
            else:
                print "Usted no tiene acceso a las matriculas y menciones del grado"
            raw_input(" Presione cualquier tecla... ")

    def __subMenuResumenCentro(self):
        resumen = self.getCentroController().obtenerResumen(self.getSesion())
        if resumen is not None:
            print "Estado del centro."
            print "------------------"
            print "Nota promedio de alumno     \t%f" % resumen.getNotaPromedioAlumno()
            print "Nota promedio de asignatura \t%f" % resumen.getNotaPromedioAsignatura()
            print

    def __menuTecnico(self):
        self.__welcome()

        self.__subMenuResumenCentro()

        print " Elija opcion:"
        print "\t 1) Gestionar alumnos"
        print "\t 2) Gestionar asignaturas"
        print "\t 3) Gestionar grados"
        print "\t 0) Salir"

        opc = -1

        while not (0 <= opc <= 3):
            opc = int(raw_input(" >> "))

        if opc == 1:
            alumno = self.__menuAlumnos()
            self.__subMenuAlumnos(alumno)
        elif opc == 2:
            asignatura = self.__menuAsignaturas()
            self.__subMenuAsignaturas(asignatura)
        elif opc == 3:
            grado = self.__menuGrados()
            self.__subMenuGrados(grado)
        else:
            exit()

    def __menuAlumnos(self):
        self.__clear()
        i = 0
        opc = -1
        misAlumnos = self.getAlumnoController().listar(self.getSesion())
        if len(misAlumnos) > 0:
            print " Elija alumno:"
            while i < len(misAlumnos):
                print "\t%d) %s\t%s, %s" % (i+1, misAlumnos[i].getDNI(), misAlumnos[i].getApellidos(), misAlumnos[i].getNombre())
                i += 1
            while not (1 <= opc <= len(misAlumnos)):
                opc = int(raw_input(" >> "))
            return misAlumnos[opc-1]
        else:
            print " Usted no tiene acceso a alumno alguno."
            raw_input(" Presione cualquier tecla... ")
            return None

    def __menuAsignaturas(self):
        self.__clear()
        i = 0
        opc = -1
        misAsignaturas = self.getAsignaturaController().listar(self.getSesion())
        if len(misAsignaturas) > 0:
            print " Elija asignatura:"
            while i < len(misAsignaturas):
                print "\t%d) %s" % (i+1, misAsignaturas[i].getNombre())
                i += 1
            while not (1 <= opc <= len(misAsignaturas)):
                opc = int(raw_input(" >> "))
            return misAsignaturas[opc-1]
        else:
            print " Usted no tiene acceso a asignatura alguna."
            raw_input(" Presione cualquier tecla... ")
            return None

    def __menuGrados(self):
        self.__clear()
        i = 0
        opc = -1
        misGrados = self.getGradoController().listar(self.getSesion())
        if len(misGrados) > 0:
            print " Elija grado:"
            while i < len(misGrados):
                print "\t%d) %s" % (i+1, misGrados[i].getNombre())
                i += 1
            while not (1 <= opc <= len(misGrados)):
                opc = int(raw_input(" >> "))
            return misGrados[opc-1]
        else:
            print " Usted no tiene acceso a grado alguno."
            raw_input(" Presione cualquier tecla... ")
            return None

    def __menuMisAlumnos(self):
        i = 0
        opc = -1
        misAlumnos = self.getAlumnoController().listar(self.getSesion())
        if len(misAlumnos) > 0:
            print " Elija alumno:"
            while i < len(misAlumnos):
                print "\t%d) %s, %s" % (i+1, misAlumnos[i].getApellidos(), misAlumnos[i].getNombre())
                i += 1
            while not (1 <= opc <= len(misAlumnos)):
                opc = int(raw_input(" >> "))
            return misAlumnos[opc-1]
        else:
            print "Usted no tiene acceso a alumno alguno"
            raw_input(" Presione cualquier tecla... ")
            return None



    def __menu(self):
        pass