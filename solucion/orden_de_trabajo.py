from solucion.item_de_trabajo import ItemDeTrabajo
from solucion.vehiculo import Vehiculo
from solucion.mecanico import Mecanico

class OrdenDeTrabajo:
    def __init__(self, numero_orden: int, vehiculo: Vehiculo, mecanico: Mecanico):
        self.numero_orden = numero_orden
        self.vehiculo = vehiculo
        self.mecanico = mecanico
        self._items = []
        self.cerrada = False

    def agregar_item(self, item: ItemDeTrabajo) -> None:
        if self.cerrada:
            raise ValueError("No se pueden agregar ítems a una orden cerrada.")

        item.marcar_como_asignado()

        self._items.append(item)

    def presupuesto(self):
        return sum(item.costo for item in self._items) #sum devuelve 0 si la colección está vacía
