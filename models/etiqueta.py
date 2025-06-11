#importar modelo base
from db import Base

#importaciones de las clases sqlalchemy
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, TIMESTAMP

from models.enums import EstadoEtiqueta
class Etiqueta(Base):
    __tablename__ = "etiqueta"
    id_etiqueta = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    descripcion = Column(String(450))
    autor_id = Column(Integer, ForeignKey('usuario.id_usuario'))
    estado = Column(Enum(EstadoEtiqueta))
    fecha_creacion = Column(TIMESTAMP)
