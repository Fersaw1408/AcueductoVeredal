
from modelos.Vereda import Vereda
from repositorios.Interfaces import IVeredaRepositorio


class VeredaRepositorio(IVeredaRepositorio):

    def __init__(self, conexion):
        self.conexion = conexion

    def obtener_todas(self):
        conexion = self.conexion.obtener_conexion()
        cursor = conexion.cursor()

        try:
            cursor.execute(
                "SELECT id, nombre FROM veredas ORDER BY nombre"
            )

            resultados = cursor.fetchall()

            return [
                Vereda(id, nombre)
                for id, nombre in resultados
            ]

        finally:
            cursor.close()
            conexion.close()
