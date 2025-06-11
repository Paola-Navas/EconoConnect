#importar modelo base
from db import Base

#importaciones de las clases sqlalchemy
from sqlalchemy import Column, Integer, ForeignKey

class ComentarioAdjunto(Base):
    __tablename__ = "comentario_adjunto"
    id_comentario = Column(Integer, ForeignKey('comentario.id_comentario'), primary_key=True)
    id_adjunto = Column(Integer, ForeignKey('adjunto.id_adjunto'), primary_key=True)

