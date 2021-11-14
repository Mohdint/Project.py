#Mohdint

#imported turtle module
import turtle

wind = turtle.Screen()
wind.title("Ping Pong Created By Mohdint©")
wind.bgcolor("blue")
wind.setup(width=800, height=600)
wind.tracer(0)

#M1
M1 = turtle.Turtle()
M1.speed(0)
M1.shape("circle")
M1.color("white")
M1.shapesize(stretch_wid=5, stretch_len=1)
M1.penup()
M1.goto(-350, 0)

#M2
M2 = turtle.Turtle()
M2.speed(0)
M2.shape("circle")
M2.color("red")
M2.shapesize(stretch_wid=5, stretch_len=1)
M2.penup()
M2.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0 Player 2: 0", align="center", font=("Courier",24,"normal"))

#functions
def M1_up():
    y = M1.ycor()
    y += 20
    M1.sety(y)

def M1_down():
    y = M1.ycor()
    y -= 20
    M1.sety(y)

def M2_up():
    y = M2.ycor()
    y += 20
    M2.sety(y)

def M2_down():
    y = M2.ycor()
    y -= 20
    M2.sety(y)


#keyboard bindings
wind.listen()
wind.onkeypress(M1_up, "w")
wind.onkeypress(M1_down, "s")

wind.listen()
wind.onkeypress(M2_up, "Up")
wind.onkeypress(M2_down, "Down")

#main game loop
while True:
    wind.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx) #ball starts at 0 and everytime loops run--->0.2 x
    ball.sety(ball.ycor() + ball.dy) #ball starts at 0 and everytime loops run--->0.2 y

    #border check return ball
    if ball.ycor() >290: #if ball is at top border
        ball.sety(290) #set y coordinate +290
        ball.dy *= -1 #reverse direction, making +0.2---> -0.2

    if ball.ycor() <-290: #if ball is at bottom border
        ball.sety(-290) #set y coordinate -290
        ball.dy *= -1 #reverse direction, making -0.2---> +0.2

    if ball.xcor() >390: #if ball is at right border
        ball.goto(0, 0) #return ball to center
        ball.dx *= -1 #reverse the x direction
        score1 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier",24,"normal"))

    if ball.xcor() <-390: #if ball is at left border
        ball.goto(0, 0) #return ball to center
        ball.dx *= -1 #reverse the x direction
        score2 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier",24,"normal"))

    #tasadom madrab and ball
    if(ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < M2.ycor() + 40 and ball.ycor() > M2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < M1.ycor() + 40 and ball.ycor() > M1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1    

