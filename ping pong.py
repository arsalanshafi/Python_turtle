import turtle
import random
dot = turtle.Turtle("circle")
dot.color("yellow")
sc = dot.screen
# sc.bgpic("bg2.gif")

#score board
scorer_1 = turtle.Turtle()
scorer_2 = turtle.Turtle()
scorer_1.color("red")
scorer_2.color("red")
scorer_1.pu()
scorer_2.pu()
scorer_1.speed(7)
scorer_2.speed(7)
scorer_1.goto(230,230)
scorer_2.goto(-230,230)
score1 = 0
score2 = 0
scorer_1.write(score1)
scorer_2.write(score2)

#creating peddles
right_peddle = turtle.Turtle("square")
left_peddle  = turtle.Turtle("square")
right_peddle.color("blue")
left_peddle.color("blue")
right_peddle.shapesize(5,0.5)
left_peddle.shapesize(5,0.5)
right_peddle.pu()
left_peddle.pu()
right_peddle.goto(200,0)
left_peddle.goto(-200,0)

#creating functions to move peddles
def r_up():
    right_peddle.sety(right_peddle.ycor()+20)
def r_down():
    right_peddle.sety(right_peddle.ycor()-20)
def l_up():
    left_peddle.sety(left_peddle.ycor()+20)
def l_down():
    left_peddle.sety(left_peddle.ycor()-20)

#key binding
sc.onkey(r_up,"Up")
sc.onkey(r_down,"Down")
sc.onkey(l_up,"w")
sc.onkey(l_down,"s")
sc.listen()

#sqaure making and dot making
dot.speed(9)
sc.setup(500,500)
xleft = -200
yleft = -200
xright = 200
yright =200
dot.pu()
dot.goto(xleft,yleft)
dot.pd()
dot.goto(xleft,yright)
dot.goto(xright,yright)
dot.goto(xright,yleft)
dot.goto(xleft,yleft)
dot.pu()
dot.goto(0,0)
angle = random.randint(1,30)
dot.lt(angle)
dot.speed(3)


#game logic
while True:
    dot.fd(5)
    #right/left peddle hit
    if (   dot.xcor() >= xright ) or ( dot.xcor() <= xleft ) :
        #print("dy=",dot.ycor(),"py=",right_peddle.ycor())
        if ( right_peddle.ycor() - 35 <= dot.ycor() <= right_peddle.ycor() + 35 ):
            scorer_1.clear()
            score1 +=1
            scorer_1.write(score1)
            dot.setheading(180-dot.heading())
        elif ( left_peddle.ycor() - 35 <= dot.ycor() <= left_peddle.ycor() + 35 ):
            scorer_2.clear()
            score2 +=1
            scorer_2.write(score2)
            dot.setheading(180-dot.heading())
        else:
            dot.write("you lose")
            break
    #top/bottom wall hit
    elif ( dot.ycor() >= yright ) or ( dot.ycor() <= yleft ) :
        dot.setheading(360-dot.heading())

  

sc.mainloop()