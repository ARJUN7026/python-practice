import turtle
import math

screen = turtle.Screen()
screen.setup(900, 500)
screen.title("Bike Animation")
screen.bgcolor("skyblue")
screen.tracer(0)

bike = turtle.Turtle()
bike.hideturtle()
bike.speed(0)

road = turtle.Turtle()
road.hideturtle()
road.speed(0)


def draw_line(pen, x1, y1, x2, y2, color, width):
    pen.penup()
    pen.goto(x1, y1)
    pen.color(color)
    pen.pensize(width)
    pen.pendown()
    pen.goto(x2, y2)
    pen.penup()


def draw_wheel(cx, cy, rotation):
    radius = 45

    # Spokes
    for i in range(8):
        angle = math.radians(rotation + i * 45)
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        draw_line(bike, cx, cy, x, y, "gray", 2)

    # Outer wheel
    bike.penup()
    bike.goto(cx, cy - radius)
    bike.setheading(0)
    bike.color("black")
    bike.pensize(4)
    bike.pendown()
    bike.circle(radius)
    bike.penup()

    # Hub
    bike.goto(cx, cy)
    bike.dot(10, "black")


frame = 0
bike_x = -400


def animate():
    global frame, bike_x

    bike.clear()
    road.clear()

    # Moving road dashes
    draw_line(road, -450, -165, 450, -165, "dim gray", 4)
    for i in range(10):
        dash_x = i * 100 - (frame * 4 % 100) - 450
        draw_line(road, dash_x, -165, dash_x + 45, -165, "white", 3)

    rear_x = bike_x - 110
    front_x = bike_x + 110
    wheel_y = -115
    crank_x = bike_x
    crank_y = wheel_y

    # Wheels
    draw_wheel(rear_x, wheel_y, -frame * 8)
    draw_wheel(front_x, wheel_y, -frame * 8)

    # Bike frame
    seat_x, seat_y = bike_x - 45, -25
    handle_x, handle_y = bike_x + 45, -40

    draw_line(bike, rear_x, wheel_y, seat_x, seat_y, "teal", 6)
    draw_line(bike, seat_x, seat_y, crank_x, crank_y, "teal", 6)
    draw_line(bike, crank_x, crank_y, rear_x, wheel_y, "teal", 6)
    draw_line(bike, seat_x, seat_y, handle_x, handle_y, "teal", 6)
    draw_line(bike, handle_x, handle_y, crank_x, crank_y, "teal", 6)
    draw_line(bike, handle_x, handle_y, front_x, wheel_y, "teal", 6)

    # Seat and handlebar
    draw_line(bike, seat_x, seat_y, seat_x - 10, seat_y + 15, "black", 5)
    draw_line(bike, seat_x - 25, seat_y + 15, seat_x + 2, seat_y + 15, "black", 6)
    draw_line(bike, handle_x, handle_y, handle_x + 5, handle_y + 20, "black", 5)
    draw_line(bike, handle_x - 10, handle_y + 20, handle_x + 25, handle_y + 20, "black", 5)

    # Turning pedals
    pedal_angle = math.radians(frame * 10)
    pedal_radius = 18
    for direction in (1, -1):
        px = crank_x + direction * pedal_radius * math.cos(pedal_angle)
        py = crank_y + direction * pedal_radius * math.sin(pedal_angle)
        draw_line(bike, px - 8, py, px + 8, py, "black", 4)

    # Move bike across the screen, then start again
    bike_x += 3
    if bike_x > 450:
        bike_x = -450

    frame += 1
    screen.update()
    screen.ontimer(animate, 30)


animate()
screen.mainloop()