# encoding=UTF-8
"""Módulo Terminal
"""

__author__ = 'Gregorio y Ángel'
import os


class Terminal:
    """Esta clase es la vista del programa
    """

    def __init__(self):
        self.set_alumno_controller(None)
        self.set_asignatura_controller(None)
        self.set_centro_controller(None)
        self.set_grado_controller(None)
        self.set_sesion_controller(None)
        self.set_sesion(None)

    def get_alumno_controller(self):
        """Obtiene el controlador de la entidad alumno
        :return: Controlador alumno (AlumnoController)
        """
        return self.__alumnoController

    def get_asignatura_controller(self):
        """Obtiene el controlador de la entidad asignatura
        :return: Controlador asignatura (AsignaturaController)
        """
        return self.__asignaturaController

    def get_centro_controller(self):
        """Obtiene el controlador de la entidad centro
        :return: Controlador centro (CentroController)
        """
        return self.__centroController

    def get_grado_controller(self):
        """Obtiene el controlador de la entidad grado
        :return: Controlador grado (GradoController)
        """
        return self.__gradoController

    def get_sesion_controller(self):
        """Obtiene el controlador de la entidad sesion
        :return: Controlador sesion (SesionController)
        """
        return self.__sesionController

    def get_sesion(self):
        """Obtiene la sesión activa asignada a este terminal
        :return: Sesión (Sesion)
        """
        return self.__sesion

    def set_alumno_controller(self, alumno_controller):
        """Actualiza el controlador de la entidad alumno
        :param alumno_controller: Controlador de alumno (AlumnoController)
        :return: None
        """
        self.__alumnoController = alumno_controller

    def set_asignatura_controller(self, asignatura_controller):
        """Actualiza el controlador de la entidad asignatura
        :param asignatura_controller: Controlador de asignatura (AsignaturaController)
        :return: None
        """
        self.__asignaturaController = asignatura_controller

    def set_centro_controller(self, centro_controller):
        """Actualiza el controlador de la entidad centro
        :param centro_controller: Controlador de centro (CentroController)
        :return: None
        """
        self.__centroController = centro_controller

    def set_grado_controller(self, grado_controller):
        """Actualiza el controlador de la entidad grado
        :param grado_controller: Controlador de grado (GradoController)
        :return: None
        """
        self.__gradoController = grado_controller

    def set_sesion_controller(self, sesion_controller):
        """Actualiza el controlador de la entidad sesión
        :param sesion_controller: Controlador de sesión (SesionController)
        :return: None
        """
        self.__sesionController = sesion_controller

    def set_sesion(self, sesion):
        """Actualiza la sesión activa del terminal
        :param sesion: Sesión activa (Sesion)
        :return: None
        """
        self.__sesion = sesion

    def iniciar(self):
        """Este método en la primera pantalla que nos aparece al iniciar el programa
        :return: None
        """

        str_logo1 = """
   _____           _
  / ____|         | |
 | |  __  ___  ___| |_ ___  _ __
 | | |_ |/ _ \/ __| __/ _ \| '__|
 | |__| |  __/\__ \ || (_) | |
  \_____|\___||___/\__\___/|_|
"""
        str_logo2 = """
                        _                _
     /\                | |              (_)
    /  \   ___ __ _  __| | ___ _ __ ___  _  ___ ___
   / /\ \ / __/ _` |/ _` |/ _ \ '_ ` _ \| |/ __/ _ \\
  / ____ \ (_| (_| | (_| |  __/ | | | | | | (_| (_) |
 /_/    \_\___\__,_|\__,_|\___|_| |_| |_|_|\___\___/ ®

"""
        str_copy1 = "\tAngel Crujera & Gregorio L. Mármol"
        str_copy2 = "\tCopyright 2015 – Todos los derechos reservados"

        print str_logo1
        print str_logo2
        print str_copy1
        print str_copy2
        print

        raw_input("Presione una tecla para continuar...")

        while self.get_sesion() is None:
            self.__clear()
            self.__login()

        if self.get_sesion().getTipo() == "Docente":
            while True:
                self.__menu_docente()
        elif self.get_sesion().getTipo() == "TecnicoCalidad":
            while True:
                self.__menu_tecnico()

    def __clear(self):
        """Limpia el terminal
        :return:
        """
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")

    def __login(self):
        """Método que gestiona el log en la aplicación
        :return: None
        """
        str_login = "Por favor, identifiquese."
        print str_login
        print
        usr = raw_input("Usuario: \t")
        pwd = raw_input("Contraseña: \t")
        self.set_sesion(self.get_sesion_controller().obtenerSesion(usr, pwd))
        if self.get_sesion() is None:
            print "Credenciales incorrectos."
            raw_input(" Presione cualquier tecla... ")

    def __welcome(self):
        """Imprime la bienvenida al usuario que ha iniciado sesión
        :return: None
        """
        self.__clear()
        print "-----------------------o--------------------------"
        print "         Bienvenido de nuevo, %s" % (self.get_sesion().getDNI())
        print "-----------------------o--------------------------"

    def __menu_docente(self):
        """Imprime el menú de un usuario registrado como docente y gestiona la siguiente pantalla
        :return: None
        """

        self.__welcome()

        print " Elija opcion:"
        print "\t 1) Gestionar asignaturas"
        print "\t 0) Salir"

        opc = -1

        while not (0 <= opc <= 3):
            opc = int(raw_input(" >> "))

        if opc == 1:
            asignatura = self.__menu_asignaturas()
            self.__sub_menu_asignaturas(asignatura)
        else:
            exit()

    def __sub_menu_alumnos(self, alumno):
        """Imprime un menú con diferentes opciones sobre un alumno seleccionado y gestiona el paso a la siguiente pantalla
        :param alumno: Alumno (Alumno)
        :return: None
        """
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
                self.__sub_menu_media_alumno_centro(alumno)
            elif opc == 2:
                self.__sub_menu_rangos_alumno_centro(alumno)
            else:
                pass

    def __sub_menu_asignaturas(self, asignatura):
        """Imprime un menú con diferentes opciones sobre una asignatura seleccionada y gestiona el paso a la siguiente pantalla
        :param asignatura: Asignatura (Asignatura)
        :return: None
        """
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
                alumno = self.__sub_menu_alumnos_asignatura(asignatura)
                self.__sub_menu_media_alumno_asignatura(alumno, asignatura)
            elif opc == 2:
                self.__sub_menu_media_asignatura(asignatura)
            elif opc == 3:
                self.__sub_menu_rangos_asignatura(asignatura)
            else:
                pass

    def __sub_menu_grados(self, grado):
        """Imprime un menú con diferentes opciones sobre un grado seleccionado y gestiona el paso a la siguiente pantalla
        :param grado: Grado (Grado)
        :return: None
        """
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
                self.__sub_menu_media_grado(grado)
            elif opc == 2:
                self.__sub_menu_rangos_grado(grado)
            elif opc == 3:
                self.__sub_menu_matriculas_y_menciones_grado(grado)
            else:
                pass

    def __sub_menu_alumnos_asignatura(self, asignatura):
        """Imprime un menú con los diferentes alumnos que pertenecen a una asignatura y gestiona el paso a la siguiente
        pantalla, imprime si el usuario no tiene acceso a dicha información
        :param asignatura: Asignatura de la que queremos obtener los alumnos (Asignatura)
        :return: None
        """
        if asignatura is not None:
            self.__clear()
            i = 0
            opc = -1
            mis_alumnos = self.get_alumno_controller().obtenerAlusAsignatura(asignatura.getCodigo(), self.get_sesion())
            if len(mis_alumnos) > 0:
                print " Elija alumno:"
                while i < len(mis_alumnos):
                    print "\t%d) %s, %s" % (i + 1, mis_alumnos[i].getApellidos(), mis_alumnos[i].getNombre())
                    i += 1
                while not (1 <= opc <= len(mis_alumnos)):
                    opc = int(raw_input(" >> "))
                return mis_alumnos[opc - 1]
            else:
                print "Usted no tiene acceso a alumno alguno"
                raw_input(" Presione cualquier tecla... ")
                return None
        else:
            return None

    def __sub_menu_media_alumno_asignatura(self, alumno, asignatura):
        """Muestra la media de un alumno en una asignatura, en caso de que el usuario no tenga acceso a dicha
         información se imprimirá en pantalla
        :param alumno: Alumno del que queremos obtener la media de las notas (Alumno)
        :param asignatura: Asignatura de la que queremos obtener la nota media (Asignatura)
        :return: None
        """
        if alumno is not None:
            self.__clear()
            media = self.get_alumno_controller().obtenerMedia(alumno.getDNI(), asignatura.getCodigo(),
                                                              self.get_sesion())
            if media is not None:
                print " La media de %s %s en la asignatura es %f" % (alumno.getNombre(), alumno.getApellidos(), media)
            else:
                print "Usted no tiene acceso a la media del alumno"
            raw_input(" Presione cualquier tecla... ")

    def __sub_menu_media_alumno_centro(self, alumno):
        """Muestra la nota media de un alumno en el centro, en caso de que el usuario no tenga acceso a dicha
        información se mostrará en pantalla
        :param alumno: Alumno del que queremos obtener la nota media en el centro (Alumno)
        :return: None
        """
        if alumno is not None:
            self.__clear()
            media = self.get_alumno_controller().obtenerMediaCentro(alumno.getDNI(), self.get_sesion())
            if media is not None:
                print " La media global de %s %s en el centro es %f" % (
                    alumno.getNombre(), alumno.getApellidos(), media)
            else:
                print "Usted no tiene acceso a la media global del alumno"
            raw_input(" Presione cualquier tecla... ")

    def __sub_menu_media_grado(self, grado):
        """Muestra la nota media de los alumnos de un grado concreto, en caso de que el usuario no tenga acceso a dicha
        información lo muestra por pantalla
        :param grado: Grado del que queremos obtener la nota media de sus alumnos (Grado)
        :return: None
        """
        if grado is not None:
            self.__clear()
            media = self.get_grado_controller().obtenerMedia(grado.getCodigo(), self.get_sesion())
            if media is not None:
                print " La media del grado de \"%s\" es de %f" % (grado.getNombre(), media)
            else:
                print "Usted no tiene acceso a la media global del grado"
            raw_input(" Presione cualquier tecla... ")

    def __sub_menu_media_asignatura(self, asignatura):
        """Muestra la nota media de los alumnos de una asignatura, en caso de que el usuario no tenga acceso a dicha
        información se mostrará en pantalla
        :param asignatura: Asignatura de la que queremos obtener la nota media de sus alumnos (Asignatura)
        :return: None
        """
        if asignatura is not None:
            self.__clear()
            media = self.get_asignatura_controller().obtenerMedia(asignatura.getCodigo(), self.get_sesion())
            if media is not None:
                print " El promedio de nota de la asignatura de %s es %f" % (asignatura.getNombre(), media)
            else:
                print "Usted no tiene acceso a la media de la asignatura"
            raw_input(" Presione cualquier tecla... ")

    def __sub_menu_rangos_alumno_centro(self, alumno):
        """Muestra los rangos de notas de un alumno del centro, en caso de que el usuario no tenga acceso a dicha
        información se mostrará por pantalla
        :param alumno: Alumno del que se quiere obtener el rango de sus notas (Alumno)
        :return: None
        """
        if alumno is not None:
            self.__clear()
            rango = self.get_alumno_controller().obtenerRango(alumno.getDNI(), self.get_sesion())
            if rango is not None:
                print " Estadisticas del alumno %s %s." % (alumno.getNombre(), alumno.getApellidos())
                print "\tNumero de suspensos totales: %d" % rango.getSuspensos()
                print "\tNumero de aprobados totales: %d" % rango.getAprobados()
                print "\tNumero de notables totales: %d" % rango.getNotables()
                print "\tNumero de sobresalientes totales: %d" % rango.getSobresalientes()
            else:
                print "Usted no tiene acceso a los rangos del alumno"
            raw_input(" Presione cualquier tecla... ")

    def __sub_menu_rangos_asignatura(self, asignatura):
        """Muestra los rangos de notas de una asignatura, en caso de que el usuario no tenga acceso a dicha información
        se mostrará por pantalla
        :param asignatura: Asignatura del que se quiere obtener el rango de notas (Asignatura)
        :return: None
        """
        if asignatura is not None:
            self.__clear()
            rango = self.get_asignatura_controller().obtenerRango(asignatura.getCodigo(), self.get_sesion())
            if rango is not None:
                print " Estadisticas de la asignatura %s." % asignatura.getNombre()
                print "\tNumero de suspensos totales: %d" % rango.getSuspensos()
                print "\tNumero de aprobados totales: %d" % rango.getAprobados()
                print "\tNumero de notables totales: %d" % rango.getNotables()
                print "\tNumero de sobresalientes totales: %d" % rango.getSobresalientes()
            else:
                print "Usted no tiene acceso a los rangos de la asignatura"
            raw_input(" Presione cualquier tecla... ")

    def __sub_menu_rangos_grado(self, grado):
        """Muestra los rangos de notas de un grado, en caso de que el usuario no tenga acceso a dicha información
        se mostrará por pantalla
        :param grado: Grado del que se quiere obtener el rango de notas (Grado)
        :return: None
        """
        if grado is not None:
            self.__clear()
            rango = self.get_grado_controller().obtenerRango(grado.getCodigo(), self.get_sesion())
            if rango is not None:
                print " Estadisticas del grado de \"%s\"." % grado.getNombre()
                print "\tNumero de suspensos totales: %d" % rango.getSuspensos()
                print "\tNumero de aprobados totales: %d" % rango.getAprobados()
                print "\tNumero de notables totales: %d" % rango.getNotables()
                print "\tNumero de sobresalientes totales: %d" % rango.getSobresalientes()
            else:
                print "Usted no tiene acceso a los rangos del grado"
            raw_input(" Presione cualquier tecla... ")

    def __sub_menu_matriculas_y_menciones_grado(self, grado):
        """Muestra el número de matrículas y menciones de un grado, en caso de que el usuario no tenga acceso a dicha
        información se mostrará por pantalla
        :param grado: Grado del que se quiere obtener las matrículas y menciones (Grado)
        :return: None
        """
        if grado is not None:
            self.__clear()
            matriculas_y_menciones = self.get_grado_controller().obtenerMatriculasYMenciones(grado.getCodigo(),
                                                                                             self.get_sesion())
            if matriculas_y_menciones is not None:
                print " Estadisticas del grado de \"%s\"." % grado.getNombre()
                print "\tNumero de menciones totales: %d" % matriculas_y_menciones.getMenciones()
                print "\tNumero de matriculas totales: %d" % matriculas_y_menciones.getMatriculas()
            else:
                print "Usted no tiene acceso a las matriculas y menciones del grado"
            raw_input(" Presione cualquier tecla... ")

    def __sub_menu_resumen_centro(self):
        """Muestra el resumen estadístico del centro
        :return: None
        """
        resumen = self.get_centro_controller().obtenerResumen(self.get_sesion())
        if resumen is not None:
            print "Estado del centro."
            print "------------------"
            print "Nota promedio de alumno     \t%f" % resumen.getNotaPromedioAlumno()
            print "Nota promedio de asignatura \t%f" % resumen.getNotaPromedioAsignatura()
            print

    def __menu_tecnico(self):
        """Imprime el menú de un usuario registrado como técnico y gestiona la siguiente pantalla
        :return: None
        """
        self.__welcome()

        self.__sub_menu_resumen_centro()

        print " Elija opcion:"
        print "\t 1) Gestionar alumnos"
        print "\t 2) Gestionar asignaturas"
        print "\t 3) Gestionar grados"
        print "\t 0) Salir"

        opc = -1

        while not (0 <= opc <= 3):
            opc = int(raw_input(" >> "))

        if opc == 1:
            alumno = self.__menu_alumnos()
            self.__sub_menu_alumnos(alumno)
        elif opc == 2:
            asignatura = self.__menu_asignaturas()
            self.__sub_menu_asignaturas(asignatura)
        elif opc == 3:
            grado = self.__menu_grados()
            self.__sub_menu_grados(grado)
        else:
            exit()

    def __menu_alumnos(self):
        """Imprime la lista de alumnos del centro, en caso de que el usuario no tenga acceso a esta información
        se mostrará por pantalla
        :return: None
        """
        self.__clear()
        i = 0
        opc = -1
        mis_alumnos = self.get_alumno_controller().listar(self.get_sesion())
        if len(mis_alumnos) > 0:
            print " Elija alumno:"
            while i < len(mis_alumnos):
                print "\t%d) %s\t%s, %s" % (
                    i + 1, mis_alumnos[i].getDNI(), mis_alumnos[i].getApellidos(), mis_alumnos[i].getNombre())
                i += 1
            while not (1 <= opc <= len(mis_alumnos)):
                opc = int(raw_input(" >> "))
            return mis_alumnos[opc - 1]
        else:
            print " Usted no tiene acceso a alumno alguno."
            raw_input(" Presione cualquier tecla... ")
            return None

    def __menu_asignaturas(self):
        """Imprime las asignaturas a la que el usuario tiene acceso, en caso de que el usuario no tenga acceso
         a esta ninguna se mostrará por pantalla
        :return: None
        """
        self.__clear()
        i = 0
        opc = -1
        mis_asignaturas = self.get_asignatura_controller().listar(self.get_sesion())
        if len(mis_asignaturas) > 0:
            print " Elija asignatura:"
            while i < len(mis_asignaturas):
                print "\t%d) %s" % (i + 1, mis_asignaturas[i].getNombre())
                i += 1
            while not (1 <= opc <= len(mis_asignaturas)):
                opc = int(raw_input(" >> "))
            return mis_asignaturas[opc - 1]
        else:
            print " Usted no tiene acceso a asignatura alguna."
            raw_input(" Presione cualquier tecla... ")
            return None

    def __menu_grados(self):
        """Imprime los grados a los que tiene acceso, en caso de que el usuario no tenga acceso a ninguno se mostrará
         por pantalla
        :return: None
        """
        self.__clear()
        i = 0
        opc = -1
        mis_grados = self.get_grado_controller().listar(self.get_sesion())
        if len(mis_grados) > 0:
            print " Elija grado:"
            while i < len(mis_grados):
                print "\t%d) %s" % (i + 1, mis_grados[i].getNombre())
                i += 1
            while not (1 <= opc <= len(mis_grados)):
                opc = int(raw_input(" >> "))
            return mis_grados[opc - 1]
        else:
            print " Usted no tiene acceso a grado alguno."
            raw_input(" Presione cualquier tecla... ")
            return None

    def __menu_mis_alumnos(self):
        """Imprime la lista de alumnos a los que tiene acceso el usuario, en caso de no tener acceso a ninguno
        se mostrará por pantalla
        :return: None
        """
        i = 0
        opc = -1
        mis_alumnos = self.get_alumno_controller().listar(self.get_sesion())
        if len(mis_alumnos) > 0:
            print " Elija alumno:"
            while i < len(mis_alumnos):
                print "\t%d) %s, %s" % (i + 1, mis_alumnos[i].getApellidos(), mis_alumnos[i].getNombre())
                i += 1
            while not (1 <= opc <= len(mis_alumnos)):
                opc = int(raw_input(" >> "))
            return mis_alumnos[opc - 1]
        else:
            print "Usted no tiene acceso a alumno alguno"
            raw_input(" Presione cualquier tecla... ")
            return None

    def __menu(self):
        pass