from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget

from functools import partial

class Vista_reporte_gastos(QWidget):
    #Ventana que muestra el reporte de gastos de un auto

    def __init__(self, interfaz):
        """
        Constructor de la ventana
        """
        super().__init__()

        # Se establecen las características de la ventana
        self.titulo = 'Auto-perfecto - Reporte de gastos'
        self.left = 80
        self.top = 80
        self.width = 400
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

        # Creación de la tabla en dónde se hará el reporte
        self.tabla_reporte = QScrollArea(self)
        self.tabla_reporte.setWidgetResizable(True)
        self.widget_tabla_reporte = QWidget()
        self.distribuidor_tabla_reporte = QGridLayout(self.widget_tabla_reporte)
        self.tabla_reporte.setWidget(self.widget_tabla_reporte)

        self.distribuidor_tabla_reporte.setColumnStretch(0, 1)
        self.distribuidor_tabla_reporte.setColumnStretch(1, 1)


        self.contenedor_tabla = QGroupBox(self)
        self.contenedor_tabla.setLayout(QHBoxLayout())
        self.contenedor_tabla.setTitle('Ganancias')
        self.distribuidor_base.addWidget(self.contenedor_tabla)


        self.contenedor_tabla.layout().addWidget(self.tabla_reporte)
        self.tabla_reporte.setStyleSheet('QScrollArea{border:none}')
        # Creación de las etiquetas con los encabezados
        etiqueta_anio = QLabel("Año")
        etiqueta_anio.setFont(QFont("Times",weight=QFont.Bold)) 
        self.distribuidor_tabla_reporte.addWidget(etiqueta_anio, 0, 0, Qt.AlignCenter|Qt.AlignTop)

        etiqueta_gasto = QLabel("Gastos")
        etiqueta_gasto.setFont(QFont("Times",weight=QFont.Bold)) 
        self.distribuidor_tabla_reporte.addWidget(etiqueta_gasto, 0, 1, Qt.AlignCenter|Qt.AlignTop)

        grupo_anio = QGroupBox()
        grupo_anio.setLayout(QHBoxLayout())

        etiqueta_kilometro = QLabel("Valor del kilómetro:")
        etiqueta_kilometro.setFont(QFont("Times",weight=QFont.Bold)) 
        grupo_anio.layout().addWidget(etiqueta_kilometro)

        self.etiqueta_valor_casa = QLabel("$\t")
        grupo_anio.layout().addWidget(self.etiqueta_valor_casa)

        grupo_anio.setStyleSheet('QGroupBox{border:none}')

        self.distribuidor_base.addWidget(grupo_anio)
        self.distribuidor_base.setAlignment(grupo_anio, Qt.AlignCenter)

        #Creación de los botones de funciones de la ventana
        self.btn_volver = QPushButton("Volver", self)
        self.btn_volver.setFixedSize(200, 40)
        self.btn_volver.setToolTip("Volver")
        self.btn_volver.setIcon(QIcon("src/recursos/007-back-button.png"))
        self.btn_volver.setIconSize(QSize(120, 120))
        self.btn_volver.clicked.connect(self.volver)
        self.distribuidor_base.addWidget(self.btn_volver)
        self.distribuidor_base.setAlignment(self.btn_volver, Qt.AlignCenter)


    def mostrar_gastos(self, lista_gastos, gastos_kilometro):
        """
        Esta función puebla el reporte de ganancias con la información en la lista
        """

        #Por cada iteración, llenamos con el año del gasto y sus valores
        
        numero_fila = 1
        for gasto, valor in lista_gastos:

            etiqueta_anio = QLabel("\t{}".format(gasto))
            etiqueta_anio.setWordWrap(True)
            self.distribuidor_tabla_reporte.addWidget(etiqueta_anio, numero_fila, 0, Qt.AlignLeft)

            etiqueta_total = QLabel("${:,.2f}".format(valor))
            etiqueta_total.setWordWrap(True)
            self.distribuidor_tabla_reporte.addWidget(etiqueta_total, numero_fila, 1, Qt.AlignCenter)

            if numero_fila == len(lista_gastos):
                etiqueta_anio.setFont(QFont("Times",weight=QFont.Bold))
                etiqueta_total.setFont(QFont("Times",weight=QFont.Bold))

            numero_fila = numero_fila+1

        #Añadimos el valor por kilómetro
        self.etiqueta_valor_casa.setText("${:,.2f}".format(gastos_kilometro))
        #Elemento para ajustar la forma de la tabla (y evitar que queden muy espaciados)
        self.distribuidor_tabla_reporte.layout().setRowStretch(numero_fila+1, 1)
        
    def volver(self):
        """
        Esta función permite volver a la ventana de la lista de autos
        """   
        self.hide()
        self.interfaz.mostrar_vista_lista_autos()
