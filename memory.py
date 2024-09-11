"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

"Cambiamos los numeros por letras. Autor: Juan Daniel"
car = path('car.gif')
tiles = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')[:18] * 2
state = {'mark': None}
hide = [True] * 36


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    "Ajustamos la cuadricula. Autor: Juan Daniel"
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(70)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    "Cambiamos cuadricula a 6*6. Autor: Juan Daniel"
    return int((x + 210) // 70 + ((y + 210) // 70) * 6)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 6) * 70 - 210, (count // 6) * 70 - 210

"""Creamos una variable que servira de contador para cada tap
que se pulse. Javier J.P."""
taps = 0

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    """Indicamos que la variable taps que se va a modificar dentro de
    la función,  es la misma variable que fue declarada fuera de"""
    """Autor: Javier J.P."""
    global taps
    spot = index(x, y)
    mark = state['mark']
    """Incrementar el contador de taps. Autor: Javier J.P."""
    """Imprimimos la cuenta. Autor: Javier J.P."""

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        if hide[spot]:
            taps += 1
            print("Taps:", taps)

    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(36):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        """Ajusta la posicion de los numeros de un digito.
        Autor: Alberto"""
        goto(x + 35, y + 15)
        color('black')
        """Align para que los  numeros se centren"""
        write(tiles[mark], font=('Arial', 30, 'normal'), align='center')

    """Detecta si todos los cuadros han sido abiertos. Autor: Alberto"""
    if all(not hidden for hidden in hide):
        goto(0, -110)
        color('blue')
        write(f"Congrats! Al tiles revealed\nin {taps} taps", align='center',
        font=('Arial', 20, 'bold'))


    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
