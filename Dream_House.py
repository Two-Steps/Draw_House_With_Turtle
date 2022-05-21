import turtle

def house():
    t = turtle.Turtle()
    screen = turtle.Screen()
    t.speed(8)
    # step 1
    t.fillcolor('blue')
    t.begin_fill()
    t.penup()
    t.goto(-200, -200)
    t.pendown()
    for i in range(2):
        t.forward(200)
        t.left(90)
        t.forward(250)
        t.left(90)
    t.end_fill()
    # step 2
    t.penup()
    t.goto(-125, -200)
    t.pendown()
    t.fillcolor('green')
    t.begin_fill()
    for i in range(2):
        t.forward(50)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.end_fill()
    # step 3
    t.penup()
    t.goto(0,-200)
    t.pendown()
    t.fillcolor('yellow')
    t.begin_fill()
    t.left(30)
    for i in range(2):
        t.forward(200)
        t.left(60)
        t.forward(250)
        t.left(120)
    t.end_fill()
    # step 4
    t.penup()
    t.goto(75,-50)
    t.pendown()
    t.fillcolor('brown')
    t.begin_fill()
    for i in range(2):
        t.forward(50)
        t.left(60)
        t.forward(50)
        t.left(120)
    t.end_fill()
    # step 5
    t.penup()
    t.goto(0,50)
    t.pendown()
    t.fillcolor('purple')
    t.begin_fill()
    t.left(120)
    t.forward(115.5)
    t.left(60)
    t.forward(115.5)
    t.end_fill()
    # tesp 6
    t.penup()
    t.goto(0,50)
    t.left(180)
    t.pendown()
    t.fillcolor('orange')
    t.begin_fill()
    for i in range(2):
        t.forward(200)
        t.left(120)
        t.forward(115.5)
        t.left(60)
    t.end_fill() 
    # tree
    t.right(30)
    t.fillcolor('brown')
    t.begin_fill()
    t.penup()
    t.goto(240,-150)
    t.pendown()
    for i in range(2):
        t.fd(20)
        t.lt(90)
        t.fd(50)
        t.lt(90)
    t.end_fill()
    # step 2
    t.goto(240,-100)
    t.fillcolor('green')
    t.begin_fill()
    t.bk(40)
    t.fd(100)
    t.goto(250,-50)
    t.goto(200,-100)
    t.end_fill()
    # step 3
    t.penup() 
    t.goto(200,-50)
    t.pendown()
    t.begin_fill()
    t.fd(100)
    t.goto(250,0)
    t.goto(200,-50)
    t.end_fill()
    # step 4
    t.penup() 
    t.goto(200,0)
    t.pendown()
    t.begin_fill()
    t.fd(100)
    t.goto(250,50)
    t.goto(200,0)
    t.end_fill()

    # draw the sun
    t.penup()
    t.goto(-300,250)
    t.pendown()
    # step 1
    for i in range(4):
        t.fd(100)
        t.goto(-300,250)
        t.left(90)
    # step 2
    t.left(45)
    for i in range(4):
        t.fd(75)
        t.goto(-300,250)
        t.left(90)
    t.right(45)
    t.fillcolor('yellow')
    t.begin_fill()
    t.penup()
    t.goto(-300,200)
    t.pendown()
    t.circle(50)
    t.end_fill()

    turtle.done()

def tree():
    t = turtle.Turtle()
    screen = turtle.Screen()
    t.speed(8)
    t.fillcolor('brown')
    t.begin_fill()
    t.penup()
    t.goto(240,-150)
    t.pendown()
    for i in range(2):
        t.fd(20)
        t.lt(90)
        t.fd(50)
        t.lt(90)
    t.end_fill()
    # step 2
    t.goto(240,-100)
    t.fillcolor('green')
    t.begin_fill()
    t.bk(40)
    t.fd(100)
    t.goto(250,-50)
    t.goto(200,-100)
    t.end_fill()
    # step 3
    t.penup() 
    t.goto(200,-50)
    t.pendown()
    t.begin_fill()
    t.fd(100)
    t.goto(250,0)
    t.goto(200,-50)
    t.end_fill()
    # step 4
    t.penup() 
    t.goto(200,0)
    t.pendown()
    t.begin_fill()
    t.fd(100)
    t.goto(250,50)
    t.goto(200,0)
    t.end_fill()

    turtle.done()

def sun():
    t = turtle.Turtle()
    screen = turtle.Screen()
    t.speed(8)
    # step 1
    for i in range(4):
        t.fd(100)
        t.goto(0,0)
        t.left(90)
    # step 2
    t.left(45)
    for i in range(4):
        t.fd(75)
        t.goto(0,0)
        t.left(90)
    t.right(45)
    t.fillcolor('yellow')
    t.begin_fill()
    t.penup()
    t.goto(0,-50)
    t.pendown()
    t.circle(50)
    t.end_fill()

    turtle.done()

def main():
    house()


if __name__ == "__main__":
    main()
