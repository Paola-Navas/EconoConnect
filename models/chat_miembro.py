#importar modelo base
from db import Base

#importaciones de las clases sqlalchemy
from sqlalchemy import Column, Integer, ForeignKey
class ChatMiembro(Base):
    __tablename__ = "chat_miembro"
    id_chat = Column(Integer, ForeignKey('chat.id_chat'), primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'), primary_key=True)
