#importar modelo base
from db import Base

#importaciones de las clases sqlalchemy
from sqlalchemy import Column, Integer, String, TIMESTAMP

class Grafica(Base):
    __tablename__ = "grafica"
    id_grafica = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    descripcion = Column(String(255))
    fecha_creacion = Column(TIMESTAMP)