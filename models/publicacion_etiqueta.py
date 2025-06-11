#importar modelo base
from db import Base

#importaciones de las clases sqlalchemy
from sqlalchemy import Column, Integer, ForeignKey

class PublicacionEtiqueta(Base):
    __tablename__ = "publicacion_etiqueta"
    id_publicacion = Column(Integer, ForeignKey('publicacion.id_publicacion'), primary_key=True)
    id_etiqueta = Column(Integer, ForeignKey('etiqueta.id_etiqueta'), primary_key=True)

