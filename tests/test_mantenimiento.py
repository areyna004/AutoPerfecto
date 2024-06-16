#Pruebas unitarias para crear mantenimiento
import unittest
from faker import Faker
from src.logica.propietario import Propietario
from src.modelo.mantenimiento import Mantenimiento
from src.modelo.declarative_base import Session, Base, engine

class MantenimientoTestCase(unittest.TestCase):

    def setUp(self):
        self.propietario = Propietario()
        self.data_factory = Faker()
        Faker.seed(1000)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
    
    def test_agregar_mantenimiento_vacio(self):
        resultado = self.propietario.aniadir_mantenimiento(nombre = "", descripcion = "")
        self.assertEqual(resultado,False)

    def test_agregar_mantenimiento_sin_nombre(self):
        resultado = self.propietario.aniadir_mantenimiento(nombre = "",descripcion = self.data_factory.text())
        self.assertEqual(resultado,False)

    def test_agregar_mantenimiento_sin_decripcion(self):
        resultado = self.propietario.aniadir_mantenimiento(nombre= self.data_factory.unique.name(),descripcion = "")
        self.assertEqual(resultado,False)

    def test_agregar_mantenimiento(self):
        resultado = self.propietario.aniadir_mantenimiento(nombre= self.data_factory.unique.name(), descripcion = self.data_factory.text())
        self.assertEqual(resultado,True)
    
    def test_agregar_mantenimiento_repetido(self):
        self.nombre = self.data_factory.unique.name()
        self.descripcion = self.data_factory.text()
        self.mantenimiento = Mantenimiento(nombre= self.nombre, descripcion = self.descripcion)
        self.session = Session()
        self.session.add(self.mantenimiento)
        self.session.commit()
        resultado = self.propietario.aniadir_mantenimiento(nombre= self.nombre, descripcion = self.descripcion)
        self.assertNotEqual(resultado,True)
    
    def test_agregar_mantenimiento_sin_nombre(self):
        self.nombre = self.data_factory.unique.name()
        self.descripcion = self.data_factory.text()
        self.mantenimiento = Mantenimiento(nombre= self.nombre, descripcion = self.descripcion)
        self.session = Session()
        self.session.add(self.mantenimiento)
        self.session.commit()
        resultado = self.propietario.aniadir_mantenimiento(nombre= "", descripcion = self.descripcion)
        self.assertEqual(resultado,False)
    
    def test_agregar_mantenimiento_sin_descripcion(self):
        self.nombre = self.data_factory.unique.name()
        self.descripcion = self.data_factory.text()
        self.mantenimiento = Mantenimiento(nombre= self.nombre, descripcion = self.descripcion)
        self.session = Session()
        self.session.add(self.mantenimiento)
        self.session.commit()
        resultado = self.propietario.aniadir_mantenimiento(nombre= self.nombre, descripcion = "")
        self.assertEqual(resultado,False)

    def test_ver_mantenimientos(self): 
        self.session = Session()
        self.maxDiff = None
        self.mantenimiento1 = Mantenimiento(nombre = self.data_factory.unique.name(), descripcion = self.data_factory.text())
        self.mantenimiento2 = Mantenimiento(nombre = self.data_factory.unique.name(), descripcion = self.data_factory.text())
        self.mantenimiento3 = Mantenimiento(nombre = self.data_factory.unique.name(), descripcion = self.data_factory.text())
        self.session.add(self.mantenimiento1)
        self.session.add(self.mantenimiento2)
        self.session.add(self.mantenimiento3)
        self.session.commit()
        resultado = self.propietario.dar_mantenimientos()
        n = 0
        self.assertEqual(len(resultado),3)
        self.session.close()

    def test_ver_mantenimientos_en_orden(self): 
        self.session = Session()
        self.maxDiff = None
        self.mantenimiento1 = Mantenimiento(nombre = self.data_factory.unique.name(), descripcion = self.data_factory.text())
        self.mantenimiento2 = Mantenimiento(nombre = self.data_factory.unique.name(), descripcion = self.data_factory.text())
        self.mantenimiento3 = Mantenimiento(nombre = self.data_factory.unique.name(), descripcion = self.data_factory.text())
        self.session.add(self.mantenimiento1)
        self.session.add(self.mantenimiento2)
        self.session.add(self.mantenimiento3)
        self.session.commit()
        resultado = self.propietario.dar_mantenimientos()
        n = 0
        for mantenimiento in resultado:
            if n == 0:
                self.assertEqual(mantenimiento.nombre,self.mantenimiento1.nombre)
            if n == 1:
                self.assertEqual(mantenimiento.nombre,self.mantenimiento2.nombre)
            if n == 2:
                self.assertEqual(mantenimiento.nombre,self.mantenimiento3.nombre)
            n = n + 1
        self.session.close()

        def tearDown(self):
            self.session = Session()
        busqueda = self.session.query(Mantenimiento).all()
        for mantenimiento in busqueda:
            self.session.delete(mantenimiento)
        self.session.commit()
        self.session.close()