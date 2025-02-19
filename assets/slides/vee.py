# Some handy imports, don't worry about these
# This file needs to be run locally on you machine,
# it displays graphical output.
### Docs: https://docs.python.org/3.8/library/turtle.html

# Run with python3 -i vee.py

## Code for Drawing Vee
## Everything below here is not something you need to study, but does illustrate recursion (with graphics)

# A new window opens, click in there once to make sure it recieves keyboard shortcuts.
# Press SPACE to redraw things
# Press UP/DOWN to add or remove "VEE" from the list of functions
# Press R to clear the screen (RESET)
# Press S to toggle whether to SHOW functions.
# Press Q to exist (QUIT) the program.

from turtle import *
from math import sin, cos, tan, pi, sqrt
from random import seed, choice # pick something random
from os import name

# Stupid simple state tracking
SHOW_FUNCTION_LIST = True

#### HOFs and Recusion Vee Demo ######

def start_postion():
  return (0, (window_height() / -2) + 30)

def reset():
    start = start_postion()
    pencolor('black')
    pensize(1)
    speed("fastest")
    setheading(90) # 90 degrees, facing "north"
    penup()
    goto(start[0], start[1])
    clear()
    display_functions()
    goto(start[0], start[1])

def triangle():
    """Draw a filled triangle with a side length of 12."""
    n = 3
    fillcolor(choice(colors))
    begin_fill()
    while n > 0:
        forward(12) # size 10
        left(120)
        n -= 1
    end_fill()

def dot():
    """Draw a filled circle with radius 6."""
    fillcolor(choice(colors))
    begin_fill()
    circle(6) # this is a built in turtle function, size 8 a little smaller
    end_fill()

def square():
    """Draw a square of length 12"""
    n = 4
    fillcolor(choice(colors))
    begin_fill()
    while n > 0:
        forward(12)
        left(90)
        n -= 1
    end_fill()

def draw_polygon(sides):
    "Return a generic draw a polygon function like the ones above"
    def draw_shape():
        n = sides
        fillcolor(choice(colors))
        begin_fill()
        while n > 0:
            forward(12)
            left(sides / 360)
            n -= 1
        end_fill()
    return draw_shape

# Some colors, `choice(colors)` returns a random color.
colors = [
    '#003262', # Hex code color "Berkeley Blue"
    '#FDB515' # Hex code for "California Gold"
]

# A list of HOFs
draw_functions = [
    triangle,
    dot,
    square
    # vee() will get added here.
]

def vee():
    """Draw a 'v' shape, with random shapes at the end of each leg."""
    angle = 15
    size = 45
    pendown()
    left(angle)
    forward(size)
    shape = choice(draw_functions) # A random shape
    print('Shape: ', shape)
    shape() # Call a HOF, with a size input
    backward(size)
    right(angle * 2) # turn where we strated, then to the right again.
    forward(size)
    shape = choice(draw_functions) # () # We can also stack parens together
    print('Shape: ', shape)
    shape()
    backward(size)
    left(angle)

def add_vee():
    if len(draw_functions) == 3:
        draw_functions.append(vee)
        draw_functions.append(vee)
    display_functions()

def fractal(level, size=200):
    """Draw a 'v' shape, with random shapes at the end of each leg."""
    if level == 0:
        shape = choice(draw_functions) # A random shape
        shape() # Call a HOF, with a size input
        return
    angle = 30
    pendown()
    left(angle)
    forward(size)
    fractal(level - 1, size * .75)
    backward(size)
    right(angle * 2) # turn where we strated, then to the right again.
    forward(size)
    fractal(level - 1, size * .75)
    backward(size) # return to start.
    left(angle)

def draw_fractal(levels=5, size=200):
    reset()
    remove_vee()
    fractal(levels, size)

def remove_vee():
    if len(draw_functions) == 5:
        draw_functions.pop() # remove the last item, twice.
        draw_functions.pop()
    display_functions()

def toggle_display_functions():
    global SHOW_FUNCTION_LIST
    SHOW_FUNCTION_LIST = not SHOW_FUNCTION_LIST

def top_left():
  """An x:, y: dict of the top-left corner of the window."""
  return { 'x': window_width() / -2, 'y': window_height() / 2}

def display_functions():
    global SHOW_FUNCTION_LIST
    if not SHOW_FUNCTION_LIST:
        return
    clear()
    pencolor('black')
    penup() # pen up to not show movement. Doesn't affect `write`.
    corner = top_left()
    goto(corner['x'], corner['y'])
    write('VEE LIST:', font=('Courier', 22, 'normal'))
    for func in draw_functions:
        goto(corner['x'], ycor() - 22)
        write(func, font=('Courier', 22, 'normal'))
    goto(start_postion()[0], start_postion()[1])

def exit_vee():
    bye()

def draw_new():
    reset()
    vee()

# simple interactivity
onkey(draw_new, 'space')
onkey(reset, 'r')
onkey(draw_fractal, 'f')
onkey(add_vee, 'Up')
onkey(remove_vee, 'Down')
onkey(exit_vee, 'q')
onkey(toggle_display_functions, 's')
listen()

################ Do the work! This runs the file when started.
if __name__ == '__main__':
    print(f"Seed: {seed()}")
    reset()
    vee()
    mainloop()

######################## Some extra stuff for later

##### More HOFs
def vee_hof():
    """Draw a 'v' shape, with random shapes at the end of each leg."""
    angle = 15
    size = 45
    def draw_leg():
        forward(size)
        choice(draw_functions)() # Call a HOF
        backward(size)

    left(angle)
    draw_leg()
    right(angle) # face the direction where we strated, then to the right.
    right(angle)
    draw_leg()
    left(angle)
