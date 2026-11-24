
class PrimServicio:

    def __init__(self):
        pass

    def ejecutar(self, inicio, grafo):

        vertices = set(grafo.obtener_vertices())
        aristas = grafo.obtener_aristas()

        if inicio not in vertices:
            raise ValueError("La vereda inicial no existe")

        conectadas = {inicio}
        arbol = []
        pasos = []
        total = 0

        while len(conectadas) < len(vertices):

            candidatas = [
                arista for arista in aristas
                if (arista.origen in conectadas) !=
                (arista.destino in conectadas)
            ]

            if not candidatas:
                raise ValueError("El grafo no está conectado")

            candidatas.sort(
                key=lambda arista: (
                    arista.distancia,
                    arista.origen,
                    arista.destino
                )
            )

            elegida = candidatas[0]

            pasos.append({
                "conectadas": sorted(conectadas),
                "candidatas": candidatas.copy(),
                "elegida": elegida
            })

            arbol.append(elegida)
            total += elegida.distancia

            conectadas.add(elegida.origen)
            conectadas.add(elegida.destino)

        return {
            "pasos": pasos,
            "arbol": arbol,
            "total": total,
            "vertices": sorted(conectadas)
        }
