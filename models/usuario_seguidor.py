#importar modelo base
from db import Base

#importaciones de las clases sqlalchemy
from sqlalchemy import Column, Integer, ForeignKey

class UsuarioSeguidor(Base):
    __tablename__ = "usuario_seguidor"
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'), primary_key=True)
    id_usuario_seguidor = Column(Integer, ForeignKey('usuario.id_usuario'), primary_key=True)
