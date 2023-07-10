import turtle
import random
a = turtle.Turtle()
a.hideturtle()
sc = a.screen
sc.setup(500,500)
racer_i = []
color_list = ["red","blue","orange","green","pink",
               "yellow","cyan","lightgreen","skyblue","turquoise"]
c = 240
for color in color_list:
    for i in range(0,1):
        ai = turtle.Turtle()
        racer_i.append(ai)
        ai.shape("turtle")
        ai.pu() 
        ai.color(color)
        ai.goto(-240,c)
        c -= 50

finish = 0

while finish<220:
    for racer in racer_i:
        steps = random.randint(1,10)
        racer.pd()
        racer.fd(steps)
        finish = racer.xcor()
        if finish >220:
            racer.color("red")
            racer.write("i won")
            break
    

sc.mainloop()