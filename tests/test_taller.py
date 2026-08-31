import pytest
from solucion.item_de_trabajo import ItemDeTrabajo
from solucion.mecanico import Mecanico
from solucion.orden_de_trabajo import OrdenDeTrabajo
from solucion.taller import Taller
from solucion.vehiculo import Vehiculo

def test_camino_feliz_crear_orden_agregar_items_presupuesto_y_cierre():
    taller = Taller()
    mecanico = taller.registrar_mecanico()
    vehiculo = Vehiculo("ABC123")

    orden = taller.crear_orden(vehiculo, mecanico)

    item_1 = ItemDeTrabajo("Cambio de aceite", 15000.0)
    item_2 = ItemDeTrabajo("Filtro de aire", 5000.0)

    orden.agregar_item(item_1)
    orden.agregar_item(item_2)

    assert orden.numero_orden == 1
    assert orden.cerrado is False
    assert vehiculo.en_reparacion is True
    assert mecanico.ocupado is True
    assert orden.presupuesto() == 20000.0

    orden.cerrar()
    assert orden.cerrada is True
    assert vehiculo.en_reparacion is False
    assert mecanico.ocupado is False

def test_rechazo_asignar_mismo_item_a_dos_ordenes():
    taller = Taller()
    mecanico_1 = taller.registrar_mecanico()
    vehiculo_1 = Vehiculo("AAA111")
    mecanico_2 = taller.registrar_mecanico()
    vehiculo_2 = Vehiculo("BBB222")

    orden1 = taller.crear_orden(vehiculo_1, mecanico_1)
    orden2 = taller.crear_orden(vehiculo_2, mecanico_2)

    item = ItemDeTrabajo("Alineación y balanceo", 10000.0)

    orden1.agregar_item(item)

    with pytest.raises(ValueError):
        orden2.agregar_item(item)
