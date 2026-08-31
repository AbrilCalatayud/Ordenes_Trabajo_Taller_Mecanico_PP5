class ItemDeTrabajo:
    def __init__(self, descripcion: str, costo: float):
        self.descripcion = descripcion
        self.costo = costo
        self.asignado = False

    def marcar_como_asignado(self) -> None:
        if self.asignado:
            raise ValueError(f"El ítem '{self.descripcion}' ya está asignado a una orden.")
        
        self.asignado = True