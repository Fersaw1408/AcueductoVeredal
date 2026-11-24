from configuracion.ConexionBD import ConexionBD
from repositorios.VeredaRepositorio import VeredaRepositorio
from repositorios.ConexionRepositorio import ConexionRepositorio
from servicios.PrimServicio import PrimServicio
from interfaz.Menu import Menu


def main():

    conexion = ConexionBD()

    vereda_repositorio = VeredaRepositorio(conexion)
    conexion_repositorio = ConexionRepositorio(conexion)

    prim_servicio = PrimServicio()

    menu = Menu(
        vereda_repositorio,
        conexion_repositorio,
        prim_servicio
    )

    menu.ejecutar()


main()