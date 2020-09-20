# V1 original by Christian Thompson  ==> Github: @wynand1004
#Comments and minor tweeks of the code ==> by Ali Rezaei ==> Github: Cry_Rez
#CC ==> Share all you want!
#Note that sound is configed for Windows and doesn't work on Mac or Linux
import pygame
import turtle  # helps in making basic graphics
import winsound #sound player module
from pygame import mixer

wn = turtle.Screen()
wn.title("Pong by Ali Rezaei")
wn.bgcolor("black")
wn.setup(width=800, height=600)
# Decreases tha amout of update time to the time when you only touch the controls so it speeds up the program:
wn.tracer(0)

#Backfround Sound (Pygame)
pygame.init()
mixer.music.load("Bounce")
mixer.music.play(-1)  #It only plays the song once if you don't ad -1 as an argument (does some mombo jumbo to play it in a loop)

#score
score_a = 0
Score_b = 0 

#Paddle A
paddle_a = turtle.Turtle()
# ===> THis basically determine the speed of the animation(soemthing you have to do for this module) ===> set to maximum
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()   #turtles by default draw the line when they are moving, we don't want them to do that so we use this
paddle_a.goto(-350, 0) #determines the start location of the right paddle



#Paddle B

paddle_b = turtle.Turtle()
# ===> THis basically determine the speed of the animation(soemthing you have to do for this module) ===> set to maximum
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #This basically stretches the size of the paddle from the default square
paddle_b.penup()  # turtles by default draw the line when they are moving, we don't want them to do that so we use this
paddle_b.goto(350, 0)  # determines the start location of the right paddle

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()  #if you don't use this function, the objects live lines behind them
ball.goto(0, 0)
ball.dx = 0.1  #basically says that every time the ball moves, it moves by 2px
ball.dy = 0.1


#Pen Score (Score Writing):
pen = turtle.Turtle()
pen.speed()
pen.color("White")
pen.penup()
pen.hideturtle() #==> We don't want the graphics, we want the text
pen.goto(0, 260)
pen.write("player A:0  Player B:0", align="center", font=("courier", 24,"bold"))





# Functions

def paddle_a_up():
    y = paddle_a.ycor()  # .ycor(): default Turtle mfunction that returns y coordinate
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()  
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()  
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


#Keyboard Binding
wn.listen()  # Set focus on TurtleScreen (in order to collect key-events)
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()  # every time the loop runs, it updates the screen
                    #if you put it at the start of the program(like I did at first) it won't get to the bottom section of the code and get stuck in the loop

#move the ball:
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

 #Border checking:

    #upper limit
    if ball.ycor()> 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("Bounce", winsound.SND_ASYNC)

    #lower limit:
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("Bounce", winsound.SND_ASYNC)

    #right limit
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear() #==> This cleans the old text and prints the new one (if you don't do this, the scores are just gonna print over each other) 
        pen.write("player A:{}  Player B:{}".format(score_a,Score_b), align="center",font=("courier", 24, "bold"))
    
    #left limit:
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        Score_b += 1
        pen.clear()
        pen.write("player A:{}  Player B:{}".format(score_a,Score_b), align="center",font=("courier", 24, "bold"))


    # Paddle and ball collisions

    #  if ball.xcor() > 340 ball.xcor() < 350)==> basically they are touching and the ball is not pass the paddle
    # and (ball.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50): ===> So this bascially says that if the ball has the same coordinates to the length of the paddle, it bounces back ===> (remember we streched the square paddles fromt their coordinate point so we need to account for that.)                                                             |

#right
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
#left
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
    #(basically what we do is to compare the coordinate of the paddles with the coordinates of the ball)


    






































#  ===> don't wait untill the wole code is typed to review it. Review it constantly while typing the program. That way, it's easier to find the problems. ===> Use iteration process
#   Read the error messages. most beginners don't.


#Notes for the future:
#add input from the users so they can determine the size of their paddles ==> (The difficulty continium    (easy) big======>small (hard))\
#set limit for the paddles so they can't exit the screen
#make it online or multiplayer
#add memes
#score system 
#add GUI and game menue
#randomize spawn moving direction
#perks: Double balls!
#Add red team and blue team
#Add cyberpunk style switching backgound pics


"""
Operator Precedence from highest to lowest

Parentheses/Brackets {} [] () 
function calling e.g square(5), indexing/slicing
await x
Exponentiation e.g x ** 3
+x, -x postive/negative
multiplication, division remainders e.g *, //, /, %
Addition and Subtraction, + and -
Shifts: <<, >>
Bitwise AND: &
Bitwise XOR: ^
Bitwise OR: |
Comparisons: in, is, is not, not in, ==, !=, >, <, >=, <=
Boolean NOT: not x
Boolean AND: and
Boolean OR: or
Conditional: if, else, elif
lambda expressions
Assignment Operator: =

"""



