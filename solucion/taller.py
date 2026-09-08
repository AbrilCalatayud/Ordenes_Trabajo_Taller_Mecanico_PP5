from solucion.orden_de_trabajo import OrdenDeTrabajo
from solucion.vehiculo import Vehiculo
from solucion.mecanico import Mecanico

class Taller:
    def __init__(self):
        self.ordenes = []
        self.mecanicos = []
        self.siguiente_numero_de_orden = 1
        self.siguiente_numero_de_legajo = 1

    def crear_orden(self, vehiculo: Vehiculo, mecanico: Mecanico) -> OrdenDeTrabajo:

        nueva_orden = OrdenDeTrabajo(self.siguiente_numero_de_orden, vehiculo, mecanico)

        self.siguiente_numero_de_orden += 1

        self.ordenes.append(nueva_orden)

        return nueva_orden

    def registrar_mecanico(self) -> Mecanico:
        nuevo_mecanico = Mecanico(self.siguiente_numero_de_legajo)

        self.siguiente_numero_de_legajo += 1

        self.mecanicos.append(nuevo_mecanico)

        return nuevo_mecanico