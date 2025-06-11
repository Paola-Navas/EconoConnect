#importar modelo base
from db import Base

#importaciones de las clases sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Date

class DatoGrafica(Base):
    __tablename__ = "dato_grafica"
    id_dato = Column(Integer, primary_key=True)
    id_grafica = Column(Integer, ForeignKey('grafica.id_grafica'))
    etiqueta = Column(String(100))
    fecha = Column(Date)
    valor = Column(DECIMAL(20, 6))

