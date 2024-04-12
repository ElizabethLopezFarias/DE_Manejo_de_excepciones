# foto.py
from error import DimensionError

class Foto:
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        self.ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        #llama a excepción de tipo DimensionError si ancho es inválido
        if ancho < 1 or ancho > self.MAX:
            raise DimensionError("Ancho inválido", ancho, self.MAX)
        self.__ancho = ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        #llama a excepción de tipo DimensionError si alto es inválido
        if alto < 1 or alto > self.MAX:
            raise DimensionError("Alto inválido", alto, self.MAX)
        self.__alto = alto
