class Error(Exception)
    pass


class DimensionError(Exception):
    def __init__(self, mensaje, dimension, maximo):
        super().__init__(mensaje)
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self):
        return f"Error de dimensiones: {self.dimension}. Máximo permitido: {self.maximo}. {super().__str__()}"
 