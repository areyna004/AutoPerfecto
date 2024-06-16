from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from functools import partial
from PyQt5.QtWidgets import QWidget

from .Vista_crear_accion import Dialogo_crear_accion

class Vista_lista_acciones(QWidget):
    #Ventana que muestra la lista de acciones

    def __init__(self, interfaz):
        """
        Constructor de la ventana
        """
        super().__init__()

        # Se establecen las características de la ventana
        self.titulo = 'Auto-perfecto - Acciones de mantenimiento del auto'
        self.width = 720
        self.height = 560

        self.setAttribute(Qt.WA_DeleteOnClose)

        self.interfaz = interfaz
        self.inicializar_GUI()
        self.show()

    def inicializar_GUI(self):

        # inicializamos la ventana
        self.setWindowTitle(self.titulo)
        self.setFixedSize(self.width, self.height)
        self.setWindowIcon(QIcon("src/recursos/smallLogo.png"))

        self.distribuidor_base = QVBoxLayout(self)

        self.widget_nombre = QWidget()
        self.distribuidor_nombre = QHBoxLayout()
        self.widget_nombre.setLayout(self.distribuidor_nombre)
        self.distribuidor_base.addWidget(self.widget_nombre, Qt.AlignTop)

        self.etiqueta_mantenimiento=QLabel("")
        self.distribuidor_nombre.addWidget(self.etiqueta_mantenimiento)                


        self.contenedor_tabla = QGroupBox(self)
        self.contenedor_tabla.setLayout(QHBoxLayout())
        self.contenedor_tabla.setTitle('Acciones')
        self.distribuidor_base.addWidget(self.contenedor_tabla)

        #Creación de la tabla en donde se mostrarán las acciones 
        self.tabla_actividades = QScrollArea(self)
        self.tabla_actividades.setFixedSize(600, 400)
        self.tabla_actividades.setStyleSheet('''
                QScrollArea{border:none}''')
        self.tabla_actividades.setWidgetResizable(True)
        self.widget_contenidos_tabla_actividades = QWidget()
        self.distribuidor_actividades = QGridLayout(self.widget_contenidos_tabla_actividades)
        self.tabla_actividades.setWidget(self.widget_contenidos_tabla_actividades)
        self.contenedor_tabla.layout().addWidget(self.tabla_actividades, Qt.AlignTop)


        etiqueta_mantenimiento = QLabel("\tMantenimiento")
        etiqueta_mantenimiento.setFont(QFont("Times",weight=QFont.Bold)) 
        self.distribuidor_actividades.addWidget(etiqueta_mantenimiento, 0, 0, Qt.AlignTop)

        etiqueta_accion = QLabel("Kilometraje")
        etiqueta_accion.setFont(QFont("Times",weight=QFont.Bold)) 
        self.distribuidor_actividades.addWidget(etiqueta_accion, 0, 1, alignment=Qt.AlignCenter|Qt.AlignTop)

        etiqueta_valor = QLabel("Valor")
        etiqueta_valor.setFont(QFont("Times",weight=QFont.Bold)) 
        self.distribuidor_actividades.addWidget(etiqueta_valor, 0, 2, Qt.AlignCenter|Qt.AlignTop)

        etiqueta_fecha = QLabel("Fecha")
        etiqueta_fecha.setFont(QFont("Times",weight=QFont.Bold)) 
        self.distribuidor_actividades.addWidget(etiqueta_fecha, 0, 3, Qt.AlignCenter|Qt.AlignTop)

        etiqueta_accion = QLabel("Acciones")
        etiqueta_accion.setFont(QFont("Times",weight=QFont.Bold)) 
        self.distribuidor_actividades.addWidget(etiqueta_accion, 0, 4, 0, 2, alignment=Qt.AlignCenter|Qt.AlignTop)


        #Creación de la caja con los botones
        self.widget_botones = QWidget()
        self.distribuidor_botones = QGridLayout()
        self.widget_botones.setLayout(self.distribuidor_botones)
        self.distribuidor_base.addWidget(self.widget_botones, Qt.AlignTop)

       #Creación de los botones con las diferentes operaciones
        self.btn_volver = QPushButton("Volver", self)
        self.btn_volver.setFixedSize(200, 40)
        self.btn_volver.setToolTip("Añadir Actividad")
        self.btn_volver.setIcon(QIcon("src/recursos/007-back-button.png"))
        self.distribuidor_botones.addWidget(self.btn_volver, 0, 0, Qt.AlignCenter)
        self.btn_volver.clicked.connect(self.volver)

        self.btn_aniadir_accion = QPushButton("Añadir accion", self)
        self.btn_aniadir_accion.setFixedSize(200, 40)
        self.btn_aniadir_accion.setToolTip("Añadir acción")
        self.btn_aniadir_accion.setIcon(QIcon("src/recursos/009-money.png"))
        self.distribuidor_botones.addWidget(self.btn_aniadir_accion, 0, 1, Qt.AlignCenter)
        self.btn_aniadir_accion.clicked.connect(self.aniadir_accion)

        self.btn_reporte_gastos = QPushButton("Reporte gastos", self)
        self.btn_reporte_gastos.setFixedSize(200, 40)
        self.btn_reporte_gastos.setToolTip("Reporte gastos")
        self.btn_reporte_gastos.setIcon(QIcon("src/recursos/008-data-spreadsheet.png"))
        self.distribuidor_botones.addWidget(self.btn_reporte_gastos, 0, 2, Qt.AlignCenter)
        self.btn_reporte_gastos.clicked.connect(self.mostrar_reporte_gastos)

    def mostrar_acciones(self, etiqueta_auto,  acciones):
        """
        Esta función construye el reporte a partir de una matriz
        """        
        self.etiqueta_mantenimiento.setText('acciones para {}'.format(etiqueta_auto))
        self.acciones = acciones

        #Este pedazo de código borra todos los contenidos anteriores de la tabla (salvo los encabezados)
        while self.distribuidor_actividades.count()>4:
            child = self.distribuidor_actividades.takeAt(4)
            if child.widget():
                child.widget().deleteLater()

        numero_fila=1

        if self.acciones != False and self.acciones != None:

            for accion in self.acciones:

                etiqueta_mantenimiento = QLabel(accion.mantenimiento.nombre)
                etiqueta_mantenimiento.setWordWrap(True)
                self.distribuidor_actividades.addWidget(etiqueta_mantenimiento, numero_fila, 0, alignment=Qt.AlignTop)

                etiqueta_kilometraje = QLabel(str(accion.kilometraje))
                etiqueta_kilometraje.setWordWrap(True)
                self.distribuidor_actividades.addWidget(etiqueta_kilometraje, numero_fila, 1, alignment=Qt.AlignTop|Qt.AlignCenter)

                etiqueta_valor = QLabel("{:,.3f}".format(float(accion.valor)))
                etiqueta_valor.setWordWrap(True)
                self.distribuidor_actividades.addWidget(etiqueta_valor, numero_fila, 2, alignment=Qt.AlignTop|Qt.AlignCenter)
                
                etiqueta_fecha = QLabel(str(accion.fecha))
                etiqueta_fecha.setWordWrap(True)
                self.distribuidor_actividades.addWidget(etiqueta_fecha, numero_fila, 3, alignment=Qt.AlignTop|Qt.AlignCenter)
                


                btn_editar = QPushButton("", self)
                btn_editar.setToolTip("Editar")
                btn_editar.setGeometry(0, 0, 35, 35)
                btn_editar.setFixedSize(35, 35)
                btn_editar.setIcon(QIcon("src/recursos/004-edit-button.png"))
                btn_editar.setIconSize(QSize(35, 35))
                btn_editar.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                btn_editar.clicked.connect(partial(self.editar_accion, numero_fila-1))
                self.distribuidor_actividades.addWidget(btn_editar, numero_fila, 4, alignment=Qt.AlignTop)

                btn_eliminar = QPushButton("", self)
                btn_eliminar.setToolTip("Eliminar")
                btn_eliminar.setGeometry(0, 0, 35, 35)
                btn_eliminar.setFixedSize(35, 35)
                btn_eliminar.setIcon(QIcon("src/recursos/005-delete.png"))
                btn_eliminar.setIconSize(QSize(35, 35))
                btn_eliminar.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                btn_eliminar.clicked.connect(partial(self.eliminar_accion, numero_fila-1))
                self.distribuidor_actividades.addWidget(btn_eliminar, numero_fila, 5, alignment=Qt.AlignTop)

                numero_fila+=1

        height = 360
        elemento_de_espacio = QSpacerItem(140, height-numero_fila*40 if numero_fila*40<=height else 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.distribuidor_actividades.addItem(elemento_de_espacio, numero_fila, 0, 1, 3)


    def volver(self):
        """
        Esta función permite volver a la ventana de la lista de autos
        """   
        self.hide()
        self.interfaz.mostrar_vista_lista_autos()

    def aniadir_accion(self):
        """
        Esta función permite ejecutar el diálogo para crear una accion
        """   
        dialogo = Dialogo_crear_accion(self.interfaz.dar_mantenimientos())
        dialogo.exec_()
        if dialogo.resultado == 1:
            self.interfaz.aniadir_accion(str(dialogo.combobox_mantenimientos.currentText()), dialogo.texto_valor.text(), dialogo.texto_kilometraje.text(), dialogo.fecha.text())
            
    def editar_accion(self, id_accion):
        """
        Esta función permite ejecutar el diálogo para editar una accion
        """ 
        dialogo = Dialogo_crear_accion(self.interfaz.dar_mantenimientos(), self.interfaz.dar_accion(id_accion))
        dialogo.exec_()
        if dialogo.resultado == 1:
            self.interfaz.editar_accion(id_accion, str(dialogo.combobox_mantenimientos.currentText()), dialogo.texto_valor.text(), dialogo.texto_kilometraje.text(), dialogo.fecha.text())
            
   
    def eliminar_accion(self, id_accion):
        """
        Esta función permite eliminar una accion
        """ 
        mensaje_confirmacion=QMessageBox()
        mensaje_confirmacion.setIcon(QMessageBox.Question)
        mensaje_confirmacion.setText("¿Esta seguro de que desea eliminar esta accion?\nRecuerde que esta acción es irreversible")        
        mensaje_confirmacion.setWindowTitle("¿Desea eliminar esta accion?")
        mensaje_confirmacion.setWindowIcon(QIcon("src/recursos/smallLogo.png"))
        mensaje_confirmacion.setStandardButtons(QMessageBox.Yes | QMessageBox.No ) 
        respuesta=mensaje_confirmacion.exec_()
        if respuesta == QMessageBox.Yes:
             self.interfaz.eliminar_accion(id_accion)

    def mostrar_reporte_gastos(self):
        """
        Esta función reenvía al reporte de gastos
        """
        self.interfaz.mostrar_reporte_gastos()
        self.close()

    def error_crear_editar_accion(self):
            mensaje_error=QMessageBox()
            mensaje_error.setIcon(QMessageBox.Question)
            mensaje_error.setText("Verifique que todos los campos se encuentren diligenciados y que Kilometraje y Valor sean valores numéricos.")        
            mensaje_error.setWindowTitle("Error al guardar")
            mensaje_error.setWindowIcon(QIcon("src/recursos/smallLogo.png"))
            mensaje_error.setStandardButtons(QMessageBox.Ok ) 
            respuesta=mensaje_error.exec_()
