from datetime import datetime
from setuptools import sic

from sqlalchemy import Float, Integer
from src.modelo.declarative_base import engine, Base, Session
from src.modelo.vehiculo import Vehiculo
from src.modelo.mantenimiento import Mantenimiento
from src.modelo.accion import Accion

class Propietario():

    def __init__(self):
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
    
    def dar_autos(self):
        session = Session()
        vehiculos = session.query(Vehiculo).all()
        session.close()
        if len(vehiculos) == 0:
            return False
        else: 
            return vehiculos

    def dar_auto(self, id):
        session = Session()
        vehiculos = session.query(Vehiculo).filter(Vehiculo.id == id+1).all()
        session.close()
        if len(vehiculos) != 0:
            for vehiculo in vehiculos:
                return vehiculo
        else:
            return False

    def crear_auto(self, marca, placa, modelo, kilometraje, color, cilindraje, tipoDeCombustible):
        session = Session()
        busqueda = session.query(Vehiculo).filter(Vehiculo.placa == placa).all()
        busqueda2 = session.query(Vehiculo).filter(Vehiculo.marca == marca).all()
        if len(busqueda) == 0 and len(busqueda2) == 0 and len(placa) != 0 and len(marca) != 0 and len(modelo) != 0 and kilometraje != 0 and len(color) != 0 and len(cilindraje) != 0 and len(tipoDeCombustible) != 0 :
            vehiculo = Vehiculo(placa = placa, marca = marca, color = color, modelo = modelo, cilindraje = cilindraje, 
                kilometraje =  kilometraje, tipoDeCombustible = tipoDeCombustible)
            session.add(vehiculo)
            session.commit()
            session.close()
            return True
        else:
            session.close()
            return False

    def editar_auto(self, id, marca, placa, modelo, kilometraje, color, cilindraje, tipo_combustible):
        session = Session()
        vehiculos = session.query(Vehiculo).filter(Vehiculo.id == id+1).all()
        busqueda_placa = session.query(Vehiculo).filter(Vehiculo.placa == placa).all()
        busqueda_marca = session.query(Vehiculo).filter(Vehiculo.marca == marca).all()
        if len(vehiculos) != 0 and len(busqueda_placa) <= 1 and len(busqueda_marca) <= 1 and len(placa) != 0 and len(marca) != 0 and len(modelo) != 0 and kilometraje != 0 and len(color) != 0 and len(cilindraje) != 0 and len(tipo_combustible) != 0:
            for vehiculo in vehiculos:
                vehiculo.marca = marca
                vehiculo.placa = placa
                vehiculo.modelo = modelo 
                vehiculo.kilometraje = kilometraje
                vehiculo.color = color
                vehiculo.cilindraje = cilindraje
                vehiculo.tipo_combustible = tipo_combustible
                session.commit()
                session.close()
            return True
        else:
            return False

    def vender_auto(self, id, kilometraje_venta, valor_venta):
        if valor_venta >= 0 and kilometraje_venta >= 0:
            session = Session()
            busqueda = session.query(Vehiculo).filter(Vehiculo.id == id+1).all()
            if len(busqueda) >> 0 and kilometraje_venta != 0 and valor_venta != 0:
                for vehiculo in busqueda:
                    vehiculo.vendido = True
                    vehiculo.kilometraje_venta = kilometraje_venta
                    vehiculo.valor_venta = valor_venta
                    session.commit()
                    session.close()
                return True
            else:
                return False
        else:
            return False

    def eliminar_auto(self, id):
        session = Session()
        vehiculos = session.query(Vehiculo).filter(Vehiculo.id == id+1).all()
        if len(vehiculos) != 0:
            for vehiculo in vehiculos:
                session.delete(vehiculo)
                session.commit()
                session.close()
                return True
        else:
            return False

    def validar_crear_editar_auto(self, id, marca, placa, modelo, kilometraje, color, cilindraje, tipoDeCombustible):
        if kilometraje != 0:
            return True
        else:
            return False

    def validar_vender_auto(self, id, kilometraje_venta, valor_venta):
        validacion = False
        try:
            float(kilometraje_venta)
            float(valor_venta)
            validacion = True
        except ValueError:
            validacion = False
        return validacion

    def dar_mantenimientos(self):
            session = Session()
            mantenimientos = session.query(Mantenimiento).all()
            session.close()
            if len(mantenimientos) != 0 :
                return mantenimientos
            else:
                return False
    


    def aniadir_mantenimiento(self, nombre, descripcion):
        session = Session()
        busqueda = session.query(Mantenimiento).filter(Mantenimiento.nombre == nombre).all()
        if len(busqueda) == 0 and len(nombre) != 0 and len(descripcion) != 0:
            mantenimiento = Mantenimiento(nombre = nombre, descripcion = descripcion)
            session.add(mantenimiento)
            session.commit()
            session.close()
            return True
        else:
            session.close()
            return False

    def editar_mantenimiento(self, id, nombre, descripcion):
        session = Session()
        mantenimientos = session.query(Mantenimiento).filter(Mantenimiento.id == id+1).all()
        if len(mantenimientos) != 0 and len(nombre) != 0 and len(descripcion) != 0:
            for mantenimiento in mantenimientos:
                mantenimiento.nombre = nombre
                mantenimiento.descripcion = descripcion
                session.commit()
                session.close()
            return True
        else:
            return False

    def eliminar_mantenimiento(self, id):
        session = Session()
        mantenimientos = session.query(Mantenimiento).filter(Mantenimiento.id == id+1).all()
        if len(mantenimientos) != 0:
            for mantenimiento in mantenimientos:
                session.delete(mantenimiento)
                session.commit()
                session.close()
                return True
        else:
            return False
    
    def validar_crear_editar_mantenimiento(self, nombre, descripcion):
        validacion = False
        if nombre!=None and descripcion!=None:
            validacion = True
        return validacion
    
    def dar_acciones_auto(self, id_auto):
        session = Session()
        acciones = session.query(Accion).filter(Accion.id_auto == id_auto+1).all()
        if len(acciones) == 0:
            return False
        else:
            return acciones

    def dar_accion(self, id_auto, id_accion):
        session = Session()
        acciones = session.query(Accion).filter(Accion.id_accion == id_accion+1).all()
        for accion in acciones:
            return accion

    def crear_accion(self, mantenimiento, id_auto, valor, kilometraje, fecha):
        session = Session()
        Session.expire_on_commit = False
        if type(mantenimiento) == str:
            mantenimiento = session.query(Mantenimiento).filter(Mantenimiento.nombre == mantenimiento).first()
        if  valor != 0 and kilometraje != 0:
            accion = Accion(id_auto = id_auto+1, mantenimiento = mantenimiento, valor = valor, kilometraje = kilometraje, fecha = datetime.strptime(str(fecha), "%Y-%m-%d"))
            session.add(accion)
            session.commit()
            
            return True    
        else:
            session.close()
            return False 

    def editar_accion(self, id_accion, mantenimiento, id_auto, valor, kilometraje, fecha):
        session = Session()
        acciones = session.query(Accion).filter(Accion.id_accion == id_accion+1).all()
        if len(acciones) != 0  and mantenimiento != None and id_auto+1 != 0 and valor != 0 and kilometraje != 0 and len(fecha) != 0:
            for accion in acciones:
                accion.id_auto = id_auto+1
                accion.valor = valor
                accion.kilometraje = kilometraje
                accion.fecha = datetime.strptime(str(fecha), "%Y-%m-%d")
                session.commit()
                session.close()
            return True
        else:
            return False

    def eliminar_accion(self, id_auto, id_accion):
        session = Session()
        accion = session.query(Accion).filter(Accion.id_accion == id_accion+1).first()
        if accion != None:
            session.delete(accion)
            session.commit()
            session.close()
            return True
        else:
            return False

    def validar_crear_editar_accion(self, id_accion, mantenimiento, id_auto, valor, kilometraje, fecha):
        validacion = False
        try:
            float(kilometraje)
            float(valor)
            validacion = True
        except ValueError:
            validacion = False
        return validacion

    def dar_reporte_ganancias(self, id_auto):
        session = Session()
        vehiculo = session.query(Vehiculo).filter(Vehiculo.id == id_auto+1).first()
        if vehiculo != None :
            acciones = session.query(Accion).filter(Accion.id_auto == id_auto+1).all()
            if len(acciones) != 0:
                total = 0
                gastos = []
                kilometraje = 0
                for accion in acciones:
                    gastos += [accion.fecha.year, accion.valor]
                    kilometraje += accion.kilometraje
                    total += accion.valor 
                gastos += [('Total',total)]
                gastos = [x for x in zip(*[iter(gastos)]*2)]
                return gastos, kilometraje
            else:
                session.close()
                return [('Total',0)], 0 
        else:
            return False


    