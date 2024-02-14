import turtle
screen = turtle.Screen()
screen.bgcolor("white")

heart = turtle.Turtle()
heart.shape("turtle")
heart.color("red")
heart.speed(5)

heart.penup()

for _ in range(1):
    heart.begin_fill()
    heart.fillcolor("red")
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

    # Capture the pixel values and create an image at each step
    stamp_id = heart.stamp()
    image_data = screen.getcanvas().postscript(colormode="color")
    heart.clearstamp(stamp_id)

    # Create a new turtle to display the image at each step
    image_turtle = turtle.Turtle()
    image_turtle.shape("square")  # Change shape to square
    image_turtle.penup()
    image_turtle.goto(heart.xcor(), heart.ycor())

    # Update the screen
    screen.update()

# Keep the window open
screen.mainloop()
