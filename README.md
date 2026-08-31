# Tarea de Paradigmas de Programación 5: Órdenes de trabajo de un taller mecánico

## Consigna: [Link](https://paradigmas-v-fie.github.io/reuniones-2026/ejercicios/reuniones/clase-2.html)

## Análisis de dominio
### Listado de conceptos
#### Son clases:
* Taller Mecánico.
* Vehículo.
* Orden de Trabajo.
* Item de Trabajo.
* Mecánico.
#### NO son clases:
* *Visita*, el hecho de que un vehículo "visite" el taller se representa directamente en la creación de una OrdenDeTrabajo. Crear una clase Visita sería redundante.
* *Mano de obra*/*Repuesto*, no son clases separadas, ya que tienen la misma estructura (nombre y costo) y el mismo comportamiento (debe pertencer a una y solo una OrdenDeTrabajo), por lo que simplemente son instancias de ItemDeTrabajo. Por ahora, no hay razón para diferenciarlas, pero si así fuera, podría hacerse una herencia de la clase ItemDeTrabajo
* *Plantilla*, porque es una estructura que únicamente agrupa a los mecánicos del taller. No tiene lógica de negocio propia ni responsabilidades adicionales. Puede representarse como una colección de Metcánicos dentro del Taller.
* *Presupuesto*, porque es solo es un valor que surge de la suma de los costos de los ItemDeTrabajo contenidos en una OrdenDeTrabajo. Si se representara como una clase, presentaría el riesgo de que se desincronicen los datos. Se implementa como un método (orden.presupuesto()).
* *Estado de la Orden*, porque simplemente puede ser un atributo booleano de la clase OrdenDeTrabajo (en curso/terminada). No hay anda que indique que podría ser más complicado por el momento.

## Tarjetas CRC
| Clase | Responsabilidades | Colaboradores |
|---|---|---|
| OrdenDeTrabajo | agregar ítems, calcular presupuesto, saber si está cerrada | ItemDeTrabajo, Vehiculo, Mecanico |
| ItemDeTrabajo | validar si no tiene una orden ya asignada |  |
| Vehiculo | validar si no tiene órdenes abiertas (en reparación o no), actualizar su estado de reparación |  |
| Mecanico | saber si está disponible, cambiar su disponibilidad |  |
| Taller | crear órdenes, cerrar órdenes, registrar mecánicos, asignar mecánicos | OrdenDeTrabajo, Mecanico, Vehiculo |

## Tabla de Relaciones
| Relación | Tipo | Justificación | Por qué no es otro tipo |
|---|---|---|---|
| OrdenDeTrabajo - ItemDeTrabajo | Composición | No tiene sentido su existencia fuera de la orden, es una parte que no puede existir por sí sola. | Es una parte de OrdenDeTrabajo (esta lo posee) así que la otra opción sería que fuera una agregación, pero no lo es, porque se debería cumplir que puede seguir existiendo independientemente del ciclo de vida de la orden. |
| OrdenDeTrabajo - Vehiculo| Asociación | Es el vehículo que se está reparando es un dato de la orden, pero el vehículo existe y existió fuera de la orden e incluso puede estar asociado a varias de estas los largo de su ciclo de vida. | No es agregación ni composición, porque la orden no posee al vehiculo, es una entidad separada cuya patente es necesaria para identificar de qué auto se trata. No es dependencia, porque la orden almacena al vehículo en un atributo. |
| Orden de Trabajo - Mecanico | Asociación | Es el mecánico que está asignado para reparar el vehículo es un dato de la orden, pero el vehículo existe y existió fuera de la orden e incluso puede estar asociado a varias de estas los largo de su ciclo de vida. | No es agregación ni composición, porque el mecánico es una entidad separada, no lo posee la orden. No es dependencia, porque la orden almacena al vehículo en un atributo. |
| Taller - OrdenDeTrabajo | Composición | El taller crea, contiene y administra las órdenes de trabajo, estas no existen ni se gestionan por fuera del sistema del taller que las emite. | No es Agregación ni Asociación porque las órdenes son generadas y mantenidas dentro del ciclo de vida del taller y no existen fuera de este. |
| Taller - Mecanico | Agregación | El taller agrupa a los mecánicos dentro de su planilla de personal. Mantiene una colección y administra a qué órdenes de trabajo serán asignados. | No es Asociación, ya que el taller agrupa a una conjunto de mecánicos, son parte de este. No es Composición, porque los mecánicos no dejan de existir si cierra el taller o si se dan de baja en la planilla, son entidades con un ciclo de vida independiente. Si existieran varios talleres en el sistema, podría formar parte de otros talleres en diferentes momentos. |
| Taller - Vehiculo | Dependencia | El taller utiliza una instancia de vehículo como parámetro para crear la orden. | No es Asociación, Agregación ni Composición porque el taller en sí no almacena al vehículo ni retiene una referencia permanente de él. |
