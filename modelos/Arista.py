
class Arista:

    def __init__(self, origen, destino, distancia):
        self.origen = origen
        self.destino = destino
        self.distancia = float(distancia)

    def __str__(self):
        return f"{self.origen} - {self.destino}: {self.distancia} km"
