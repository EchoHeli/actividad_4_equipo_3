"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Cambia la dirección de la serpiente."""
    aim.x = x
    aim.y = y


def inside(head):
    """Verifica si la cabeza está dentro de los límites."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Mueve la serpiente un segmento hacia adelante."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        # Cambia el color al perder
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        # Se cambió el color de la serpiente a azul
        square(body.x, body.y, 9, 'blue')

    # Se cambió el color de la comida a amarillo
    square(food.x, food.y, 9, 'yellow')

    update()

    # Se aumentó ligeramente la velocidad del juego
    ontimer(move, 70)


# Se aumentó el tamaño de la ventana
setup(600, 600, 370, 0)

hideturtle()
tracer(False)
listen()

onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

move()
done()
