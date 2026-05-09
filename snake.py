"""Snake, juego clasico de arcade.

Ejercicios

1. Como hacer que la serpiente sea mas rapida o mas lenta?
2. Como hacer que la serpiente atraviese los bordes?
3. Como mover la comida?
4. Cambiar la serpiente para que responda a clics del raton.
"""

# Importacion de modulos necesarios
from random import randrange  # Para generar posiciones aleatorias de la comida
from turtle import *  # Modulo grafico para dibujar en pantalla

# Funciones auxiliares de freegames: square dibuja cuadrados y vector maneja
# coordenadas en 2D
from freegames import square, vector

# Variables globales del juego
food = vector(0, 0)         # Posicion inicial de la comida en el centro
snake = [vector(10, 0)]     # Lista de segmentos que conforman la serpiente
aim = vector(0, -10)        # Direccion inicial de movimiento (hacia abajo)


def change(x, y):
    """Cambia la direccion de movimiento de la serpiente.

    Recibe los valores x e y que indican el nuevo desplazamiento por
    iteracion y los asigna al vector global aim.
    """
    aim.x = x
    aim.y = y


def inside(head):
    """Verifica si la cabeza de la serpiente esta dentro de los limites.

    Devuelve True si la posicion de la cabeza esta dentro del area de
    juego permitida, y False en caso contrario.
    """
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Mueve la serpiente un segmento hacia adelante.

    Calcula la nueva posicion de la cabeza, comprueba colisiones con los
    bordes o con el propio cuerpo, gestiona el consumo de comida y vuelve
    a programar la siguiente llamada para crear el ciclo de animacion.
    """
    # Se obtiene una copia de la cabeza actual y se desplaza segun aim
    head = snake[-1].copy()
    head.move(aim)

    # Si la cabeza sale del area o choca con el cuerpo, se pierde la partida
    if not inside(head) or head in snake:
        # Se dibuja un cuadrado rojo (cambiado a tamano 12) marcando el final
        square(head.x, head.y, 12, 'red')
        update()
        return

    # Se agrega la nueva cabeza al final de la lista de segmentos
    snake.append(head)

    # Si la cabeza coincide con la comida, la serpiente crece y se reubica
    # la comida en una posicion aleatoria
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        # Si no comio, se elimina el primer segmento para simular movimiento
        snake.pop(0)

    # Se limpia la pantalla antes de volver a dibujar
    clear()

    # Se dibuja cada segmento de la serpiente en color azul (cambio visu