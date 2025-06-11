#importar modelo base
from db import Base

#importaciones de las clases sqlalchemy
from sqlalchemy import Column, Integer, String, Enum

from models.enums import TipoChat

class Chat(Base):
    __tablename__ = "chat"
    id_chat = Column(Integer, primary_key=True)
    tipo = Column(Enum(TipoChat))
    nombre = Column(String(100))

