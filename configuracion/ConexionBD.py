
import mysql.connector


class ConexionBD:

    def __init__(self):
        self.configuracion = {
            "host": "localhost",
            "user": "root",
            "password": "",
            "database": "acueducto_veredal"
        }

    def obtener_conexion(self):
        return mysql.connector.connect(**self.configuracion)
