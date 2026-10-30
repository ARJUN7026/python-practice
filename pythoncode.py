import turtle

screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(3)

def draw_square(size, color):
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(4):
        pen.forward(size)
        pen.left(90)
    pen.end_fill()

# Draw the large square, then a smaller white square to look like a hole
draw_square(200, "blue")

pen.penup()
pen.goto(60, 60)
pen.pendown()
draw_square(80, "white")

turtle.done()