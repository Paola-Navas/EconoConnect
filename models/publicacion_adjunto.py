#importar modelo base
from db import Base

#importaciones de las clases sqlalchemy
from sqlalchemy import Column, Integer, ForeignKey

class PublicacionAdjunto(Base):
    __tablename__ = "publicacion_adjunto"
    id_publicacion = Column(Integer, ForeignKey('publicacion.id_publicacion'), primary_key=True)
    id_adjunto = Column(Integer, ForeignKey('adjunto.id_adjunto'), primary_key=True)

