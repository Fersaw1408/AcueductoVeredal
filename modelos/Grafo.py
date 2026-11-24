
class Grafo:

    def __init__(self, veredas, aristas):
        self.veredas = veredas
        self.aristas = aristas

    def obtener_vertices(self):
        return [vereda.nombre for vereda in self.veredas]

    def obtener_aristas(self):
        return self.aristas

    def obtener_cantidad_vertices(self):
        return len(self.veredas)

    def obtener_cantidad_aristas(self):
        return len(self.aristas)
