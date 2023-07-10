import turtle
import random

bound = turtle.Turtle()
sc = bound.screen
sc.setup(500,500)

#boundry building
bound.speed(10)
bound.color("green")
bound.pu()
bound.goto(200,0)
bound.lt(90)
bound.pd()
bound.pensize(10)
bound.goto(200,200)
bound.goto(-200,200)
bound.goto(-200,0)
bound.ht()

#pedlle
pedlle = turtle.Turtle("square")
pedlle.color("blue")
pedlle.shapesize(0.5,3)
pedlle.pu()
#pedlle.goto(0,-150)

#move pedlle
#def right():
    #pedlle.setx(pedlle.xcor()+30)

#def left():
    #pedlle.setx(pedlle.xcor()-30)   

def move(x,y):
    pedlle.setx(x)


#key binding 
#sc.onkey(right,"Right")
#sc.onkey(left,"Left")
#sc.listen()
sc.onclick(move)
#score baord
scorer = turtle.Turtle()
scorer.pu()
scorer.goto(-240,240)
score = 0
scorer.write(score)

#dot making/moving
dot = turtle.Turtle("circle")
dot.color("yellow")
dot.pu()

#set heading
angle = random.randint(0,180)
dot.setheading(30)

#reflect logic
while True:
    dot.fd(5)
    #right/left wall
    if (dot.xcor()>= 185) or (dot.xcor()<=-185):
        if dot.ycor()>0:
            dot.setheading(180-dot.heading())
        else:
            break
    #top wall
    elif (dot.ycor()>=185) :
        dot.setheading(360-dot.heading())
    #peddle
    elif(dot.ycor()<=0):
        if ( pedlle.xcor() - 35 <= dot.xcor() <= pedlle.xcor() +35):
          scorer.clear()
          score +=1
          scorer.write(score)
          #print("dx=",dot.xcor(),"px=",pedlle.xcor())
          dot.setheading(360-dot.heading())
        else:
            dot.write("you lose")
            break  

sc.mainloop()