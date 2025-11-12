"""
Módulo que define la clase Cocinero (Thread).
"""
import threading
import time

# Para evitar importaciones circulares y mantenerlo simple,
# no importamos las clases Cocina o Pedido, ya que las
# instancias se reciben en el constructor y métodos.

class Cocinero(threading.Thread):
    """Hilo que representa un cocinero procesando pedidos"""
    
    def __init__(self, nombre, cocina):
        """
        Inicializa el hilo del cocinero.
        :param nombre: Nombre del cocinero (ej. "Cocinero-1")
        :param cocina: Instancia de la clase Cocina (recurso compartido)
        """
        super().__init__()
        self.nombre = nombre
        self.cocina = cocina
    
    def run(self):
        """
        Método principal del hilo.
        Procesa pedidos mientras haya disponibles en la cocina.
        """
        while True:
            # Pide un pedido a la cocina (método sincronizado)
            # El objeto devuelto es de tipo Pedido o None
            pedido = self.cocina.tomar_pedido()
            
            # Si no hay más pedidos, el hilo termina
            if pedido is None:
                break
            
            # Simular la preparación del pedido (1-3 segundos)
            # Mantenemos el valor fijo de 2 segundos de tu código original
            tiempo_preparacion = 2 
            print(f"[{self.nombre}] Preparando {pedido}...")
            time.sleep(tiempo_preparacion)
            
            # Registrar el pedido completado (método sincronizado)
            self.cocina.registrar_pedido(self.nombre, pedido)
            
            print(f"[{self.nombre}] {pedido} completado")