#importar modelo base
from db import Base

#importaciones de las clases sqlalchemy
from sqlalchemy import Column, Integer, ForeignKey


class ChatMensajeAdjunto(Base):
    __tablename__ = "chat_mensaje_adjunto"
    id_mensaje = Column(Integer, ForeignKey('chat_mensaje.id_mensaje'), primary_key=True)
    id_adjunto = Column(Integer, ForeignKey('adjunto.id_adjunto'), primary_key=True)
