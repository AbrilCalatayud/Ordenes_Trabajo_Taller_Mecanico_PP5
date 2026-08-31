from solucion.item_de_trabajo import ItemDeTrabajo
from solucion.vehiculo import Vehiculo
from solucion.mecanico import Mecanico

class OrdenDeTrabajo:
    def __init__(self, numero_orden: int, vehiculo: Vehiculo, mecanico: Mecanico):
        self.numero_orden = numero_orden
        
        vehiculo.asignar_a_orden()
        try:
            mecanico.asignar_a_orden()
        except ValueError:
            vehiculo.liberar() #para que no quede en reparación si el mecánico que se intentó asignar no estaba disponible
            raise #para que vuelva a lanzar el mismo error hacia quien intentó crear la orden

        self.vehiculo = vehiculo
        self.mecanico = mecanico
        self._items = []
        self.cerrada = False

    def agregar_item(self, item: ItemDeTrabajo) -> None:
        if self.cerrada:
            raise ValueError("No se pueden agregar ítems a una orden cerrada.")

        item.marcar_como_asignado()

        self._items.append(item)

    def presupuesto(self) -> float:
        return sum(item.costo for item in self._items) #sum devuelve 0 si la colección está vacía

    def cerrar(self) -> None:
        if self.cerrada:
            raise ValueError("La orden de trabajo ya se encuentra cerrada.")

        self.cerrada = True

        self.vehiculo.liberar()

        self.mecanico.liberar()


