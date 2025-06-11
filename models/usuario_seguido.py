#importar modelo base
from db import Base

#importaciones de las clases sqlalchemy
from sqlalchemy import Column, Integer, ForeignKey

class UsuarioSeguido(Base):
    __tablename__ = "usuario_seguido"
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'), primary_key=True)
    id_usuario_seguido = Column(Integer, ForeignKey('usuario.id_usuario'), primary_key=True)
