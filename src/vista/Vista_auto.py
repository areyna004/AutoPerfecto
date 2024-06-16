from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from functools import partial

class Vista_auto(QWidget):
    #Ventana del auto

    def __init__(self,principal):
        """
        Constructor de la ventana
        """   
        super().__init__()

        self.titulo = ''
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.interfaz=principal

        self.width = 400
        self.height = 300
        self.inicializar_GUI()
        self.show()
       

    def inicializar_GUI(self):

        # inicializamos la ventana
        self.setWindowTitle(self.titulo)
        self.setFixedSize(self.width, self.height)
        self.setWindowIcon(QIcon("src/recursos/smallLogo.png"))

        self.distribuidor_base = QVBoxLayout(self)

        self.widget_auto = QWidget()
        self.distribuidor_auto = QGridLayout()
        self.widget_auto.setLayout(self.distribuidor_auto)
        self.distribuidor_base.addWidget(self.widget_auto, Qt.AlignTop)
        numero_fila = 0

        etiqueta_marca=QLabel("Marca")
        self.distribuidor_auto.addWidget(etiqueta_marca, numero_fila, 0)

        self.texto_marca=QLineEdit(self)
        self.distribuidor_auto.addWidget(self.texto_marca, numero_fila, 1)
        numero_fila=numero_fila+1

        etiqueta_placa=QLabel("Placa")
        self.distribuidor_auto.addWidget(etiqueta_placa, numero_fila, 0)

        self.texto_placa=QLineEdit(self)
        self.distribuidor_auto.addWidget(self.texto_placa, numero_fila, 1)
        numero_fila=numero_fila+1 

        etiqueta_modelo=QLabel("Modelo")
        self.distribuidor_auto.addWidget(etiqueta_modelo, numero_fila, 0)

        self.texto_modelo=QLineEdit(self)
        self.distribuidor_auto.addWidget(self.texto_modelo, numero_fila, 1)
        numero_fila=numero_fila+1

        etiqueta_kilometraje=QLabel("Kilometraje")
        self.distribuidor_auto.addWidget(etiqueta_kilometraje, numero_fila, 0)

        self.texto_kilometraje=QLineEdit(self)
        self.distribuidor_auto.addWidget(self.texto_kilometraje, numero_fila, 1)
        numero_fila=numero_fila+1

        etiqueta_color=QLabel("Color")
        self.distribuidor_auto.addWidget(etiqueta_color, numero_fila, 0)

        self.texto_color=QLineEdit(self)
        self.distribuidor_auto.addWidget(self.texto_color, numero_fila, 1)
        numero_fila=numero_fila+1

        etiqueta_cilindraje=QLabel("Cilindraje")
        self.distribuidor_auto.addWidget(etiqueta_cilindraje, numero_fila, 0)

        self.texto_cilindraje=QLineEdit(self)
        self.distribuidor_auto.addWidget(self.texto_cilindraje, numero_fila, 1)
        numero_fila=numero_fila+1

        etiqueta_tipo_combustible=QLabel("Tipo de combustible")
        self.distribuidor_auto.addWidget(etiqueta_tipo_combustible, numero_fila, 0)

        self.texto_tipo_combustible=QLineEdit(self)
        self.distribuidor_auto.addWidget(self.texto_tipo_combustible, numero_fila, 1)
        numero_fila=numero_fila+1

        #Creación de la caja con los botones
        self.widget_botones = QWidget()
        self.distribuidor_botones = QGridLayout()
        self.widget_botones.setLayout(self.distribuidor_botones)
        self.distribuidor_base.addWidget(self.widget_botones, Qt.AlignTop)

       #Creación de los botones con las diferentes operaciones
        self.btn_volver = QPushButton("Volver", self)
        self.btn_volver.setFixedSize(120, 40)
        self.btn_volver.setToolTip("Volver")
        self.btn_volver.setIcon(QIcon("src/recursos/007-back-button.png"))
        self.distribuidor_botones.addWidget(self.btn_volver, 0, 0, Qt.AlignCenter)
        self.btn_volver.clicked.connect(self.volver)

        self.btn_guardar_auto = QPushButton("Guardar auto", self)
        self.btn_guardar_auto.setFixedSize(120, 40)
        self.btn_guardar_auto.setToolTip("Guardar auto")
        self.btn_guardar_auto.setIcon(QIcon("src/recursos/floppy-disk.png"))
        self.distribuidor_botones.addWidget(self.btn_guardar_auto, 0, 2, Qt.AlignCenter)
        self.btn_guardar_auto.clicked.connect(self.guardar_cambios)

    def mostrar_auto(self, auto):
        self.auto=auto
        if (self.auto!=None and self.auto!=False):
            self.texto_marca.setText(self.auto.marca)
            self.texto_placa.setText(self.auto.placa)
            self.texto_modelo.setText(self.auto.modelo)
            self.texto_kilometraje.setText(str(self.auto.kilometraje))
            self.texto_color.setText(self.auto.color)
            self.texto_cilindraje.setText(str(self.auto.cilindraje))
            self.texto_tipo_combustible.setText(self.auto.tipoDeCombustible)

    def volver(self):
        """
        Esta función permite volver a la lista de autos
        """    
        self.hide()
        self.interfaz.mostrar_vista_lista_autos()

    def guardar_cambios(self):
        """
        Esta función guarda los cambios al auto (editando o guardando los nuevos autos)
        """    
        if self.interfaz.guardar_auto(self.texto_marca.text(), self.texto_placa.text(), self.texto_modelo.text(), self.texto_kilometraje.text(), \
        self.texto_color.text(), self.texto_cilindraje.text(), self.texto_tipo_combustible.text()) != False:
            self.hide()
            self.interfaz.mostrar_vista_lista_autos()
        else:
            self.error_auto()
    
    def error_auto(self):
        mensaje_error=QMessageBox()
        mensaje_error.setIcon(QMessageBox.Question)
        mensaje_error.setText("Verifique que todos los campos se encuentren diligenciados y que el kilometraje sea un valor numérico.")        
        mensaje_error.setWindowTitle("Error al guardar")
        mensaje_error.setWindowIcon(QIcon("src/recursos/smallLogo.png"))
        mensaje_error.setStandardButtons(QMessageBox.Ok ) 
        respuesta=mensaje_error.exec_()
