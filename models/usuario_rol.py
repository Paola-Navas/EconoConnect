#importar modelo base
from db import Base

#importaciones de las clases sqlalchemy
from sqlalchemy import Column, Integer, ForeignKey

class UsuarioRol(Base):
    __tablename__ = "usuario_rol"
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'), 
                        primary_key=True
                        )
    id_rol = Column(Integer, ForeignKey('rol.id_rol'), 
                    primary_key=True
                    )