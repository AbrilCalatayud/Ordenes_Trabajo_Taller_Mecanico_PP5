class Mecanico:
    def __init__(self, legajo: int):
        self.legajo = legajo
        self.ocupado = False

    def asignar_a_orden(self) -> None:
        if self.ocupado:
            raise ValueError(f"El mecánico con legajo '{self.legajo}' ya tiene una orden activa, no puede ser asignado a otra.")

        self.ocupado = True

    def disponible(self) -> None:
        self.ocupado = False