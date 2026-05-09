"""
Serpiente, juego clásico de arcade.

Ejercicios

1. ¿Cómo haces la serpiente más rápida o más lenta?
2. ¿Cómo haces que la serpiente atraviese los bordes?
3. ¿Cómo moverías la comida?
4. Cambia la serpiente para responder a clics del mouse.
"""

from random import randrange
from turtle import (
    setup,
    hideturtle,
    tracer,
    listen,
    onkey,
    ontimer,
    update,
    clear,
    done,
)

from freegames import square, vector

# Posición de la comida
comida = vector(0, 0)

# Cuerpo inicial de la serpiente
serpiente = [vector(10, 0)]

# Dirección inicial
direccion = vector(0, -10)


def cambiar_direccion(x, y):
    """Cambia la dirección de la serpiente."""
    direccion.x = x
    direccion.y = y


def dentro_limites(cabeza):
    """Verifica si la cabeza está dentro de los límites."""
    return -200 < cabeza.x < 190 and -200 < cabeza.y < 190


def mover():
    """Mueve la serpiente un segmento hacia adelante."""

    cabeza = serpiente[-1].copy()
    cabeza.move(direccion)

    # Verifica colisiones
    if not dentro_limites(cabeza) or cabeza in serpiente:
        square(cabeza.x, cabeza.y, 9, 'red')
        update()
        return

    serpiente.append(cabeza)

    # Verifica si comió la comida
    if cabeza == comida:
        print('Puntaje:', len(serpiente))

        comida.x = randrange(-15, 15) * 10
        comida.y = randrange(-15, 15) * 10
    else:
        serpiente.pop(0)

    clear()

    # Dibuja la serpiente
    for parte in serpiente:
        square(parte.x, parte.y, 9, 'blue')

    # Dibuja la comida
    square(comida.x, comida.y, 9, 'yellow')

    update()

    # Velocidad del juego
    ontimer(mover, 70)


# Configuración de la ventana
setup(600, 600, 370, 0)

hideturtle()
tracer(False)
listen()

# Controles del teclado
onkey(lambda: cambiar_direccion(10, 0), 'Right')
onkey(lambda: cambiar_direccion(-10, 0), 'Left')
onkey(lambda: cambiar_direccion(0, 10), 'Up')
onkey(lambda: cambiar_direccion(0, -10), 'Down')

# Inicia el juego
mover()

done()
