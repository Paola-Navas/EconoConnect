#importar modelo base
from db import Base

#importaciones de las clases sqlalchemy
from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP

from models.enums import EstadoUsuario, VerificacionUsuario

class Usuario(Base):
    __tablename__ = "usuario"
    id_usuario = Column(Integer, 
                        primary_key=True, 
                        autoincrement=True
                        )
    nombre_usuario = Column(String(50))
    correo = Column(String(100))
    contrasena = Column(String(255))
    estado = Column(Enum(EstadoUsuario))
    verificacion = Column(Enum(VerificacionUsuario))
    telefono = Column(Integer)
    direccion = Column(String(255))
    pais = Column(String(50))
    fecha_creacion = Column(TIMESTAMP)