#import turtle


def drawMountain(turtle, degree, angle, length):
    if degree <= 0:
        turtle.forward(length/3)
    else:
        drawMountain(turtle, degree-1, angle, length/3)
        turtle.left(angle)
        drawMountain(turtle, degree-1, angle, length/3)
        turtle.left(180+angle)
        drawMountain(turtle, degree-1, angle, length/3)
        turtle.left(angle)
        drawMountain(turtle, degree-1, angle, length/3)

