from solucion.orden_de_trabajo import OrdenDeTrabajo
from solucion.item_de_trabajo import ItemDeTrabajo
from solucion.vehiculo import Vehiculo
from solucion.mecanico import Mecanico

class Taller:
    def __init__(self):
        self.ordenes = []
        self.mecanicos = []
        self.siguiente_numero_de_orden = 1
        self.siguiente_numero_de_legajo = 1

    def crear_orden(self, vehiculo, mecanico) -> OrdenDeTrabajo:
        vehiculo.asignar_a_orden()
        try:
            mecanico.asignar_a_orden()
        except ValueError:
            vehiculo.liberar() #para que no quede en reparación si el mecánico que se intentó asignar no estaba disponible
            raise #para que vuelva a lanzar el mismo error hacia quien intentó crear la orden

        nueva_orden = OrdenDeTrabajo(self.siguiente_numero_de_orden, vehiculo, mecanico)

        self.siguiente_numero_de_orden += 1

        self.ordenes.append(nueva_orden)

        return nueva_orden

    