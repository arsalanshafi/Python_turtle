import turtle
import random
sc = turtle.Screen()
sc.setup(500,500)


shooter = turtle.Turtle("turtle")
dot = turtle.Turtle("circle")
dot.shapesize(0.25)
shooter.pu()
dot.pu()
shooter.goto(0,-230)
dot.goto(0,-230)
shooter.lt(90)
dot.lt(90)


def shoot():
    while True:
        dot.fd(1)
        if dot.ycor()>=200:
            dot.goto(shooter.xcor(),shooter.ycor())
            break

def right():
    shooter.setx(shooter.xcor()+10)
def left():
    shooter.setx(shooter.xcor()-10)

sc.onkey(right,"Right")
sc.onkey(left,"Left")
sc.onkey(shoot,"Up")
sc.listen()

#falling turtles
while True:
    pos = random.randint(-240,240)
    fall = turtle.Turtle("turtle")
    fall.ht()
    fall.pu()
    fall.goto(pos,240)
    fall.showturtle()
    fall.rt(90)
    for i in range (0,48): 
        fall.fd(10)
        if fall.ycor()<=-200:
            fall.ht()
            break


        
sc.mainloop()