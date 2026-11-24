
from abc import ABC, abstractmethod


class IVeredaRepositorio(ABC):

    @abstractmethod
    def obtener_todas(self):
        pass


class IConexionRepositorio(ABC):

    @abstractmethod
    def obtener_todas(self):
        pass
