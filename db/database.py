from sqlalchemy import create_engine


# Variable cadena de conexión
MARIADB_URL = "mysql+pymysql://root:admin@127.0.0.1:3315/database_econoconnect"
#Crea el objeto conexion de la base de datos
engine = create_engine(MARIADB_URL)

