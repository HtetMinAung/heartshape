import turtle as t

# Create a Turtle object
heart = t.Turtle()

# Set the fill color and speed
heart.fillcolor("red")
heart.speed(1)

# Move to the starting position
heart.penup()
heart.goto(0, -200)
heart.pendown()

# Draw the heart shape
heart.begin_fill()
heart.left(140)
heart.forward(224)
for _ in range(200):
    heart.right(1)
    heart.forward(2)
heart.left(120)
for _ in range(200):
    heart.right(1)
    heart.forward(2)
heart.forward(224)
heart.end_fill()

# Hide the Turtle
heart.hideturtle()

# Keep the window open
t.done()
