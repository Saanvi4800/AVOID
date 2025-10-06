# Import necessary libraries
import turtle as trtl
import random
import time
import os
import sys
import tkinter as tk

#Set up screen
wn=trtl.Screen()
wn.title("AVOID")
wn.bgcolor("old lace")
wn.screensize(400,400)


# Turtle color/shape options
turtle_shapes = ["arrow","turtle","circle","triangle","classic"]
turtle_colors = ["dark salmon","salmon","light coral","hot pink","steel blue","purple","pale violet red","MediumPurple1","LightSkyBlue1","DeepPink"]

# Default user settings (will be replaced by menu selections)
user_shape = "turtle"
user_color = "steel blue"
user_speed = 10
user_difficulty = 5

# Writer turtle for menu
writer = trtl.Turtle()
writer.hideturtle()
writer.penup()

def write_text(text, x, y, size=18):
    writer.goto(x, y)
    writer.write(text, align="center", font=("Futura", size, "bold"))
#Instructions
write_text("Welcome to AVOID! Use the arrow keys to move your turtle and avoid the obstacles", 0, 0, 18)
time.sleep(3)
writer.clear()
write_text("You can customize your turtle's shape, color, and speed", 0, 0, 18)
time.sleep(3)
writer.clear()
write_text("The objective is to AVOID the obstacles and get the chests!", 0, 0, 18)
time.sleep(3)
writer.clear()
write_text("Good luck!", 0, 0, 18)
time.sleep(2)
writer.clear()

# --- Menu functions ---
def pick_shape(shape):
    global user_shape
    user_shape = shape
    wn.clear()
    wn.bgcolor("old lace")
    show_color_menu()

def pick_color(color):
    global user_color
    user_color = color
    wn.clear()
    wn.bgcolor("old lace")
    show_difficulty_menu()

def pick_difficulty(level):
    global user_difficulty
    user_difficulty = level
    wn.clear()
    wn.bgcolor("old lace")
    show_speed_menu()

def pick_speed(speed):
    global user_speed
    user_speed = speed
    wn.clear()
    wn.bgcolor("old lace")
    start_game()



# --- Menus ---

def show_shape_menu():
    wn.tracer(False)
    write_text("Choose your Turtle Shape", 0, 250, 24)
    y=150
    for shape in turtle_shapes:
        button = trtl.Turtle()
        button.shape("square")
        button.color("lightblue")
        button.shapesize(1, 5)
        button.penup()
        button.goto(0, y)
        button.onclick(lambda x, y, s=shape: pick_shape(s))
        write_text(shape,0,y+15,18)
        y-=60
    wn.tracer(True) 
    wn.update()




def show_color_menu():
    write_text("Choose your Turtle Color", 0, 250, 24)
    y = 150
    for color in turtle_colors:
        button = trtl.Turtle()
        button.shape("square")
        button.color(color)
        button.shapesize(1, 5)
        button.penup()
        button.goto(0, y)
        button.onclick(lambda x, y, c=color: pick_color(c))
        y -= 60

def show_difficulty_menu():
    write_text("Choose Difficulty (1 = Easy, 20 = Hard)", 0, 250, 18)
    y = 150
    for level in [1, 5, 10, 15, 20]:
        button = trtl.Turtle()
        button.shape("square")
        button.color("lightblue")
        button.shapesize(1, 3)
        button.penup()
        button.goto(0, y)
        write_text(level,0,y+15,18)
        button.onclick(lambda x, y, l=level: pick_difficulty(l))
        y -= 60

def show_speed_menu():
    write_text("Choose Movement Speed", 0, 250, 24)
    y = 150
    for speed in [5, 10, 15, 20]:
        button = trtl.Turtle()
        button.shape("square")
        button.color("lightblue")
        button.shapesize(1, 4)
        button.penup()
        button.goto(0, y)
        write_text(speed,0,y+15,18)
        button.onclick(lambda x, y, s=speed: pick_speed(s))
        y -= 60

def restartGame():
    os.execl(sys.executable, sys.executable, *sys.argv)
    continueloop = 1

def restart_game_menu():
    write_text("Restart Game?",0,250,24)
    y = 150
    for option in ["Yes","No"]:
        button = trtl.Turtle()
        button.shape("square")
        button.color("lightblue")
        button.shapesize(1, 5)
        button.penup()
        button.goto(0, y)
        write_text(option,0,y+15,18)
        if option == "Yes":
            button.onclick(lambda x, y: restartGame())
        else:
            button.onclick(lambda x, y: wn.bye())
        y -= 60
   


def start_game():
    user=trtl.Turtle()
    user.shape(user_shape)
    user.color(user_color)
    user.showturtle()
    user.penup()

    #Define funtions that handle turtle movement
    def move_right():
        x = user.xcor()
        user.setx(x+user_speed)

    def move_left():
        x = user.xcor()
        user.setx(x-user_speed)

    def move_up():
        y = user.ycor()
        user.sety(y+user_speed)

    def move_down():
        y = user.ycor()
        user.sety(y-user_speed)


    wn.onkey(move_right, "Right")
    wn.onkey(move_left, "Left")
    wn.onkey(move_up,"Up")
    wn.onkey(move_down, "Down")
    wn.listen()

    #Create the obstacles (make them move?)
    obstacles=[]
    obstacle_shape = random.choice(turtle_shapes)
    obstacle_color = random.choice(turtle_colors)
    for i in range(10):
        obstacle_shape = obstacle_shape
        obstacle_color = obstacle_color
        obstacle=trtl.Turtle()
        obstacle.shape(obstacle_shape)
        obstacle.color(obstacle_color)
        obstacle.penup()
        obstacle.speed(0)
        obstacle.goto(random.randint(-200,200),random.randint(-200,200))
        obstacle.dx = random.choice([-2,2])
        obstacle.dy = random.choice([-2,2])
        obstacles.append(obstacle)

    #Add the chests, 

    chests=[]
    for x in range(5):
        chest=trtl.Turtle()
        chest.shape("square")
        chest.color("bisque")
        chest.penup()
        chest.speed(0)
        chest.goto(random.randint(-200,200),random.randint(-200,200))
        chest.dx = random.choice([-2,2])
        chest.dy = random.choice([-2,2])
        chests.append(chest)

    #Set up point system
    points = 0
    score_writer = trtl.Turtle()
    score_writer.penup()
    score_writer.hideturtle()
    score_writer.goto(-350, 300)
    score_writer.write("Points: {}".format(points), font=("Futura", 16, "normal"))
    def update_score():
        # `points` is defined in the enclosing function `start_game` — use nonlocal to modify it
        nonlocal points
        points += 1
        score_writer.clear()
        score_writer.write("Points: {}".format(points), font=("Futura", 16, "normal"))
    # every time you go to a chest it will add a point, and dissapear, thhere will be five
    continueloop = 1
    while continueloop < 10:
      wn.update()
      for chest in chests:
        if chest.isvisible() and chest.distance(user) < 20:
          chest.hideturtle()  
          update_score()
        if points == 5:
         score_writer.clear()
         score_writer.goto(-200, 0)
         score_writer.write("You Win!", font=("Futura", 80, "bold"))
         score_writer.goto(-200, -50)
         for obstacle in obstacles:
            obstacle.hideturtle()
         user.hideturtle()
         continueloop = 11
         time.sleep(4)
         score_writer.clear()
         points = 0
         restart_game_menu()
      for obstacle in obstacles:
        obstacle.penup()
        obstacle.forward(user_difficulty+10)
        obstacle.right(90)
        if obstacle.distance(user) < 20:
             for x in range(9):
                user.showturtle()
                time.sleep(.1)
                user.hideturtle()
             user.hideturtle()
             user.goto(600,600)
             for obstacle in obstacles:
                obstacle.hideturtle()
             for chest in chests:
                chest.hideturtle()
             score_writer.clear()
             score_writer.goto(-200, 0)
             score_writer.write("You lose!", font=("Futura", 80, "bold"))
             score_writer.goto(-200, -50)
             continueloop = 11
             time.sleep(4)
             score_writer.clear()
             restart_game_menu()
             

show_shape_menu()
wn.mainloop()