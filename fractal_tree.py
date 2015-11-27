import turtle
import random

def tree(branchLen,t, thickness, colorN):
    if branchLen > 5:
        color = ["green", "red", "yellow", "blue"]
        if colorN >= len(color):
            colorN = len(color) -1
        t.color(color[colorN])
        angle = random.randrange(15, 45)
        subBranch = random.randrange(12, 16)
        t.pensize(thickness)
        t.forward(branchLen)
        t.right(angle)
        tree(branchLen-subBranch,t, thickness-2, colorN-1)
        t.left(2*angle)
        tree(branchLen-subBranch,t, thickness-2, colorN-1)
        t.right(angle)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t, 9, 5)
    myWin.exitonclick()

main()
