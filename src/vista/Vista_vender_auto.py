from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Dialogo_vender_auto(QDialog):
    #Diálogo para vender un auto

    def __init__(self, auto):
        """
        Constructor del diálogo
        """    
        super().__init__()

        self.auto = auto

        self.setFixedSize(340, 150)
        self.setWindowIcon(
            QIcon("src/recursos/smallLogo.png"))
        self.setWindowTitle("Vender auto")
        self.resultado = ""

        self.widget_dialogo = QListWidget()

        self.distribuidor_dialogo = QGridLayout()
        self.setLayout(self.distribuidor_dialogo)
        numero_fila = 0

        #Creación de las etiquetas
        etiqueta_kilometraje=QLabel("Kilometraje")
        self.distribuidor_dialogo.addWidget(etiqueta_kilometraje,numero_fila,0)

        self.texto_kilometraje=QLineEdit(self)
        self.distribuidor_dialogo.addWidget(self.texto_kilometraje,numero_fila,1,1,3)
        numero_fila=numero_fila+1

        etiqueta_valor=QLabel("Valor")
        self.distribuidor_dialogo.addWidget(etiqueta_valor,numero_fila,0)

        self.texto_valor=QLineEdit(self)
        self.distribuidor_dialogo.addWidget(self.texto_valor,numero_fila,1,1,3)
        numero_fila=numero_fila+1


        numero_fila+=1

        self.btn_volver = QPushButton("Volver")
        self.btn_volver.setIcon(QIcon("src/recursos/007-back-button.png"))
        self.distribuidor_dialogo.addWidget(self.btn_volver, numero_fila, 1,1,1)
        self.btn_volver.clicked.connect(self.cancelar)

        self.btn_generar_reporte = QPushButton("Vender")
        self.btn_generar_reporte.setIcon(QIcon("src/recursos/009-money.png"))
        self.distribuidor_dialogo.addWidget(self.btn_generar_reporte, numero_fila, 0,1,1)
        
        self.btn_generar_reporte.clicked.connect(self.vender)


        #self.distribuidor_dialogo.layout().setRowStretch(numero_fila, 1)

    def vender(self):
        """
        Esta función envía la información de que, al vender un auto, se genera un reporte
        """   
        self.resultado=1
        self.close()
        return self.resultado

    def cancelar(self):
        """
        Esta función envía la información de que se ha cancelado la operación
        """ 
        self.resultado = 0
        self.close()
        return self.resultado
