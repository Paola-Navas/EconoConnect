#Enum: Tipo de Dato Personalizado
#Uso: Restringir variables de algunos valores
from enum import Enum

class EstadoPublicacion(Enum):
    Publicada = "publicada"
    Eliminada = "eliminada"
    Archivada = "archivada"