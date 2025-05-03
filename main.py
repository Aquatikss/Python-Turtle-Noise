import turtle
import math
import random

def setup_screen():
    window = turtle.Screen()
    window.setup(width=1.0, height=1.0)
    window.tracer(0)
    return window

def setup_pen():
    pen = turtle.Turtle()
    pen.shape("square")
    pen.shapesize(0.5, 0.5)
    pen.penup()
    pen.hideturtle()
    pen.speed(0)  # Fastest speed
    return pen

def get_grid_dimensions(window, pen):
    pen_width = pen.shapesize()[0] * 20
    pen_height = pen.shapesize()[1] * 20
    x_loops = math.floor(window.window_width() / pen_width)
    y_loops = math.floor(window.window_height() / pen_height)
    return pen_width, pen_height, x_loops, y_loops

def move_to_start(pen, window, pen_width, pen_height):
    start_x = (0 - (window.window_width() / 2) + pen_width/2)
    start_y = ((0 + (window.window_height() / 2)) - pen_height/2)
    pen.setpos(start_x, start_y)
    pen.showturtle()

def main():
    window = setup_screen()
    pen = setup_pen()
    
    pen_width, pen_height, x_loops, y_loops = get_grid_dimensions(window, pen)
    move_to_start(pen, window, pen_width, pen_height)

    for i in range(x_loops):
        for j in range(y_loops):
            x = (0 - window.window_width()/2 + pen_width/2) + (i * pen_width)
            y = (window.window_height()/2 - pen_height/2) - (j * pen_height)
            pen.goto(x, y)
            if random.random() > 0.5:
                pen.stamp()

    window.update()
    turtle.done()

if __name__ == "__main__":
    main()