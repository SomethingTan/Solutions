import turtle  # this imports a library called "turtle". A library is (typically someone else's) python code, that you can use in your own program.

def demo():  # demonstration of basic turtle commands
    tom.speed(1)  # fastest: 10, slowest: 1
    for x in range(8):  # do the following for x = 0, 1, 2, 3, 4, 5, 6, 7
        tom.forward(50)  # move 50 pixels
        tom.left(45)  # turn 45 degrees left
        print(f'Tom is now at {tom.position()}, x-value: {tom.position()[0]=:.2f}, y-value: {tom.position()[1]=:.2f}')
    tom.penup()  # do not draw while moving from now on
    tom.forward(100)
    tom.pendown()  # draw while moving from now on
    tom.circle(50)  # draw a circle with radius 50
    tom.pencolor("red")  # draw in red
    tom.right(90)  # turn 90 degrees right
    tom.forward(120)
    tom.right(-90)  # turning -90 degrees right is the same as turning +90 degrees left
    tom.forward(120)
    tom.goto(-100, -200)  # move to coordinates -100, -200  (0, 0 is the middle of the screen)
    tom.home()  # return to the original position in the middle of the window
    tom.left()
    tom.right()

def circle(radius):
    tom.circle(radius)

def move_to(x,y):
    tom.penup()
    tom.goto(x,y)
    tom.pendown()

def square(length):
    for i in range(4):
        tom.forward(length)
        tom.right(90)

def triangle(length):
    for i in range(3):
        tom.forward(length)
        tom.left(120)

def coloured_triangle(length, colour):
    tom.pencolor(colour)
    for i in range(3):
        tom.forward(length)
        tom.left(120)

def many_squares(number_of_squares,size,distance):
    for i in range(number_of_squares):
        for j in range(4):
            tom.forward(size)
            tom.left(90)
        if number_of_squares-i>1:
            tom.penup()
            tom.forward(size+distance)
            tom.pendown()

def many_circles(size,x,y):
    move_to(x,y)
    for i in range(10):
        tom.circle(size)
        tom.forward(20)

def draw_square_at(x,y):
    move_to(x,y)
    square(50)

def draw_grid(rows,cols,size):
    for i in range(rows+1):
        tom.forward(size*cols)
        move_to(0,-(i+1)*size)
    move_to(0,0)
    tom.right(90)
    for i in range(cols+1):
        tom.forward(size*rows)
        move_to((i+1)*size,0)
    move_to(0,0)

def draw_house(size):
    square(size)
    triangle(size)

def spiral_square(twists):
    iteration = 1
    while iteration <= twists:
        for i in range(2):
            tom.forward(10*iteration)
            tom.left(90)
        iteration += 1

def star_polygon(vertices,size):
    for i in range(vertices):
        tom.forward(size)
        tom.left(180/vertices+180)


def cool_pattern(twists):
    iteration = 1
    while iteration <= twists:
        for i in range(3):
            tom.forward(10*iteration)
            tom.left(90)
        tom.forward(10+(iteration*10))
        iteration+=1

tom = turtle.Turtle()  # create an object named tom of type Turtle
tom.shape("turtle")  # make Tom look like a turtle
# demo()
# circle(43)
# move_to(50,200)
# square(45)
# triangle(94)
# coloured_triangle(120,"red")
# many_squares(3,70,30)
# many_circles(50,-200,5)
# draw_square_at(-30,-200)
# draw_grid(50,100,3)
# draw_house(50)
# spiral_square(15)
# star_polygon(11, 200)
cool_pattern(30)

turtle.done()  # keep the turtle window open after the program is done
