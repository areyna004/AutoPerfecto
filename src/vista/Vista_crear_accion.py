from PyQt5 import QtCore
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from functools import partial


class Dialogo_crear_accion(QDialog):
    #Diálogo para crear o editar una accion

    def __init__(self, mantenimientos, accion=None):
        """
        Constructor del diálogo
        """   
        super().__init__()

        
        self.setFixedSize(340, 250)
        self.setWindowIcon(QIcon("src/recursos/smallLogo.png"))

        self.resultado = ""
        self.mantenimientos = mantenimientos

        self.widget_lista = QListWidget()
        

        distribuidor_dialogo = QGridLayout()
        self.setLayout(distribuidor_dialogo)
        numero_fila=0
        
        #Si el diálogo se usa para crear o editar, el título cambia.

        titulo=""
        if(accion==None):
            titulo="Nueva accion"
        else:
            titulo="Editar accion"
      

        self.setWindowTitle(titulo)

        #Creación de las etiquetas y campos de texto

        etiqueta_concepto=QLabel("Mantenimiento")
        distribuidor_dialogo.addWidget(etiqueta_concepto,numero_fila,0)                

        self.combobox_mantenimientos = QComboBox(self)
        for mantenimiento in self.mantenimientos:
            self.combobox_mantenimientos.addItem(mantenimiento.nombre)
        distribuidor_dialogo.addWidget(self.combobox_mantenimientos,numero_fila,1,1,3)
        numero_fila=numero_fila+1


        etiqueta_kilometraje=QLabel("Kilometraje")
        distribuidor_dialogo.addWidget(etiqueta_kilometraje,numero_fila,0)

        self.texto_kilometraje=QLineEdit(self)
        distribuidor_dialogo.addWidget(self.texto_kilometraje,numero_fila,1,1,3)
        numero_fila=numero_fila+1

        etiqueta_valor=QLabel("Valor")
        distribuidor_dialogo.addWidget(etiqueta_valor,numero_fila,0)

        self.texto_valor=QLineEdit(self)
        distribuidor_dialogo.addWidget(self.texto_valor,numero_fila,1,1,3)
        numero_fila=numero_fila+1

        etiqueta_fecha=QLabel("Fecha")
        distribuidor_dialogo.addWidget(etiqueta_fecha,numero_fila,0)

        self.fecha=QDateEdit(self)
        self.fecha.setDisplayFormat("yyyy-MM-dd")
        distribuidor_dialogo.addWidget(self.fecha,numero_fila,1,1,3)
        numero_fila=numero_fila+1
        numero_fila=numero_fila+1

        #Creación de los botones para guardar o cancelar

        self.btn_guardar = QPushButton("Guardar")
        distribuidor_dialogo.addWidget(self.btn_guardar ,numero_fila,1)
        self.btn_guardar.clicked.connect(self.guardar)

        self.btn_cancelar = QPushButton("Cancelar")
        distribuidor_dialogo.addWidget(self.btn_cancelar ,numero_fila,2)
        self.btn_cancelar.clicked.connect(self.cancelar)

        #Si el diálogo se usa para editar, se debe poblar con la información de la acción a editar
        if accion != None:
            self.texto_valor.setText(str(accion.valor))
            indice_mantenimiento = self.combobox_mantenimientos.findText(str(accion.mantenimiento.nombre))
            self.combobox_mantenimientos.setCurrentIndex(indice_mantenimiento)
            self.texto_kilometraje.setText(str(accion.kilometraje))
            self.fecha.setDate(QtCore.QDate.fromString(str(accion.fecha), "yyyy-MM-dd"))

    
    def guardar(self):
        """
        Esta función envía la información de que se han guardado los cambios
        """   
        self.resultado=1
        self.close()
        return self.resultado


    def cancelar(self):
        """
        Esta función envía la información de que se ha cancelado la operación
        """   
        self.resultado=0
        self.close()
        return self.resultado

