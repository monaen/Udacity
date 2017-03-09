import turtle

def draw_parallelogram(some_turtle):
	for i in range(1, 3):
		some_turtle.forward(100)
		some_turtle.right(45)
		some_turtle.forward(100)
		some_turtle.right(135)


def draw_flower():
	window = turtle.Screen()
	window.bgcolor("red")

	# Create the turtle Flower - Draws a pallelogram
	flower = turtle.Turtle()
	flower.shape("turtle")
	flower.color("blue")
	flower.speed(2)
	for i in range(1, 37):
		flower.right(10)
		draw_parallelogram(flower)

	flower.right(90)
	flower.forward(360)

	window.exitonclick()

draw_flower()