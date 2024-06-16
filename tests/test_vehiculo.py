#Pruebas unitarias para crear automovil
import unittest
from faker import Faker
from src.logica.propietario import Propietario
from src.modelo.vehiculo import Vehiculo
from src.modelo.declarative_base import Session, Base, engine

class VehiculoCaseTest(unittest.TestCase):

    def setUp(self):
        self.propietario = Propietario()
        self.data_factory = Faker()
        Faker.seed(1000)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
    

    def test_eliminar_auto_inexistente(self):
        resultado = self.propietario.eliminar_auto(160)
        self.assertEqual(resultado,False)

    def test_ver_vehiculos_vacio(self):
        resultado = self.propietario.dar_autos()
        self.assertEqual(resultado,False)

    def test_editar_vehiculo_no_existente(self):
        resultado = self.propietario.editar_auto(id = 132, marca = self.data_factory.unique.name(), placa = self.data_factory.text(), 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipo_combustible = self.data_factory.text())
        self.assertEqual(resultado,False)

    def test_ver_vehiculo_por_Id(self):
        self.vehiculo1 = Vehiculo(marca = self.data_factory.unique.name(), placa = self.data_factory.text(),
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.session = Session()
        self.session.add(self.vehiculo1)
        self.session.commit()
        resultado = self.propietario.dar_auto(0)
        self.assertEqual(resultado.placa,self.vehiculo1.placa)

    def test_ver_vehiculo_por_Id_inexistente(self):
        self.vehiculo1 = Vehiculo(marca = self.data_factory.unique.name(), placa = self.data_factory.text(),
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.session = Session()
        self.session.add(self.vehiculo1)
        self.session.commit()
        resultado = self.propietario.dar_auto(2)
        self.assertEqual(resultado,False)

    def test_agregar_vehiculo(self):
        resultado = self.propietario.crear_auto(marca = self.data_factory.unique.name(), placa = self.data_factory.text(), 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.assertEqual(resultado,True)
    
    def test_agregar_vehiculo_sin_modelo(self):
        resultado = self.propietario.crear_auto(marca = self.data_factory.unique.name(), placa = self.data_factory.text(), 
            modelo = "", kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.assertEqual(resultado,False)

    def test_agregar_vehiculo_sin_marca(self):
        resultado = self.propietario.crear_auto(marca = "", placa = self.data_factory.text(), 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.assertEqual(resultado,False)
    
    def test_agregar_vehiculo_sin_placa(self):
        resultado = self.propietario.crear_auto(marca = self.data_factory.unique.name(), placa = "", 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.assertEqual(resultado,False)
    
    def test_agregar_vehiculo_sin_kilometraje(self):
        resultado = self.propietario.crear_auto(marca = self.data_factory.unique.name(), placa = self.data_factory.text(), 
            modelo = self.data_factory.text(), kilometraje = 0, color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.assertEqual(resultado,False)

    def test_agregar_vehiculo_sin_color(self):
        resultado = self.propietario.crear_auto(marca = self.data_factory.unique.name(), placa = self.data_factory.text(), 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = "", 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.assertEqual(resultado,False)

    def test_agregar_vehiculo_sin_cilindraje(self):
        resultado = self.propietario.crear_auto(marca = self.data_factory.unique.name(), placa = self.data_factory.text(), 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = "", tipoDeCombustible = self.data_factory.text())
        self.assertEqual(resultado,False)

    def test_agregar_vehiculo_sin_tipoDeCombustible(self):
        resultado = self.propietario.crear_auto(marca = self.data_factory.unique.name(), placa = self.data_factory.text(), 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = "")
        self.assertEqual(resultado,False)

    def test_agregar_vehiculo_placa_repetida(self):
        self.marca = self.data_factory.unique.name()
        self.placa = self.data_factory.text()
        self.modelo = self.data_factory.text()
        self.kilometraje = self.data_factory.random_int(0,300000)
        self.color = self.data_factory.text()
        self.cilindraje = self.data_factory.text()
        self.tipoDeCombustible = self.data_factory.text()
        self.vehiculo1 = Vehiculo(marca = self.marca, placa = self.placa, modelo = self.modelo, 
            kilometraje = self.kilometraje, color = self.color, cilindraje = self.cilindraje,
            tipoDeCombustible = self.tipoDeCombustible)
        self.session = Session()
        self.session.add(self.vehiculo1)
        self.session.commit()
        resultado = self.propietario.crear_auto(marca = self.data_factory.unique.name(), placa = self.placa, 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = "")
        self.assertNotEqual(resultado,True)

    def test_agregar_vehiculo_marca_repetida(self):
        self.marca = self.data_factory.unique.name()
        self.placa = self.data_factory.text()
        self.modelo = self.data_factory.text()
        self.kilometraje = self.data_factory.random_int(0,300000)
        self.color = self.data_factory.text()
        self.cilindraje = self.data_factory.text()
        self.tipoDeCombustible = self.data_factory.text()
        self.vehiculo1 = Vehiculo(marca = self.marca, placa = self.placa, modelo = self.modelo, 
            kilometraje = self.kilometraje, color = self.color, cilindraje = self.cilindraje,
            tipoDeCombustible = self.tipoDeCombustible)
        self.session = Session()
        self.session.add(self.vehiculo1)
        self.session.commit()
        resultado = self.propietario.crear_auto(marca = self.marca, placa = self.data_factory.text(), 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = "")
        self.assertNotEqual(resultado,True)

    def test_ver_vehiculos(self): 
        self.session = Session()
        self.maxDiff = None
        self.vehiculo1 = Vehiculo(marca = self.data_factory.unique.name(), placa = self.data_factory.text(), 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.vehiculo2 = Vehiculo(marca = self.data_factory.unique.name(), placa = self.data_factory.text(), 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.vehiculo3 = Vehiculo(marca = self.data_factory.unique.name(), placa = self.data_factory.text(), 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.session.add(self.vehiculo1)
        self.session.add(self.vehiculo2)
        self.session.add(self.vehiculo3)
        self.session.commit()
        resultado = self.propietario.dar_autos()
        n = 0
        self.assertEqual(len(resultado),3)
        self.session.close()

    def test_ver_vehiculos_en_orden(self): 
        self.session = Session()
        self.maxDiff = None
        self.vehiculo1 = Vehiculo(marca = self.data_factory.unique.name(), placa = self.data_factory.text(), 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.vehiculo2 = Vehiculo(marca = self.data_factory.unique.name(), placa = self.data_factory.text(), 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.vehiculo3 = Vehiculo(marca = self.data_factory.unique.name(), placa = self.data_factory.text(), 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.session.add(self.vehiculo1)
        self.session.add(self.vehiculo2)
        self.session.add(self.vehiculo3)
        self.session.commit()
        resultado = self.propietario.dar_autos()
        n = 0
        for vehiculo in resultado:
            if n == 0:
                self.assertEqual(vehiculo.placa,self.vehiculo1.placa)
            if n == 1:
                self.assertEqual(vehiculo.placa,self.vehiculo2.placa)
            if n == 2:
                self.assertEqual(vehiculo.placa,self.vehiculo3.placa)
            n = n + 1
        self.session.close()

    def test_vender_vehiculo_sin_precio(self):
        self.session = Session()
        self.vehiculo1 = Vehiculo(marca = self.data_factory.unique.name(), placa = self.data_factory.text(), 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.session.add(self.vehiculo1)
        self.session.commit()
        resultado = self.propietario.vender_auto(0, self.data_factory.random_int(0,300000), 0)
        self.assertEqual(resultado,False)

    def test_vender_vehiculo_sin_kilometraje(self):
        self.session = Session()
        self.vehiculo1 = Vehiculo(marca = self.data_factory.unique.name(), placa = self.data_factory.text(), 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.session.add(self.vehiculo1)
        self.session.commit()
        resultado = self.propietario.vender_auto(0, 0, self.data_factory.random_int(0,300000))
        self.assertEqual(resultado,False)

    def test_vender_vehiculo(self):
        self.session = Session()
        self.vehiculo1 = Vehiculo(marca = self.data_factory.unique.name(), placa = self.data_factory.text(), 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.session.add(self.vehiculo1)
        self.session.commit()
        resultado = self.propietario.vender_auto(0, self.data_factory.random_int(0,300000), self.data_factory.random_int(0,300000))
        self.assertEqual(resultado,True)
    
    def test_validar_crear_vehiculo(self):
        resultado = self.propietario.validar_crear_editar_auto(id = 1, marca = self.data_factory.unique.name(), placa = self.data_factory.text(), 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.assertEqual(resultado,True)

    def test_editar_vehiculo_sin_placa(self): 
        self.vehiculo1 = Vehiculo(marca = self.data_factory.unique.name(), placa = self.data_factory.text(), 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.session = Session()
        self.session.add(self.vehiculo1)
        self.session.commit()
        resultado = self.propietario.editar_auto(id = 1,  marca = self.data_factory.unique.name(), placa = "", 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipo_combustible = self.data_factory.text())
        self.assertEqual(resultado,False)

    def test_editar_vehiculo_sin_marca(self): 
        self.placa = self.data_factory.text()
        self.vehiculo1 = Vehiculo(marca = self.data_factory.unique.name(), placa = self.placa, 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.session = Session()
        self.session.add(self.vehiculo1)
        self.session.commit()
        resultado = self.propietario.editar_auto(id = 1,  marca = "", placa = self.placa, 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipo_combustible = self.data_factory.text())
        self.assertEqual(resultado,False)

    def test_editar_vehiculo_sin_modelo(self): 
        self.placa = self.data_factory.text()
        self.vehiculo1 = Vehiculo(marca = self.data_factory.unique.name(), placa = self.placa, 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.session = Session()
        self.session.add(self.vehiculo1)
        self.session.commit()
        resultado = self.propietario.editar_auto(id = 1,  marca = self.data_factory.text(), placa = self.placa, 
            modelo = "", kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipo_combustible = self.data_factory.text())
        self.assertEqual(resultado,False)
    
    def test_editar_vehiculo_sin_kilometraje(self): 
        self.placa = self.data_factory.text()
        self.vehiculo1 = Vehiculo(marca = self.data_factory.unique.name(), placa = self.placa, 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.session = Session()
        self.session.add(self.vehiculo1)
        self.session.commit()
        resultado = self.propietario.editar_auto(id = 0,  marca = self.data_factory.text(), placa = self.placa, 
            modelo = self.data_factory.text(), kilometraje = 0, color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipo_combustible = self.data_factory.text())
        self.assertEqual(resultado,False)

    def test_editar_vehiculo_sin_color(self): 
        self.placa = self.data_factory.text()
        self.vehiculo1 = Vehiculo(marca = self.data_factory.unique.name(), placa = self.placa, 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.session = Session()
        self.session.add(self.vehiculo1)
        self.session.commit()
        resultado = self.propietario.editar_auto(id = 0,  marca = self.data_factory.text(), placa = self.placa, 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = "", 
            cilindraje = self.data_factory.text(), tipo_combustible = self.data_factory.text())
        self.assertEqual(resultado,False)

    def test_editar_vehiculo_sin_tipoDeCombustible(self): 
        self.placa = self.data_factory.text()
        self.vehiculo1 = Vehiculo(marca = self.data_factory.unique.name(), placa = self.placa, 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.session = Session()
        self.session.add(self.vehiculo1)
        self.session.commit()
        resultado = self.propietario.editar_auto(id = 0,  marca = self.data_factory.text(), placa = self.placa, 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipo_combustible = "")
        self.assertEqual(resultado,False)

    def test_editar_vehiculo_sin_cilindraje(self): 
        self.placa = self.data_factory.text()
        self.vehiculo1 = Vehiculo(marca = self.data_factory.unique.name(), placa = self.placa, 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.session = Session()
        self.session.add(self.vehiculo1)
        self.session.commit()
        resultado = self.propietario.editar_auto(id = 0,  marca = self.data_factory.text(), placa = self.placa, 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = "", tipo_combustible = self.data_factory.text())
        self.assertEqual(resultado,False)

    def test_editar_vehiculo(self): 
        self.vehiculo1 = Vehiculo(marca = self.data_factory.unique.name(), placa = self.data_factory.text(), 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.session = Session()
        self.session.add(self.vehiculo1)
        self.session.commit()
        resultado = self.propietario.editar_auto(id = 0,  marca = self.data_factory.unique.name(), placa = self.data_factory.text(), 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipo_combustible = self.data_factory.text())
        self.assertEqual(resultado,True)

    def test_editar_vehiculo_placa_igual(self): 
        self.marca = self.data_factory.unique.name()
        self.placa = self.data_factory.text()
        self.modelo = self.data_factory.text()
        self.kilometraje = self.data_factory.random_int(0,300000)
        self.color = self.data_factory.text()
        self.cilindraje = self.data_factory.text()
        self.tipoDeCombustible = self.data_factory.text()
        self.vehiculo1 = Vehiculo(marca = self.marca, placa = self.placa, modelo = self.modelo, 
            kilometraje = self.kilometraje, color = self.color, cilindraje = self.cilindraje,
            tipoDeCombustible = self.tipoDeCombustible)
        self.vehiculo2 = Vehiculo(marca = self.data_factory.unique.name(), placa = self.data_factory.text(), 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.session = Session()
        self.session.add(self.vehiculo1)
        self.session.add(self.vehiculo2)
        self.session.commit()
        self.marca2 = self.data_factory.unique.name()
        resultado = self.propietario.editar_auto(id = 2,  marca = self.data_factory.text(), placa = "", 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipo_combustible = self.data_factory.text())
        self.assertEqual(resultado,False)

    def test_editar_vehiculo_marca_igual(self): 
        self.marca = self.data_factory.unique.name()
        self.placa = self.data_factory.text()
        self.modelo = self.data_factory.text()
        self.kilometraje = self.data_factory.random_int(0,300000)
        self.color = self.data_factory.text()
        self.cilindraje = self.data_factory.text()
        self.tipoDeCombustible = self.data_factory.text()
        self.vehiculo1 = Vehiculo(marca = self.marca, placa = self.placa, modelo = self.modelo, 
            kilometraje = self.kilometraje, color = self.color, cilindraje = self.cilindraje,
            tipoDeCombustible = self.tipoDeCombustible)
        self.vehiculo2 = Vehiculo(marca = self.data_factory.unique.name(), placa = self.data_factory.text(), 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.session = Session()
        self.session.add(self.vehiculo1)
        self.session.add(self.vehiculo2)
        self.session.commit()
        self.marca2 = self.data_factory.unique.name()
        resultado = self.propietario.editar_auto(id = 2,  marca = self.marca, placa = self.data_factory.text(), 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipo_combustible = self.data_factory.text())
        self.assertEqual(resultado,False)

    def test_eliminar_auto(self):
        self.vehiculo1 = Vehiculo(marca = self.data_factory.unique.name(), placa = self.data_factory.text(), 
            modelo = self.data_factory.text(), kilometraje = self.data_factory.random_int(0,300000), color = self.data_factory.text(), 
            cilindraje = self.data_factory.text(), tipoDeCombustible = self.data_factory.text())
        self.session = Session()
        self.session.add(self.vehiculo1)
        self.session.commit()
        resultado = self.propietario.eliminar_auto(0)
        self.assertEqual(resultado,True)

    def tearDown(self):
        self.session = Session()
        busqueda = self.session.query(Vehiculo).all()
        for vehiculo in busqueda:
            self.session.delete(vehiculo)
        self.session.commit()
        self.session.close()