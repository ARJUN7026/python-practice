import turtle

screen = turtle.Screen()
screen.setup(700, 400)
screen.bgcolor("#f4f4f4")
screen.title("A Pen")

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)


def polygon(points, fill, outline="black"):
    pen.penup()
    pen.goto(points[0])
    pen.pendown()
    pen.color(outline, fill)
    pen.begin_fill()
    for point in points[1:]:
        pen.goto(point)
    pen.goto(points[0])
    pen.end_fill()


def line(points, color="black", width=3):
    pen.color(color)
    pen.pensize(width)
    pen.penup()
    pen.goto(points[0])
    pen.pendown()
    for point in points[1:]:
        pen.goto(point)


# Pen barrel
polygon([(-160, -25), (90, -25), (90, 25), (-160, 25)], "#2878c8")

# Pen cap
polygon([(-190, -28), (-155, -28), (-155, 28), (-190, 28)], "#174d85")
line([(-180, 28), (-180, 48), (-155, 48)], "#174d85", 5)

# Nib
polygon([(90, -25), (150, 0), (90, 25)], "#d9d9d9")
line([(90, -25), (90, 25)], "#555555", 2)
line([(90, 0), (150, 0)], "#777777", 2)

# Barrel highlight
line([(-140, 10), (70, 10)], "#8fc8f5", 4)

pen.hideturtle()
screen.exitonclick()