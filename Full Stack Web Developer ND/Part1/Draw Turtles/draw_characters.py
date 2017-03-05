import turtle

def draw_K(some_turtle):
	some_turtle.forward(100)
	some_turtle.left(135)
	some_turtle.forward(136)
	some_turtle.backward(136)
	some_turtle.right(90)
	some_turtle.forward(136)
	some_turtle.backward(136)
	some_turtle.right(45)
	some_turtle.forward(100)

def draw_C(some_turtle):
	some_turtle.forward(100)
	some_turtle.left(90)
	some_turtle.forward(200)
	some_turtle.left(90)
	some_turtle.forward(100)

def draw_characters():
	window = turtle.Screen()
	window.bgcolor("blue")

	# Create the turtle Flower - Draws a pallelogram
	characters = turtle.Turtle()
	characters.shape("turtle")
	characters.color("yellow")
	characters.speed(2)
	characters.right(90)
	draw_K(characters)

	characters.color("blue")
	characters.left(90)
	characters.forward(210)
	characters.left(90)
	characters.forward(200)
	characters.right(90)
	characters.forward(100)
	characters.right(180)
	characters.color("yellow")
	draw_C(characters)

	window.exitonclick()

draw_characters()