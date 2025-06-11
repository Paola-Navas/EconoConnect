#importar modelo base
from db import Base

#importaciones de las clases sqlalchemy
from sqlalchemy import Column, Integer, Text, ForeignKey, TIMESTAMP

class Comentario(Base):
    __tablename__ = "comentario"
    id_comentario = Column(Integer, primary_key=True)
    publicacion_id = Column(Integer, ForeignKey('publicacion.id_publicacion'))
    usuario_id = Column(Integer, ForeignKey('usuario.id_usuario'))
    contenido = Column(Text)
    fecha_creacion = Column(TIMESTAMP)

