#Enum: Tipo de Dato Personalizado
#Uso: Restringir variables de algunos valores
from enum import Enum

class EstadoForo(Enum):
    Activo = "activa"
    Inactivo = "inactiva"