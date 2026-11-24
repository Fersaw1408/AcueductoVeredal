
from modelos.Arista import Arista
from repositorios.Interfaces import IConexionRepositorio


class ConexionRepositorio(IConexionRepositorio):

    def __init__(self, conexion):
        self.conexion = conexion

    def obtener_todas(self):
        conexion = self.conexion.obtener_conexion()
        cursor = conexion.cursor()

        try:
            consulta = """
                SELECT v1.nombre, v2.nombre, c.distancia
                FROM conexiones c
                INNER JOIN veredas v1
                    ON c.origen_id = v1.id
                INNER JOIN veredas v2
                    ON c.destino_id = v2.id
                ORDER BY c.id
            """

            cursor.execute(consulta)
            resultados = cursor.fetchall()

            return [
                Arista(origen, destino, distancia)
                for origen, destino, distancia in resultados
            ]

        finally:
            cursor.close()
            conexion.close()
