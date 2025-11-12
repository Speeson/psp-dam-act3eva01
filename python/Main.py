"""
Punto de entrada principal para la simulación de la cocina.

Este script importa las clases necesarias, crea los pedidos
y la cocina, e inicia el servicio.
"""

import random
from cocina import Cocina
from pedido import Pedido

# Lista de platos (constante)
PLATOS = [
    "Tortilla de Patatas", "Gazpacho Andaluz", "Croquetas de Jamón",
    "Paella Valenciana", "Pulpo a la Gallega", "Fabada Asturiana",
    "Cochinillo Segoviano", "Jamón Ibérico", "Crema Catalana",
    "Patatas Bravas", "Gambas al Ajillo", "Salmorejo Cordobés",
    "Chuletón de Buey", "Marmitako", "Pisto Manchego",
    "Bacalao al Pil Pil", "Callos a la Madrileña", "Migas Extremeñas",
    "Rabo de Toro", "Churros con Chocolate"
]

def main():
    """Función principal del programa"""
    
    # 1. Crear la cocina
    cocina = Cocina()
    
    # 2. Definir cuántos pedidos (mínimo 6 según requisitos)
    num_pedidos = random.randint(6, 10)
    
    print("Pedidos en cola:")
    
    # 3. Crear y agregar los pedidos a la cocina
    for i in range(num_pedidos):
        plato_aleatorio = random.choice(PLATOS)
        pedido = Pedido(i + 1, plato_aleatorio)
        cocina.agregar_pedido(pedido)
        print(f"  - {pedido}")
    
    print()
    
    # 4. Definir cuántos cocineros (mínimo 3 según requisitos)
    num_cocineros = 3
    
    # 5. Iniciar el servicio
    # Esto creará los hilos, los iniciará y esperará a que terminen
    cocina.iniciar_servicio(num_cocineros)


if __name__ == "__main__":
    main()