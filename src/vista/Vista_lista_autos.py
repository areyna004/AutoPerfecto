from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from functools import partial


from .Vista_vender_auto import Dialogo_vender_auto


class Vista_lista_autos(QWidget):
    #Ventana que muestra la lista de autos

    def __init__(self, interfaz):
        """
        Constructor de la ventanas
        """
        super().__init__()
        
        self.interfaz=interfaz
       
        #Se establecen las características de la ventana
        self.title = 'Auto-perfecto'
        self.width = 720
        self.height = 600
        self.inicializar_GUI()

    def inicializar_GUI(self):
        
        #inicializamos la ventana
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.setWindowIcon(QIcon("src/recursos/smallLogo.png"))
         
        self.distribuidor_base = QVBoxLayout(self)

        #Creación del logo de encabezado
        self.logo=QLabel(self)
        self.pixmap = QPixmap("src/recursos/smallLogo.png")
        self.pixmap = self.pixmap.scaled(400,150, Qt.KeepAspectRatio)    
        self.logo.setPixmap(self.pixmap)
        self.logo.setAlignment(Qt.AlignCenter)
        self.distribuidor_base.addWidget(self.logo,alignment=Qt.AlignCenter)

        #Creación de las etiquetsa con textos de bienvenida
        self.etiqueta_bienvenida=QLabel("!!Bienvenido a Auto-perfecto!!")                               
        self.etiqueta_bienvenida.setAlignment(Qt.AlignCenter)
        self.distribuidor_base.addWidget(self.etiqueta_bienvenida,Qt.AlignCenter)
        
        self.etiqueta_descripcion=QLabel("Con este software podrás llevar los gastos de tu automóvil")                               
        self.etiqueta_descripcion.setAlignment(Qt.AlignCenter)
        self.distribuidor_base.addWidget(self.etiqueta_descripcion,Qt.AlignCenter)

        #Creación del espacio de los botones
        self.widget_botones=QWidget()
        self.distribuidor_botones=QGridLayout()
        self.widget_botones.setLayout(self.distribuidor_botones)

        #Creación de los botones
        self.btn_aniadir_auto=QPushButton("Crear automóvil",self)
        self.btn_aniadir_auto.setFixedSize(200,40)
        self.btn_aniadir_auto.setToolTip("Crear automóvil")                
        self.btn_aniadir_auto.setIcon(QIcon("src/recursos/006-add.png"))
        self.btn_aniadir_auto.setIconSize(QSize(120,120))
        self.distribuidor_botones.addWidget(self.btn_aniadir_auto,0,0,Qt.AlignLeft)
        self.btn_aniadir_auto.clicked.connect(self.mostrar_ventana_crear_auto)

        self.btn_ver_mantenimientos=QPushButton("Mantenimientos",self)
        self.btn_ver_mantenimientos.setFixedSize(200,40)
        self.btn_ver_mantenimientos.setToolTip("Mantenimientos")                
        self.btn_ver_mantenimientos.setIcon(QIcon("src/recursos/010-people-24.png"))
        self.btn_ver_mantenimientos.setIconSize(QSize(120,120))                
        self.btn_ver_mantenimientos.clicked.connect(self.mostrar_mantenimientos)
        self.distribuidor_botones.addWidget(self.btn_ver_mantenimientos,0,1,Qt.AlignRight)        
        self.distribuidor_base.addWidget(self.widget_botones,Qt.AlignCenter)

        #Creación del área con la información de los autos
        self.tabla_autos = QScrollArea(self)
        self.tabla_autos.setWidgetResizable(True)
        self.tabla_autos.setFixedSize(700, 450)
        self.widget_tabla_autos = QWidget()
        self.distribuidor_tabla_autos = QGridLayout()        
        self.widget_tabla_autos.setLayout(self.distribuidor_tabla_autos);                
        self.tabla_autos.setWidget(self.widget_tabla_autos)
        self.distribuidor_base.addWidget(self.tabla_autos)

        #Hacemos la ventana visible
        self.show()


    def mostrar_autos(self, lista_autos):
        """
        Esta función puebla la tabla con las carreras
        """
        self.autos = lista_autos
        numero_fila=0

        #Este pedazo de código borra todo lo que no sean encabezados.
        while self.distribuidor_tabla_autos.count()>2:
            child = self.distribuidor_tabla_autos.takeAt(2)
            if child.widget():
                child.widget().deleteLater()

        self.distribuidor_tabla_autos.setColumnStretch(0,1)
        self.distribuidor_tabla_autos.setColumnStretch(1,0)
        self.distribuidor_tabla_autos.setColumnStretch(2,0)
        self.distribuidor_tabla_autos.setColumnStretch(3,0)
        self.distribuidor_tabla_autos.setColumnStretch(4,0)
        self.distribuidor_tabla_autos.setColumnStretch(4,0)

        #Ciclo para llenar la tabla
        if (self.autos!= False and len(self.autos)>0) :
            self.tabla_autos.setVisible(True)

            #Creación de las etiquetas

            etiqueta_nombre=QLabel("placa")
            etiqueta_nombre.setMinimumSize(QSize(0,0))
            etiqueta_nombre.setMaximumSize(QSize(65525,65525))
            etiqueta_nombre.setAlignment(Qt.AlignCenter)
            etiqueta_nombre.setFont(QFont("Times",weight=QFont.Bold)) 
            self.distribuidor_tabla_autos.addWidget(etiqueta_nombre, 0,0, Qt.AlignCenter)

            etiqueta_acciones=QLabel("Opciones")                      
            etiqueta_acciones.setMinimumSize(QSize(0,0))
            etiqueta_acciones.setMaximumSize(QSize(65525,65525))
            etiqueta_acciones.setAlignment(Qt.AlignCenter)
            etiqueta_acciones.setFont(QFont("Times",weight=QFont.Bold))               
            self.distribuidor_tabla_autos.addWidget(etiqueta_acciones, 0,1,1,5, Qt.AlignCenter)
       
            for dic_auto in self.autos:
                numero_fila=numero_fila+1

                etiqueta_nombre=QLabel(dic_auto['placa'])
                etiqueta_nombre.setWordWrap(True)
                self.distribuidor_tabla_autos.addWidget(etiqueta_nombre,numero_fila,0)

                #Creación de los botones asociados a cada acción
                btn_ver_actividad=QPushButton("",self)
                btn_ver_actividad.setToolTip("Editar automóvil")
                btn_ver_actividad.setFixedSize(40,40)
                btn_ver_actividad.setIcon(QIcon("src/recursos/004-edit-button.png"))
                btn_ver_actividad.clicked.connect(partial(self.mostrar_auto,numero_fila-1) )
                self.distribuidor_tabla_autos.addWidget(btn_ver_actividad,numero_fila,1,Qt.AlignCenter)

                btn_editar=QPushButton("",self)
                btn_editar.setToolTip("Añadir acciones de mantenimiento")
                btn_editar.setFixedSize(40,40)
                btn_editar.setIcon(QIcon("src/recursos/009-money.png"))
                btn_editar.clicked.connect(partial(self.mostrar_acciones,numero_fila -1 ) )
                self.distribuidor_tabla_autos.addWidget(btn_editar,numero_fila,2,Qt.AlignCenter)

                btn_terminar=QPushButton("",self)
                btn_terminar.setToolTip("Vender")
                btn_terminar.setFixedSize(40,40)
                btn_terminar.setIcon(QIcon("src/recursos/reward.png"))
                btn_terminar.clicked.connect(partial(self.vender_auto,numero_fila-1) )
                self.distribuidor_tabla_autos.addWidget(btn_terminar,numero_fila,3,Qt.AlignCenter)

                btn_eliminar=QPushButton("",self)
                btn_eliminar.setToolTip("Borrar")
                btn_eliminar.setFixedSize(40,40)
                btn_eliminar.setIcon(QIcon("src/recursos/005-delete.png"))
                btn_eliminar.clicked.connect(partial(self.eliminar_auto,numero_fila -1) )
                self.distribuidor_tabla_autos.addWidget(btn_eliminar,numero_fila,4,Qt.AlignCenter)

                if dic_auto['vendido'] == True:
                    btn_ver_actividad.setDisabled(True)
                    btn_editar.setDisabled(True)
                    btn_terminar.setDisabled(True)

        else:
                self.tabla_autos.setVisible(False)

        #Elemento para ajustar la forma de la tabla (y evitar que queden muy espaciados)
        self.distribuidor_tabla_autos.layout().setRowStretch(numero_fila+2, 1)

    def vender_auto(self, id_auto):
        """
        Esta función informa a la interfaz para vender un auto
        """
        
        self.interfaz.auto_actual = id_auto
        dialogo = Dialogo_vender_auto(self.interfaz.dar_auto(id_auto))
        dialogo.exec_()
        if dialogo.resultado == 1:
            if self.interfaz.vender_auto(dialogo.texto_valor.text(), dialogo.texto_kilometraje.text()):
                self.hide()
                self.interfaz.mostrar_reporte_gastos()

    def mostrar_auto(self,id_auto):
        """
        Esta función informa a la interfaz para desplegar la ventana del auto
        """        
        self.hide()
        self.interfaz.mostrar_auto(id_auto)
 
    def mostrar_mantenimientos(self):
        """
        Esta función informa a la interfaz para desplegar la ventana de la lista de mantenimientos
        """
        self.hide()
        self.interfaz.mostrar_mantenimientos()

    def mostrar_acciones(self,id_auto):
        """
        Esta función informa a la interfaz para desplegar la ventana de la lista de acciones
        """        
        self.hide()
        self.interfaz.mostrar_acciones(id_auto)
        
    def mostrar_ventana_crear_auto(self):
        """
        Esta función informa a la interfaz para deplegar la ventana de la información de un auto
        """
        self.hide()
        self.interfaz.mostrar_auto()



    def eliminar_auto(self,indice_auto):
        """
        Esta función elimina un auto tras solicitar una confirmación
        """
        mensaje_confirmacion=QMessageBox()
        mensaje_confirmacion.setIcon(QMessageBox.Question)
        mensaje_confirmacion.setText("¿Esta seguro de que desea borrar esta carrera?\nRecuerde que esta acción es irreversible")        
        mensaje_confirmacion.setWindowTitle("¿Desea borrar esta carrera?")
        mensaje_confirmacion.setWindowIcon(QIcon("src/recursos/smallLogo.png"))
        mensaje_confirmacion.setStandardButtons(QMessageBox.Yes | QMessageBox.No ) 
        respuesta=mensaje_confirmacion.exec_()
        if respuesta == QMessageBox.Yes:
             self.interfaz.eliminar_auto(indice_auto)
    
    def error_vender_auto(self):
            mensaje_error=QMessageBox()
            mensaje_error.setIcon(QMessageBox.Question)
            mensaje_error.setText("Verifique que todos los campos se encuentren diligenciados y que sean valores numéricos.")        
            mensaje_error.setWindowTitle("Error al guardar")
            mensaje_error.setWindowIcon(QIcon("src/recursos/smallLogo.png"))
            mensaje_error.setStandardButtons(QMessageBox.Ok ) 
            respuesta=mensaje_error.exec_()
        
