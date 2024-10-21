## Prueba de conexión a la base de datos 

import mysql.connector
from mysql.connector import Error

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Francia234",
        database="db_energia"
    )
    if db.is_connected():
        print("Conexión exitosa a la base de datos")
except Error as e:
    print(f"Error al conectar a MySQL: {e}")
finally:
    if db.is_connected():
        db.close()
        print("Conexión cerrada")