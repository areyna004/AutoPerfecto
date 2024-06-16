from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *

from functools import partial
from .Vista_crear_mantenimiento import Dialogo_crear_mantenimiento

class Vista_lista_mantenimientos(QWidget):
    #Ventana que muestra la lista de mantenimientos

    def __init__(self, interfaz):
        """
        Constructor de la ventana
        """
        super().__init__()

        #Se establecen las características de la ventana
        self.titulo = 'Auto-perfecto mantenimientos'
        self.interfaz=interfaz

        self.width = 400
        self.height = 400
        self.inicializar_GUI()
        self.show()


    def inicializar_GUI(self):

        # inicializamos la ventana
        self.setWindowTitle(self.titulo)
        self.setFixedSize(self.width, self.height)
        self.setWindowIcon(QIcon("src/recursos/smallLogo.png"))
         
        self.distribuidor_base = QVBoxLayout(self)        



        #Creación del grupo de botones
        caja_botones = QGroupBox()
        caja_botones.setLayout(QHBoxLayout())

        #Creación de los botones
        self.btn_volver = QPushButton("Volver", self)
        self.btn_volver.setFixedSize(150, 40)
        self.btn_volver.setToolTip("Volver")
        self.btn_volver.setIcon(QIcon("src/recursos/007-back-button.png"))
        self.btn_volver.clicked.connect(self.volver)

        self.btn_aniadir_mantenimiento=QPushButton("Añadir mantenimiento",self)
        self.btn_aniadir_mantenimiento.setFixedSize(150,40)
        self.btn_aniadir_mantenimiento.setToolTip("Añadir mantenimiento")
        self.btn_aniadir_mantenimiento.setIcon(QIcon("src/recursos/006-add.png"))
        self.btn_aniadir_mantenimiento.clicked.connect(self.mostrar_dialogo_aniadir_mantenimiento)

        self.contenedor_tabla = QGroupBox(self)
        self.contenedor_tabla.setLayout(QHBoxLayout())
        self.contenedor_tabla.setTitle('Mantenimientos')
        self.distribuidor_base.addWidget(self.contenedor_tabla)

        #Creación de la tabla con la lista de mantenimientos
        self.tabla_mantenimientos = QScrollArea(self)
        self.tabla_mantenimientos.setWidgetResizable(True)
        self.tabla_mantenimientos.setStyleSheet('QScrollArea{border:none}')
        self.tabla_mantenimientos.setFixedSize(300, 300)
        self.widget_tabla_viajeros = QWidget()
        self.distribuidor_tabla_mantenimientos = QGridLayout(self.widget_tabla_viajeros)
        self.tabla_mantenimientos.setWidget(self.widget_tabla_viajeros)
        self.contenedor_tabla.layout().addWidget(self.tabla_mantenimientos)

        self.distribuidor_tabla_mantenimientos.setColumnStretch(0, 0)
        self.distribuidor_tabla_mantenimientos.setColumnStretch(1, 0)
        self.distribuidor_tabla_mantenimientos.setColumnStretch(2, 0)

        self.distribuidor_tabla_mantenimientos.setSpacing(0)

        #Creación de las etiquetas de encabezado
        etiqueta_nombre = QLabel("Nombre")
        etiqueta_nombre.setFixedSize(145,40)
        etiqueta_nombre.setFont(QFont("Times",weight=QFont.Bold)) 
        self.distribuidor_tabla_mantenimientos.addWidget(etiqueta_nombre, 0, 0, Qt.AlignTop)

        etiqueta_accion = QLabel("Accion")
        etiqueta_accion.setFixedSize(60,40)
        etiqueta_accion.setFont(QFont("Times",weight=QFont.Bold)) 
        etiqueta_accion.setAlignment(Qt.AlignCenter)
        self.distribuidor_tabla_mantenimientos.addWidget(etiqueta_accion, 0, 1, 0, 2, Qt.AlignTop|Qt.AlignCenter)
        

        #Se añaden los botones a la caja de botones
        caja_botones.layout().addWidget(self.btn_volver)
        caja_botones.layout().addWidget(self.btn_aniadir_mantenimiento)
        caja_botones.layout().setContentsMargins(0, 0, 0, 0)
        caja_botones.setObjectName("MyBox")
        caja_botones.setStyleSheet("#MyBox{border:3px}")
        self.distribuidor_base.addWidget(caja_botones)



       
    def mostrar_mantenimientos(self, mantenimientos):
        """
        Esta función muestra la lista de mantenimientos
        """
        self.mantenimientos = mantenimientos
        
        #Este pedazo de código borra todos los contenidos anteriores de la tabla (salvo los encabezados)
        while self.distribuidor_tabla_mantenimientos.count()>2:
            child = self.distribuidor_tabla_mantenimientos.takeAt(2)
            if child.widget():
                child.widget().deleteLater()

        numero_fila = 0

        #Ciclo para poblar la tabla
        if self.mantenimientos != False and self.mantenimientos != None:
            
            for mantenimiento in self.mantenimientos:

                etiqueta_nombre=QLabel(mantenimiento.nombre)          
                etiqueta_nombre.setWordWrap(True)
                etiqueta_nombre.setFixedSize(90,40)
                self.distribuidor_tabla_mantenimientos.addWidget(etiqueta_nombre, numero_fila+1,0, Qt.AlignTop)

                boton_editar=QPushButton("",self)
                boton_editar.setToolTip("Editar")
                boton_editar.setFixedSize(30,30)
                boton_editar.setIcon(QIcon("src/recursos/004-edit-button.png"))
                boton_editar.clicked.connect(partial(self.mostrar_dialogo_editar_mantenimiento, numero_fila) )
                self.distribuidor_tabla_mantenimientos.addWidget(boton_editar, numero_fila+1,1,Qt.AlignTop)


                etiqueta_eliminar=QPushButton("",self)
                etiqueta_eliminar.setToolTip("Borrar")
                etiqueta_eliminar.setFixedSize(30,30)
                etiqueta_eliminar.setIcon(QIcon("src/recursos/005-delete.png"))
                etiqueta_eliminar.clicked.connect(partial(self.eliminar_mantenimiento, numero_fila) )
                self.distribuidor_tabla_mantenimientos.addWidget(etiqueta_eliminar, numero_fila+1,2,Qt.AlignTop)


                numero_fila=numero_fila+1

        #Elemento para ajustar la forma de la tabla (y evitar que queden muy espaciados)
        self.distribuidor_tabla_mantenimientos.layout().setRowStretch(numero_fila+1, 1)

    def mostrar_dialogo_editar_mantenimiento(self, id_mantenimiento):
        """
        Esta función ejecuta el diálogo para editar un mantenimiento
        """    
        dialogo=Dialogo_crear_mantenimiento(self.mantenimientos[id_mantenimiento])        
        dialogo.exec_()
        if dialogo.resultado==1:            
            self.interfaz.editar_mantenimiento(id_mantenimiento, dialogo.texto_nombre.text(), dialogo.texto_descripcion.text())

    def eliminar_mantenimiento(self, indice_mantenimiento):
        """
        Esta función informa a la interfaz del mantenimiento a eliminar
        """    
        mensaje_confirmacion=QMessageBox()
        mensaje_confirmacion.setIcon(QMessageBox.Question)
        mensaje_confirmacion.setText("¿Esta seguro de que desea eliminar este mantenimiento?\nRecuerde que esta acción es irreversible")        
        mensaje_confirmacion.setWindowTitle("¿Desea borrar este mantenimiento?")
        mensaje_confirmacion.setWindowIcon(QIcon("src/recursos/smallLogo.png"))
        mensaje_confirmacion.setStandardButtons(QMessageBox.Yes | QMessageBox.No ) 
        respuesta=mensaje_confirmacion.exec_()
        if respuesta == QMessageBox.Yes:
            self.interfaz.eliminar_mantenimiento(indice_mantenimiento)          

    def mostrar_dialogo_aniadir_mantenimiento(self):
        """
        Esta función ejecuta el diálogo para crear un nuevo mantenimiento
        """
        dialogo=Dialogo_crear_mantenimiento(None)
        dialogo.exec_()
        if dialogo.resultado==1:
            self.interfaz.aniadir_mantenimiento(dialogo.texto_nombre.text(), dialogo.texto_descripcion.text())

    def volver(self):
        """
        Esta función permite volver a la ventana de lista de autos
        """    
        self.interfaz.mostrar_vista_lista_autos()
        self.close()

    def error_mantenimiento(self):
            mensaje_error=QMessageBox()
            mensaje_error.setIcon(QMessageBox.Question)
            mensaje_error.setText("Verifique que todos los campos se encuentren diligenciados.")        
            mensaje_error.setWindowTitle("Error al guardar")
            mensaje_error.setWindowIcon(QIcon("src/recursos/smallLogo.png"))
            mensaje_error.setStandardButtons(QMessageBox.Ok ) 
            respuesta=mensaje_error.exec_()
    