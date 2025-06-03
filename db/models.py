from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey, TIMESTAMP, DECIMAL, Date
from sqlalchemy.orm import relationship
from .database import Base


class Usuario(Base):
    __tablename__ = "usuario"
    id_usuario = Column(Integer, 
                        primary_key=True, 
                        autoincrement=True
                        )
    nombre_usuario = Column(String(50))
    correo = Column(String(100))
    contrasena = Column(String(255))
    estado = Column(Enum('activo', 'inactivo'))
    verificacion = Column(Enum('pendiente', 'aprobado', 'rechazado'))
    telefono = Column(Integer)
    direccion = Column(String(255))
    pais = Column(String(50))
    fecha_creacion = Column(TIMESTAMP)



class Rol(Base):
    __tablename__ = "rol"
    id_rol = Column(Integer, 
                    primary_key=True
                    )
    nombre_rol = Column(String(50))


class UsuarioRol(Base):
    __tablename__ = "usuario_rol"
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'), 
                        primary_key=True
                        )
    id_rol = Column(Integer, ForeignKey('rol.id_rol'), 
                    primary_key=True
                    )

class Seguidores(Base):
    __tablename__ = "seguidores"

    usuario_seguidor = Column(Integer, ForeignKey('usuario.id_usuario'), primary_key=True)
    usuario_seguido = Column(Integer, ForeignKey('usuario.id_usuario'), primary_key=True)
class Foro(Base):
    __tablename__ = "foro"
    id_foro = Column(Integer, 
                     primary_key=True
                     )
    nombre = Column(String(100))
    descripcion = Column(String(450))
    autor_id = Column(Integer, ForeignKey('usuario.id_usuario'))
    estado = Column(Enum('activo', 'inactivo'))
    fecha_creacion = Column(TIMESTAMP)


class Publicacion(Base):
    __tablename__ = "publicacion"
    id_publicacion = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id_usuario'))
    foro_id = Column(Integer, ForeignKey('foro.id_foro'))
    titulo = Column(String(200))
    contenido = Column(Text)
    estado = Column(Enum('publicada', 'eliminada', 'archivada'))
    fecha_creacion = Column(TIMESTAMP)


class Etiqueta(Base):
    __tablename__ = "etiqueta"
    id_etiqueta = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    descripcion = Column(String(450))
    autor_id = Column(Integer, ForeignKey('usuario.id_usuario'))
    estado = Column(Enum('activa', 'inactiva'))
    fecha_creacion = Column(TIMESTAMP)


class PublicacionEtiqueta(Base):
    __tablename__ = "publicacion_etiqueta"
    id_publicacion = Column(Integer, ForeignKey('publicacion.id_publicacion'), primary_key=True)
    id_etiqueta = Column(Integer, ForeignKey('etiqueta.id_etiqueta'), primary_key=True)


class Comentario(Base):
    __tablename__ = "comentario"
    id_comentario = Column(Integer, primary_key=True)
    publicacion_id = Column(Integer, ForeignKey('publicacion.id_publicacion'))
    usuario_id = Column(Integer, ForeignKey('usuario.id_usuario'))
    contenido = Column(Text)
    fecha_creacion = Column(TIMESTAMP)


class ComentarioAdjunto(Base):
    __tablename__ = "comentario_adjunto"
    id_comentario = Column(Integer, ForeignKey('comentario.id_comentario'), primary_key=True)
    id_adjunto = Column(Integer, ForeignKey('adjunto.id_adjunto'), primary_key=True)


class Adjunto(Base):
    __tablename__ = "adjunto"
    id_adjunto = Column(Integer, primary_key=True)
    tipo = Column(Enum('imagen', 'video', 'enlace', 'grafico'))
    url = Column(String(255))
    autor_id = Column(Integer, ForeignKey('usuario.id_usuario'))
    fecha_creacion = Column(TIMESTAMP)


class PublicacionAdjunto(Base):
    __tablename__ = "publicacion_adjunto"
    id_publicacion = Column(Integer, ForeignKey('publicacion.id_publicacion'), primary_key=True)
    id_adjunto = Column(Integer, ForeignKey('adjunto.id_adjunto'), primary_key=True)


class Grafica(Base):
    __tablename__ = "grafica"
    id_grafica = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    descripcion = Column(String(255))
    fecha_creacion = Column(TIMESTAMP)


class DatoGrafica(Base):
    __tablename__ = "dato_grafica"
    id_dato = Column(Integer, primary_key=True)
    id_grafica = Column(Integer, ForeignKey('grafica.id_grafica'))
    etiqueta = Column(String(100))
    fecha = Column(Date)
    valor = Column(DECIMAL(20, 6))


class Chat(Base):
    __tablename__ = "chat"
    id_chat = Column(Integer, primary_key=True)
    tipo = Column(Enum('privado', 'grupo'))
    nombre = Column(String(100))


class ChatMensaje(Base):
    __tablename__ = "chat_mensaje"
    id_mensaje = Column(Integer, primary_key=True)
    id_chat = Column(Integer, ForeignKey('chat.id_chat'))
    contenido = Column(Text)
    fecha_envio = Column(TIMESTAMP)


class ChatMiembro(Base):
    __tablename__ = "chat_miembro"
    id_chat = Column(Integer, ForeignKey('chat.id_chat'), primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'), primary_key=True)
    id_chatmensaje = Column(Integer, ForeignKey('chat_mensaje.id_mensaje'), primary_key=True)


class ChatMensajeAdjunto(Base):
    __tablename__ = "chat_mensaje_adjunto"
    id_mensaje = Column(Integer, ForeignKey('chat_mensaje.id_mensaje'), primary_key=True)
    id_adjunto = Column(Integer, ForeignKey('adjunto.id_adjunto'), primary_key=True)

