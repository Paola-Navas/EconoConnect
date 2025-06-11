#Enum: Tipo de Dato Personalizado
#Uso: Restringir variables de algunos valores
from enum import Enum

class TipoAdjunto(Enum):
    Imagen = "imagen"
    Video = "video" 
    Enlace = "enlace"
    Grafico = "grafico"