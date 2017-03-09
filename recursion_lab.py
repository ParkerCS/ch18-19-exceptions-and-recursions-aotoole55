'''
Using the turtle library, create a fractal pattern.
You may use heading/forward/backward or goto and fill commands to draw
your fractal.  Ideas for your fractal pattern might include
examples from the chapter.  You can find many fractal examples online,
but please make your fractal unique.  Experiment with the variables
to change the appearance and behavior.

Give your fractal a depth of at least 5.  Ensure the fractal is contained on the screen (at whatever size you set it).  Have fun.
(35pts)
'''

import turtle

color_list = ['red', 'yellow', 'orange', 'blue']

def circle(x, y, radius, iteration):
    my_turtle = turtle.Turtle()
    my_turtle.speed(0)
    my_turtle.showturtle()
    my_screen = turtle.Screen()

    #Color
    my_turtle.pencolor(color_list[iteration % (len(color_list[0:4]))])
    my_screen.bgcolor('purple')

    #Drawing
    my_turtle.penup()
    my_turtle.setposition(x, y)
    my_turtle.pendown()
    my_turtle.circle(radius)

    #Recursion
    if radius <= 200 and radius > 1:
        radius = radius * 0.75
        circle(25, -200, radius, iteration + 1)


    my_screen.exitonclick()

circle(25, -200, 200, 0)



