from xmlrpc.client import Boolean
from sqlalchemy import Column, Integer, String, Boolean, Float
from src.modelo.declarative_base import Base

class Vehiculo(Base):

  __tablename__ = 'vehiculo'
  id = Column(Integer, primary_key=True, autoincrement=True)
  placa = Column(String)
  marca = Column(String)
  modelo = Column(String)
  color = Column(String)
  kilometraje = Column(Float)
  cilindraje = Column(String)
  tipoDeCombustible = Column(String)
  valorVenta = Column(Float)
  kilometrajeVenta = Column(Float)
  vendido = Column(Boolean, default=False)

  def __getitem__(self, i):
        return self.placa