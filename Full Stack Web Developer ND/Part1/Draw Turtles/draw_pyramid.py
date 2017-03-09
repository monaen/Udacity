import turtle

def draw_small_triangle(some_turtle):
	for i in range(1, 4):
		some_turtle.forward(50)
		some_turtle.left(120)
		

def draw_big_triangle(some_turtle):
	for i in range(1, 13):
		draw_small_triangle(some_turtle)
		some_turtle.forward(50)
		if i % 4 == 0:
	 		some_turtle.left(120)
	# some_turtle.forward(50)






def draw_pyramid():
	window = turtle.Screen()
	window.bgcolor("yellow")

	triangle = turtle.Turtle()
	triangle.shape("turtle")
	triangle.color("blue")
	triangle.speed(2)
	triangle.right(120)
	for i in range(1, 4):
		draw_big_triangle(triangle)
		triangle.forward(200)
		if i % 2 == 0:
			triangle.left(120)
			triangle.forward(200)



	window.exitonclick()

draw_pyramid()