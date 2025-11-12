"""
Módulo que define la clase Cocina.
Gestiona la lista de pedidos, el log y los hilos (Cocineros).
"""
import threading
from datetime import datetime

# Importamos las clases que necesita gestionar
from pedido import Pedido
from cocinero import Cocinero

class Cocina:
    """
    Clase principal que gestiona la lista de pedidos (recurso compartido)
    y los hilos cocineros.
    """
    
    def __init__(self):
        self.pedidos = []
        self.lock = threading.Lock() # Lock para sincronizar acceso a pedidos y log
        self.archivo_log = "log_pedidos.txt"
        
        # Inicializar el archivo de log
        try:
            with open(self.archivo_log, 'w', encoding='utf-8') as f:
                f.write("=== LOG DE PEDIDOS ===\n")
                f.write(f"Inicio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        except IOError as e:
            print(f"Error al inicializar el log: {e}")
    
    def agregar_pedido(self, pedido: Pedido):
        """
        Agregar un pedido a la lista.
        En esta simulación, solo se llama antes de iniciar los hilos,
        por lo que no requiere lock.
        """
        self.pedidos.append(pedido)
    
    def tomar_pedido(self):
        """
        Método sincronizado para que un cocinero tome un pedido.
        Retorna el siguiente pedido (Pedido) o None si la lista está vacía.
        """
        with self.lock:
            if len(self.pedidos) > 0:
                # pop(0) toma el primer pedido de la lista (FIFO)
                return self.pedidos.pop(0)
            else:
                # No hay más pedidos
                return None
    
    def registrar_pedido(self, nombre_cocinero, pedido: Pedido):
        """
        Método sincronizado para registrar un pedido completado en el archivo log.
        Usa el mismo lock para asegurar la atomicidad en la escritura del fichero.
        """
        with self.lock:
            try:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                mensaje = f"[{timestamp}] {nombre_cocinero} completó {pedido}\n"
                
                with open(self.archivo_log, 'a', encoding='utf-8') as f:
                    f.write(mensaje)
            except IOError as e:
                print(f"Error al escribir en el log: {e}")
    
    def iniciar_servicio(self, num_cocineros):
        """
        Crear y lanzar los hilos de los cocineros.
        Esperar (join) a que todos terminen.
        """
        print(f"=== INICIANDO SERVICIO DE COCINA CON {num_cocineros} COCINEROS ===\n")
        
        # Crear los cocineros
        cocineros = []
        for i in range(num_cocineros):
            nombre = f"Cocinero-{i+1}"
            # Pasamos la instancia actual de Cocina (self) a cada cocinero
            cocinero = Cocinero(nombre, self)
            cocineros.append(cocinero)
        
        # Iniciar todos los hilos
        for cocinero in cocineros:
            cocinero.start()
        
        # Esperar a que todos los cocineros terminen
        for cocinero in cocineros:
            cocinero.join()
        
        # Finalizar el log
        try:
            with open(self.archivo_log, 'a', encoding='utf-8') as f:
                f.write(f"\nFin: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        except IOError as e:
            print(f"Error al finalizar el log: {e}")
        
        print("\n=== SERVICIO FINALIZADO ===")
        print("Todos los pedidos han sido procesados.")