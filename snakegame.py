import turtle
import time
import random

delay = 0.1

# Screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(100, 100)

segments = []

# Score
score = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center",
          font=("Arial", 20, "bold"))

# Movement Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    x = head.xcor()
    y = head.ycor()

    if head.direction == "up":
        head.sety(y + 20)

    if head.direction == "down":
        head.sety(y - 20)

    if head.direction == "left":
        head.setx(x - 20)

    if head.direction == "right":
        head.setx(x + 20)

# Keyboard
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main Loop
while True:
    wn.update()

    # Border Collision
    if (head.xcor() > 290 or head.xcor() < -290 or
        head.ycor() > 290 or head.ycor() < -290):

        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

        score = 0
        delay = 0.1

        pen.clear()
        pen.write(f"Score: {score}", align="center",
                  font=("Arial", 20, "bold"))

    # Food Collision
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        delay -= 0.002

        pen.clear()
        pen.write(f"Score: {score}", align="center",
                  font=("Arial", 20, "bold"))

    # Move Body
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Self Collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"

            for s in segments:
                s.goto(1000, 1000)

            segments.clear()

            score = 0
            delay = 0.1

            pen.clear()
            pen.write(f"Score: {score}", align="center",
                      font=("Arial", 20, "bold"))

    time.sleep(delay)

wn.mainloop()