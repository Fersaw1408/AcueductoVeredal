
from modelos.Grafo import Grafo


class Menu:

    def __init__(self, vereda_repositorio, conexion_repositorio, prim_servicio):
        self.vereda_repositorio = vereda_repositorio
        self.conexion_repositorio = conexion_repositorio
        self.prim_servicio = prim_servicio

    def mostrar_resultado(self, inicio, resultado):

        
        print(f"ALGORITMO DE PRIM DESDE {inicio}")
        

        for numero, paso in enumerate(resultado["pasos"], 1):

            print(f"\nITERACIÓN {numero}")
            print("Vértices conectados:", paso["conectadas"])

            print("\nAristas candidatas:")

            for arista in paso["candidatas"]:
                print(arista)

            print("\nArista elegida:", paso["elegida"])

        print("\nÁRBOL DE EXPANSIÓN MÍNIMA")

        for arista in resultado["arbol"]:
            print(arista)

        print("\nVeredas conectadas:")
        print(" -> ".join(resultado["vertices"]))

        print("\nCantidad de conexiones:", len(resultado["arbol"]))
        print("Longitud total:", resultado["total"], "km")

    def comparar_arboles(self, resultado_a, resultado_f):

        arbol_a = {
            (
                min(a.origen, a.destino),
                max(a.origen, a.destino),
                a.distancia
            )
            for a in resultado_a["arbol"]
        }

        arbol_f = {
            (
                min(a.origen, a.destino),
                max(a.origen, a.destino),
                a.distancia
            )
            for a in resultado_f["arbol"]
        }

        if arbol_a == arbol_f:
            print("Los árboles de expansión mínima son iguales.")
        else:
            print("Los árboles de expansión mínima son diferentes.")

        if resultado_a["total"] == resultado_f["total"]:
            print("El costo total es igual desde ambos puntos.")
        else:
            print("El costo total es diferente.")

    def ejecutar(self):

        veredas = self.vereda_repositorio.obtener_todas()
        aristas = self.conexion_repositorio.obtener_todas()

        grafo = Grafo(veredas, aristas)

        while True:

            print("\n ACUEDUCTO VEREDAL ")
            print("1. Ejecutar Prim desde A")
            print("2. Ejecutar Prim desde F")
            print("3. Comparar ambos resultados")
            print("4. Mostrar veredas y conexiones")
            print("5. Salir")

            opcion = input("\nSeleccione una opción: ")

            try:

                if opcion == "1":

                    resultado = self.prim_servicio.ejecutar("A", grafo)
                    self.mostrar_resultado("A", resultado)

                elif opcion == "2":

                    resultado = self.prim_servicio.ejecutar("F", grafo)
                    self.mostrar_resultado("F", resultado)

                elif opcion == "3":

                    resultado_a = self.prim_servicio.ejecutar("A", grafo)
                    resultado_f = self.prim_servicio.ejecutar("F", grafo)

                    self.mostrar_resultado("A", resultado_a)
                    self.mostrar_resultado("F", resultado_f)

                    print("\n COMPARACIÓN ")
                    print("Costo desde A:", resultado_a["total"], "km")
                    print("Costo desde F:", resultado_f["total"], "km")

                    self.comparar_arboles(resultado_a, resultado_f)

                elif opcion == "4":

                    print("\nVEREDAS REGISTRADAS")

                    for vereda in grafo.obtener_vertices():
                        print(vereda)

                    print("\nCONEXIONES REGISTRADAS")

                    for arista in grafo.obtener_aristas():
                        print(arista)

                    print("\nTotal de veredas:", grafo.obtener_cantidad_vertices())
                    print("Total de conexiones:", grafo.obtener_cantidad_aristas())

                elif opcion == "5":

                    print("Programa finalizado.")
                    break

                else:

                    print("Opción no válida.")

            except ValueError as error:

                print("Error:", error)

            except Exception as error:

                print("Error al consultar o procesar los datos:", error)
