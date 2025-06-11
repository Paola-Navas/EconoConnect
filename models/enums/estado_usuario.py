#Enum: Tipo de Dato Personalizado
#Uso: Restringir variables de algunos valores
from enum import Enum

class EstadoUsuario(Enum):
    Activo = "activo"
    Inactivo = "inactivo"
