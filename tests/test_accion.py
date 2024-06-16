#Pruebas unitarias para crear accion
import unittest
from faker import Faker
from src.logica.propietario import Propietario
from src.modelo.vehiculo import Vehiculo
from src.modelo.declarative_base import Session, Base, engine
from src.modelo.accion import Accion
from src.modelo.mantenimiento import Mantenimiento
from datetime import date

class AccionTestCase(unittest.TestCase):

    def setUp(self):
        self.propietario = Propietario()
        self.data_factory = Faker()
        Faker.seed(1000)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
    
    def test_ver_acciones_vacio(self):
        resultado = self.propietario.dar_acciones_auto(1)
        self.assertEqual(resultado,False)

    def test_agregar_accion_sin_valor(self):
        self.nombre = self.data_factory.unique.name()
        self.session = Session()
        self.mantenimiento1 = Mantenimiento(nombre = self.nombre, descripcion = self.data_factory.text())
        resultado = self.propietario.crear_accion(mantenimiento = self.mantenimiento1, id_auto = self.data_factory.random_int(0,10), 
            valor = 0, kilometraje = self.data_factory.random_int(0,1000000), fecha = date.today())
        self.assertEqual(resultado,False)

    def test_agregar_accion_sin_kilometraje(self):
        self.nombre = self.data_factory.unique.name()
        self.session = Session()
        self.mantenimiento1 = Mantenimiento(nombre = self.nombre, descripcion = self.data_factory.text())
        resultado = self.propietario.crear_accion(mantenimiento = self.mantenimiento1, id_auto = self.data_factory.random_int(0,10), 
            valor = self.data_factory.random_int(0,1000000), kilometraje = 0, fecha = date.today())
        self.assertEqual(resultado,False)

    def test_agregar_accion(self):
        self.nombre = self.data_factory.unique.name()
        self.session = Session()
        self.mantenimiento1 = Mantenimiento(nombre = self.nombre, descripcion = self.data_factory.text())
        resultado = self.propietario.crear_accion(mantenimiento = self.mantenimiento1, id_auto = self.data_factory.random_int(0,10), 
            valor = self.data_factory.random_int(0,1000000), kilometraje = self.data_factory.random_int(0,1000000),
            fecha = date.today())
        self.assertEqual(resultado,True)

    def test_ver_acciones(self): 
        self.session = Session()
        self.maxDiff = None
        self.vehiculo1 = Vehiculo(marca = self.data_factory.unique.name(), placa = self.data_factory.text(), id = 1,  
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text(), 
            valorVenta = self.data_factory.random_int(0,1000000), kilometrajeVenta = self.data_factory.random_int(0,300000), vendido = False)
        self.mantenimiento1 = Mantenimiento(nombre = self.data_factory.unique.name(), descripcion = self.data_factory.text())
        self.mantenimiento2 = Mantenimiento(nombre = self.data_factory.unique.name(), descripcion = self.data_factory.text())
        self.mantenimiento3 = Mantenimiento(nombre = self.data_factory.unique.name(), descripcion = self.data_factory.text())
        self.accion1 = Accion(mantenimiento = self.mantenimiento1, id_auto = 1, 
            valor = self.data_factory.random_int(0,1000000), kilometraje = self.data_factory.random_int(0,1000000))
        self.accion2 = Accion(mantenimiento = self.mantenimiento2, id_auto = 1, 
            valor = self.data_factory.random_int(0,1000000), kilometraje = self.data_factory.random_int(0,1000000))
        self.accion3 = Accion(mantenimiento = self.mantenimiento3, id_auto = 1, 
            valor = self.data_factory.random_int(0,1000000), kilometraje = self.data_factory.random_int(0,1000000))
        self.session.add(self.vehiculo1)
        self.session.add(self.mantenimiento1)
        self.session.add(self.mantenimiento2)
        self.session.add(self.mantenimiento3)
        self.session.add(self.accion1)
        self.session.add(self.accion2)
        self.session.add(self.accion3)
        self.session.commit()
        resultado = self.propietario.dar_acciones_auto(0)
        n = 0
        for accion in resultado:
            if n == 0:
                self.assertEqual(accion.valor,self.accion1.valor)
            if n == 1:
                self.assertEqual(accion.valor,self.accion2.valor)
            if n == 2:
                self.assertEqual(accion.valor,self.accion3.valor)
            n = n + 1
        self.session.close()

    def test_reporte_sin_auto(self):
        resultado = self.propietario.dar_reporte_ganancias(0)
        self.assertEqual(resultado,False)

    def test_reporte_vehiculo_no_existe(self):
        resultado = self.propietario.dar_reporte_ganancias(1)
        self.assertEqual(resultado,False)
    
    def test_reporte(self):
        self.session = Session()
        self.valor = self.data_factory.random_int(0,1000000)
        self.kilometraje = self.data_factory.random_int(0,1000000)
        self.vehiculo1 = Vehiculo(marca = self.data_factory.unique.name(), placa = self.data_factory.text(),  
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text(), 
            valorVenta = self.data_factory.random_int(0,1000000), kilometrajeVenta = self.data_factory.random_int(0,300000), vendido = False)
        self.mantenimiento1 = Mantenimiento(nombre = self.data_factory.unique.name(), descripcion = self.data_factory.text())
        self.mantenimiento2 = Mantenimiento(nombre = self.data_factory.unique.name(), descripcion = self.data_factory.text())
        self.mantenimiento3 = Mantenimiento(nombre = self.data_factory.unique.name(), descripcion = self.data_factory.text())
        self.accion1 = Accion(mantenimiento = self.mantenimiento1, id_auto = 1, 
            valor = self.valor, kilometraje = self.kilometraje)
        self.accion2 = Accion(mantenimiento = self.mantenimiento2, id_auto = 1, 
            valor = self.valor, kilometraje = self.kilometraje)
        self.accion3 = Accion(mantenimiento = self.mantenimiento3, id_auto = 1, 
            valor = self.valor, kilometraje = self.kilometraje)
        self.session.add(self.vehiculo1)
        self.session.add(self.mantenimiento1)
        self.session.add(self.mantenimiento2)
        self.session.add(self.mantenimiento3)
        self.session.add(self.accion1)
        self.session.add(self.accion2)
        self.session.add(self.accion3)
        self.session.commit()
        resultado = self.propietario.dar_reporte_ganancias(0)
        self.assertNotEqual(resultado,False)
        self.assertNotEqual(resultado,([('Total',0)], 0))

    def test_editar_accion_sin_mantenimiento(self): 
        self.mantenimiento1 = Mantenimiento(nombre = self.data_factory.unique.name(), descripcion = self.data_factory.text())
        self.accion1 = Accion(mantenimiento = self.mantenimiento1, id_auto = 0, 
            valor = self.data_factory.random_int(0,1000000), kilometraje = self.data_factory.random_int(0,1000000))
        self.session = Session()
        self.session.add(self.mantenimiento1)
        self.session.add(self.accion1)
        self.session.commit()
        resultado = self.propietario.editar_accion(id_accion = 0, id_auto = 0, 
            mantenimiento = None, kilometraje = self.data_factory.random_int(0,300000), valor = self.data_factory.random_int(0,1000000), 
            fecha = date.today())
        self.assertEqual(resultado,False)

    def test_editar_accion_sin_valor(self): 
        self.mantenimiento1 = Mantenimiento(nombre = self.data_factory.unique.name(), descripcion = self.data_factory.text())
        self.accion1 = Accion(mantenimiento = self.mantenimiento1, id_auto = 0, 
            valor = self.data_factory.random_int(0,1000000), kilometraje = self.data_factory.random_int(0,1000000))
        self.session = Session()
        self.session.add(self.mantenimiento1)
        self.session.add(self.accion1)
        self.session.commit()
        resultado = self.propietario.editar_accion(id_accion = 0, id_auto = 0, 
            mantenimiento = self.mantenimiento1, kilometraje = self.data_factory.random_int(0,300000), valor = 0, 
            fecha = self.data_factory.text())
        self.assertEqual(resultado,False)

    def test_editar_accion_sin_fecha(self): 
        self.mantenimiento1 = Mantenimiento(nombre = self.data_factory.unique.name(), descripcion = self.data_factory.text())
        self.accion1 = Accion(mantenimiento = self.mantenimiento1, id_auto = 0, 
            valor = self.data_factory.random_int(0,1000000), kilometraje = self.data_factory.random_int(0,1000000))
        self.session = Session()
        self.session.add(self.mantenimiento1)
        self.session.add(self.accion1)
        self.session.commit()
        resultado = self.propietario.editar_accion(id_accion = 0, id_auto = 0, 
            mantenimiento = self.mantenimiento1, kilometraje = self.data_factory.random_int(0,300000), valor = self.data_factory.random_int(0,1000000), 
            fecha = "")
        self.assertEqual(resultado,False)
    
    def test_editar_accion_sin_kilometraje(self): 
        self.mantenimiento1 = Mantenimiento(nombre = self.data_factory.unique.name(), descripcion = self.data_factory.text())
        self.accion1 = Accion(mantenimiento = self.mantenimiento1, id_auto = 0, 
            valor = self.data_factory.random_int(0,1000000), kilometraje = self.data_factory.random_int(0,1000000))
        self.session = Session()
        self.session.add(self.mantenimiento1)
        self.session.add(self.accion1)
        self.session.commit()
        resultado = self.propietario.editar_accion(id_accion = 0, id_auto = 0, 
            mantenimiento = self.mantenimiento1, kilometraje = 0, valor = self.data_factory.random_int(0,1000000), 
            fecha = date.today())
        self.assertEqual(resultado,False)

    
    def test_editar_accion(self): 
        self.mantenimiento1 = Mantenimiento(nombre = self.data_factory.unique.name(), descripcion = self.data_factory.text())
        self.accion1 = Accion(mantenimiento = self.mantenimiento1, id_auto = self.data_factory.random_int(0,10), 
            valor = self.data_factory.random_int(0,1000000), kilometraje = self.data_factory.random_int(0,1000000))
        self.session = Session()
        self.session.add(self.mantenimiento1)
        self.session.add(self.accion1)
        self.session.commit()
        resultado = self.propietario.editar_accion(id_accion = 0, id_auto = 0, 
            mantenimiento = self.mantenimiento1, kilometraje = self.data_factory.random_int(0,300000), valor = self.data_factory.random_int(0,1000000), 
            fecha = "2000-01-01")
        self.assertEqual(resultado,True)
    
    def tearDown(self):
        self.session = Session()
        busqueda = self.session.query(Accion).all()
        for accion in busqueda:
            self.session.delete(accion)
        self.session.commit()
        self.session.close()