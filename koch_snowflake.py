#got to find other recursive way

import fractal_mountain as fm

def drawSnowflake(turtle, length, angle, rDepth):
    for i in range(3):
        fm.drawMountain(turtle, rDepth, angle, length)
        turtle.right(120)
