"""
Módulo que define la clase Pedido.
"""

class Pedido:
    """Clase que representa un pedido con ID y nombre del plato"""
    
    def __init__(self, id_pedido, nombre_plato):
        self.id_pedido = id_pedido
        self.nombre_plato = nombre_plato
    
    def __str__(self):
        """Representación en cadena del pedido"""
        return f"Pedido #{self.id_pedido}: {self.nombre_plato}"