#importar modelo base
from db import Base

#importaciones de las clases sqlalchemy
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Date

#dependencias
from datetime import datetime

from models.enums import TipoAdjunto

class Adjunto(Base):
    __tablename__ = "adjunto"
    id_adjunto = Column(Integer, primary_key=True)
    tipo = Column(Enum(TipoAdjunto))
    url = Column(String(255))
    autor_id = Column(Integer, ForeignKey('usuario.id_usuario'))
    fecha_creacion = Column(Date, default=datetime.now())