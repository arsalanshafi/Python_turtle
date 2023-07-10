import turtle
import random
chaser = turtle.Turtle()
dot = turtle.Turtle()
scorer = turtle.Turtle()
sc = chaser.screen
sc.setup(500,500)
sc.bgcolor("green")
dot.shape("circle")
chaser.shapesize(2)
chaser.pu()
dot.pu()
scorer.pu()
scorer.goto(-200,200)
score = 0


def movedot():
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    dot.goto(x,y)
movedot()
def forward ():
    chaser.fd(10)
    if (chaser.xcor() >= dot.xcor()-10 and chaser.xcor() <= dot.xcor()+10) and (chaser.ycor() >= dot.ycor() -10 and chaser.ycor() <= dot.ycor() +10):
      #print("true")
      movedot()
      scorer.clear()
      global score
      score +=1
      scorer.write(score)
    #print("chaserx = ",chaser.xcor(),"dot xcor =",dot.xcor(),"chasery=",chaser.ycor(),"dopt y =",dot.ycor())
def right():
    chaser.rt(90)
def left():
    chaser.lt(90)

sc.onkey(forward,"Up")
sc.onkey(right,"Right")
sc.onkey(left,"Left")
sc.listen()

sc.mainloop()