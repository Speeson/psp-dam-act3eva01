👨‍🍳 PSP-DAM-ACTEVA03B - Simulación Concurrente de Cocina

Sistema de simulación de una cocina de restaurante mediante hilos concurrentes y bloqueos (Locks / Synchronized) para garantizar la exclusión mutua al gestionar pedidos. Implementado tanto en Java como en Python.

📋 Descripción

Este proyecto simula el acceso concurrente de múltiples cocineros (hilos) a una lista de pedidos compartida. El sistema implementa:

✅ Exclusión mutua mediante Lock (Python) y synchronized (Java).

✅ Hilos concurrentes (no procesos).

✅ Sincronización de hilos para acceder a recursos compartidos.

✅ Sección crítica protegida (lista de pedidos y fichero de log).

✅ Prevención de condiciones de carrera.

🎯 Objetivo Académico

Demostrar la comprensión de los conceptos de programación concurrente con hilos:

Diferencias entre Hilos y Procesos.

Aplicación de mecanismos de exclusión mutua (Bloqueos/Monitores).

Identificación y protección de secciones críticas.

Prevención de condiciones de carrera (Race Conditions).

Acceso concurrente seguro a ficheros.

🏗️ Arquitectura del Sistema

┌─────────────────────────────────────────────────┐
│               CLASE COCINA (Principal)          │
│    - Contiene la lista de pedidos (Recurso)     │
│    - Gestiona el Bloqueo (Lock / Monitor)       │
│    - Lanza y coordina los hilos 'Cocinero'      │
└─────────────┬──────────────────┬────────────────┘
              │                  │
      ┌───────▼───────┐    ┌─────▼─────┐
      │ LISTA PEDIDOS │    │  BLOQUEO  │
      │ (Compartida)  │    │  (Lock)   │
      └───────▲───────┘    └─────▲─────┘
              │                  │
              └─────────┬────────┴─────────────┐
                        │(Acceso Sincronizado) │
              ┌─────────▼─────────┬──────────▼─────────┐
              │                   │                    │
         ┌───────────┐        ┌──────────┐        ┌───────────┐
         │ Cocinero-1│        │ Cocinero-│        │ Cocinero-3│
         │  (Hilo)   │        │  (Hilo)  │        │  (Hilo)   │
         └─────┬─────┘        └───┬──────┘        └───┬───────┘
               │                  │                   │
               └───────────┬──────┴───────────┬───────┘
                           │ (Acceso Sincronizado)
                       ┌───▼───┐
                       │ LOG   │
                       │.txt   │
                       └───────┘


📁 Estructura del Proyecto (Python)

PSP-DAM-ACTEVA03B/
├── 📂 Java/
│   ├── Cocina.java             # Clase principal, gestiona hilos y lock
│   ├── Cocinero.java           # Clase Hilo (Thread/Runnable)
│   ├── Pedido.java             # Clase para datos del pedido
│   └── Main.java               # Punto de entrada
│
├── 📂 Python/
│   ├── main.py                 # Punto de entrada, crea pedidos
│   ├── cocina.py               # Clase principal, gestiona hilos y Lock
│   ├── cocinero.py             # Clase Hilo (threading.Thread)
│   └── pedido.py               # Clase para datos del pedido
│
└── README.md                   # Este archivo


🚀 Implementaciones

☕ Implementación en Java

Características Técnicas

Hilos: Usa Thread o implementa Runnable.

Sincronización: Usa la palabra clave synchronized (monitor) en los métodos que acceden a la lista de pedidos y al log.

Sección Crítica: Métodos tomarPedido() y registrarPedido().

Clases Principales

Clase

Responsabilidad

Cocina

Gestiona la lista, el lock, y el ciclo de vida de los hilos.

Cocinero

Hilo que toma un pedido, lo "prepara" (sleep) y lo registra.

Pedido

Objeto simple para almacenar datos del pedido.

Main

Punto de entrada. Crea la Cocina y los Pedidos.

Algoritmo de Sincronización (Java)

// Método sincronizado para tomar pedido
public synchronized Pedido tomarPedido() {
    if (this.pedidos.size() > 0) {
        return this.pedidos.remove(0);
    }
    return null; // No hay más pedidos
}

// Método sincronizado para escribir en el log
public synchronized void registrarPedido(String nombreCocinero, Pedido pedido) {
    // ... lógica para escribir en log_pedidos.txt
}


🐍 Implementación en Python

Características Técnicas

Hilos: Usa threading.Thread.

Sincronización: Usa un objeto threading.Lock() explícito.

Sección Crítica: Se protege usando el gestor de contexto with self.lock:.

Clases Principales

Clase/Módulo

Responsabilidad

cocina.py

Gestiona la lista, el Lock, y el ciclo de vida de los hilos.

cocinero.py

Hilo que toma un pedido, lo "prepara" (sleep) y lo registra.

pedido.py

Objeto simple para almacenar datos del pedido.

main.py

Punto de entrada. Crea la Cocina y los Pedidos.

Ejecución

# Ejecutar la simulación
cd Python
python main.py


Algoritmo de Sincronización (Python)

# Método sincronizado para tomar pedido
def tomar_pedido(self):
    with self.lock:
        if len(self.pedidos) > 0:
            return self.pedidos.pop(0)
        else:
            return None # No hay más pedidos

# Método sincronizado para escribir en el log
def registrar_pedido(self, nombre_cocinero, pedido):
    with self.lock:
        # ... lógica para escribir en log_pedidos.txt


🔄 Flujo de Ejecución

Inicialización: main.py crea una instancia de Cocina.

Creación de Pedidos: main.py crea entre 6 y 10 Pedidos y los añade a la Cocina.

Inicio Servicio: Se llama a cocina.iniciar_servicio(3), que crea y lanza 3 hilos Cocinero.

Competencia: Los 3 hilos Cocinero compiten para adquirir el Lock y entrar al método tomar_pedido().

Procesamiento:

Un cocinero adquiere el Lock, toma un pedido (ej. Pedido #1) y libera el Lock.

El cocinero simula la preparación (time.sleep(2)) fuera de la sección crítica, permitiendo a otros cocineros tomar más pedidos (ej. Pedido #2, Pedido #3).

Registro: Al terminar de preparar, el cocinero compite de nuevo por el Lock para entrar a registrar_pedido() y escribir en log_pedidos.txt.

Finalización: Los hilos terminan su bucle run() cuando tomar_pedido() devuelve None.

Join: El hilo principal (en cocina.py) espera (join()) a que los 3 hilos Cocinero terminen.

Se imprime "Todos los pedidos han sido procesados."

📊 Ejemplo de Salida (Python)

Pedidos en cola:
  - Pedido #1: Paella Valenciana
  - Pedido #2: Croquetas de Jamón
  - Pedido #3: Tortilla de Patatas
  - Pedido #4: Gazpacho Andaluz
  - Pedido #5: Pulpo a la Gallega
  - Pedido #6: Fabada Asturiana

=== INICIANDO SERVICIO DE COCINA CON 3 COCINEROS ===

[Cocinero-1] Preparando Pedido #1: Paella Valenciana...
[Cocinero-2] Preparando Pedido #2: Croquetas de Jamón...
[Cocinero-3] Preparando Pedido #3: Tortilla de Patatas...
[Cocinero-1] Pedido #1: Paella Valenciana completado ✓
[Cocinero-1] Preparando Pedido #4: Gazpacho Andaluz...
[Cocinero-2] Pedido #2: Croquetas de Jamón completado ✓
[Cocinero-2] Preparando Pedido #5: Pulpo a la Gallega...
[Cocinero-3] Pedido #3: Tortilla de Patatas completado ✓
[Cocinero-3] Preparando Pedido #6: Fabada Asturiana...
[Cocinero-1] Pedido #4: Gazpacho Andaluz completado ✓
[Cocinero-2] Pedido #5: Pulpo a la Gallega completado ✓
[Cocinero-3] Pedido #6: Fabada Asturiana completado ✓

=== SERVICIO FINALIZADO ===
Todos los pedidos han sido procesados.


🔑 Conceptos Clave

Exclusión Mutua

Solo un hilo puede estar en la sección crítica a la vez. Esto evita que dos cocineros intenten tomar el mismo pedido de la lista o escriban en el log simultáneamente, corrompiendo los datos.

Lock (Bloqueo) / Monitor

Es el mecanismo que implementa la exclusión mutua.

Python (threading.Lock): Un objeto explícito que se "adquiere" (acquire()) y "libera" (release(). El with lo hace automáticamente.

Java (synchronized): Un "monitor" implícito asociado a cada objeto. Cuando un hilo entra en un método synchronized, bloquea el monitor de ese objeto, impidiendo que otros hilos entren a cualquier otro método synchronized del mismo objeto.

Sección Crítica

Es el fragmento de código que accede al recurso compartido y debe ser protegido.

┌─────────────────────────┐
│   Región No Crítica     │
│  (Ej: time.sleep(2))    │
└────────────┬────────────┘
             │
┌────────────▼────────────┐
│ with self.lock:         │  ◄── Entrada a sección crítica
├─────────────────────────┤
│   SECCIÓN CRÍTICA       │
│  (Leer/modificar       │  ◄── Solo un hilo a la vez
│   self.pedidos o        │
│   escribir en log.txt)  │
├─────────────────────────┤
│ (Fin del 'with')        │  ◄── Salida de sección crítica
└────────────┬────────────┘
             │
┌────────────▼────────────┐
│   Región No Crítica     │
└─────────────────────────┘


📚 Conceptos Teóricos Aplicados

1. Hilos vs Procesos

Característica

Proceso (Usado en ACTEVA02)

Hilo (Usado en ESTA Actividad)

Memoria

Espacio de memoria propio y aislado.

Comparten el mismo espacio de memoria del proceso padre.

Creación

Más costosa (lenta).

Más ligera (rápida).

Comunicación

Difícil (Requiere IPC: tuberías, sockets, semáforos...).

Fácil (variables compartidas, locks, monitores...).

Aislamiento

Alto (un proceso no "rompe" a otro).

Bajo (un hilo puede corromper datos de otro).

Este proyecto usa HILOS porque todos los cocineros son parte de la misma aplicación (la Cocina) y necesitan acceder al mismo recurso (la lista de pedidos) de forma rápida.

2. Problemas de Concurrencia (Sin Lock)

Sin Lock (❌ Incorrecto)

[Cocinero-1] Lee que hay 1 pedido (índice 0).
[Cocinero-2] Lee que hay 1 pedido (índice 0).  <-- CONDICIÓN DE CARRERA
[Cocinero-1] Toma el pedido en índice 0.
[Cocinero-2] Intenta tomar el pedido en índice 0... ¡pero ya no existe! <-- ERROR (IndexError)


Con Lock (✅ Correcto)

[Cocinero-1] acquire() -> Éxito. Entra a la sección crítica.
[Cocinero-2] acquire() -> BLOQUEADO. Espera.
[Cocinero-1] Toma el pedido en índice 0. La lista queda vacía.
[Cocinero-1] release() -> Libera el lock.
[Cocinero-2] acquire() -> Éxito. Entra a la sección crítica.
[Cocinero-2] Comprueba la lista. Está vacía.
[Cocinero-2] Devuelve None y termina.
[Cocinero-2] release() -> Libera el lock.


🛠️ Requisitos

Para Java

JDK: Java 11 o superior.

IDE: IntelliJ IDEA, Eclipse o VSCode con Extension Pack for Java.

Para Python

Python: 3.6 o superior.

Módulos: threading, time, random (incluidos en la biblioteca estándar).

📖 Referencias

Java synchronized Methods

Python threading — Thread-based parallelism

Python Lock Objects

👨‍💻 Autor

(Tu nombre aquí, he copiado el del ejemplo)
Esteban Garcés Pérez

🎓 Alumno de 2º DAM

📧 Contacto: GitHub

📂 Repositorio: (Añade tu repo aquí)

📄 Licencia

Este proyecto es material académico para la asignatura de Programación de Servicios y Procesos (PSP) del ciclo de Desarrollo de Aplicaciones Multiplataforma (DAM).

🎓 Asignatura

Programación de Servicios y Procesos
Ciclo Formativo de Grado Superior - Desarrollo de Aplicaciones Multiplataforma (DAM)
Curso 2024/2025

<div align="center">

⭐ Si este proyecto te ha ayudado a entender la programación concurrente con hilos, considera darle una estrella ⭐

</div>