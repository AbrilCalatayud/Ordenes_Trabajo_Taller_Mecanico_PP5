class Vehiculo:
    def __init__(self, patente: str):
        self.patente = patente
        self.en_reparacion = False

    def asignar_a_orden(self) -> None:
        if self.en_reparacion:
            raise ValueError(f"El vehiculo con patente '{self.patente}' ya tiene una orden activa, no puede ser asignado a otra.")

        self.en_reparacion = True

    def reparado(self) -> None:
        self.en_reparacion = False