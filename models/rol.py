#importar modelo base
from db import Base

#importaciones de las clases sqlalchemy
from sqlalchemy import Column, Integer, String

class Rol(Base):
    __tablename__ = "rol"
    id_rol = Column(Integer, 
                    primary_key=True
                    )
    nombre_rol = Column(String(50))