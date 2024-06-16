from sqlalchemy import Column, String, Integer, ForeignKey
from src.modelo.declarative_base import Base

class Mantenimiento(Base):

  __tablename__ = 'mantenimiento'
  id = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String)
  descripcion = Column(String)
  accion = Column(Integer, ForeignKey('accion.id_accion'))

  def __getitem__(self, i):
        return self.nombre