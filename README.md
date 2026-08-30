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

## Tabla de Relaciones
