#Enum: Tipo de Dato Personalizado
#Uso: Restringir variables de algunos valores
from enum import Enum

class VerificacionUsuario(Enum):
    Pendiente = "pendiente"
    Aprobado = "aprobado"
    Rechazado = "rechazado"