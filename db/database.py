from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# Variable cadena de conexión
MARIADB_URL = "mysql+pymysql://root:admin@127.0.0.1:3315/database_econoconnect"
#Crea el objeto conexion de la base de datos
engine = create_engine(MARIADB_URL)
#Plantilla base para los modelos 
Base = declarative_base()
