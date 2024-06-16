from sqlalchemy import Column, Integer, DateTime, Date
from src.modelo.mantenimiento import Mantenimiento
from src.modelo.declarative_base import Base
from sqlalchemy.orm import relationship
from datetime import date

class Accion(Base):

  __tablename__ = 'accion'
  id_accion = Column(Integer,primary_key=True, autoincrement=True)
  id_auto = Column(Integer)
  kilometraje = Column(Integer)
  valor = Column(Integer)
  mantenimiento = relationship("Mantenimiento", cascade='all, delete, delete-orphan', uselist=False)
  fecha = Column(Date(), default=date.today())
