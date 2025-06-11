#importar modelo base
from db import Base

#importaciones de las clases sqlalchemy
from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey, TIMESTAMP

from models.enums import EstadoPublicacion

class Publicacion(Base):
    __tablename__ = "publicacion"
    id_publicacion = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id_usuario'))
    foro_id = Column(Integer, ForeignKey('foro.id_foro'))
    titulo = Column(String(200))
    contenido = Column(Text)
    estado = Column(Enum(EstadoPublicacion))
    fecha_creacion = Column(TIMESTAMP)
