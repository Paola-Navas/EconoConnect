#importar modelo base
from db import Base

#importaciones de las clases sqlalchemy
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, TIMESTAMP

from models.enums import EstadoForo

class Foro(Base):
    __tablename__ = "foro"
    id_foro = Column(Integer, 
                     primary_key=True
                     )
    nombre = Column(String(100))
    descripcion = Column(String(450))
    autor_id = Column(Integer, ForeignKey('usuario.id_usuario'))
    estado = Column(Enum(EstadoForo))
    fecha_creacion = Column(TIMESTAMP)
