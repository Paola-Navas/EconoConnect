#importar modelo base
from db import Base

#importaciones de las clases sqlalchemy
from sqlalchemy import Column, Integer, Text, ForeignKey, TIMESTAMP

class ChatMensaje(Base):
    __tablename__ = "chat_mensaje"
    id_mensaje = Column(Integer, primary_key=True)
    id_chat = Column(Integer, ForeignKey('chat.id_chat'))
    contenido = Column(Text)
    fecha_envio = Column(TIMESTAMP)
    hora_envio = Column(TIMESTAMP)
    id_chatmensaje = Column(Integer, ForeignKey('chat_miembro.id_chat'), primary_key=True)
