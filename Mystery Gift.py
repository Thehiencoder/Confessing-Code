# Import turtle package 
import turtle 
#import playsound
#playsound('audio.mp3')
#*********** This project is made by The Hien***************
#I do not own the license to use this code as a way to make money
#watch the tips for gaining insights of the code below
#create beautiful gradient background
from turtle import Screen, Turtle

color = (0.10160, 0.2, 0.7260)  # (154, 0, 254)
target = (0.86310, 0.47260, 0.31255)  # (221, 122, 80)
turtle.title("Confession Box")
tur = Screen()
tur.setup(800,800)
tur.tracer(False)
#turtle.speed('fastest')

width, height = tur.window_width(), tur.window_height()

deltas = [(hue - color[index]) / height for index, hue in enumerate(target)]

turt = Turtle()
turt.color(color)
turt.speed('fastest')
turt.penup()
turt.goto(-width/2, height/2)
turt.pendown()

direct = 1

for distance, y in enumerate(range(height//2, -height//2, -1)):

    turt.forward(width * direct)
    turt.color([color[i] + delta * distance for i, delta in enumerate(deltas)])
    turt.sety(y)

    direct *= -1

tur.tracer(True)
#tur.exitonclick()

# Creating a turtle object(pen) 
pen = turtle.Turtle() 

# Defining a method to draw curve 
def curve(): 
	for i in range(200): 

		# Defining step by step curve motion 
		pen.right(1) 
		pen.forward(2) 

# Defining method to draw a full heart 
def heart(): 

	# Set the fill color to red 
	pen.fillcolor('red') 

	# Start filling the color 
	pen.begin_fill() 

	# Draw the left line 
	pen.left(114) 
	pen.forward(113) 

	# Draw the left curve 
	curve() 
	pen.left(112) 

	# Draw the right curve 
	curve() 

	# Draw the right line 
	pen.forward(120) 

	# Ending the filling of the color 
	pen.end_fill() 

# Defining method to write text 
def txt(): 

	# Move turtle to air 
	pen.up() 

	# Move turtle to a given position 
	pen.setpos(-68, 95) 

	# Move the turtle to the ground 
	pen.down() 

	# Set the text color to lightgreen 
	pen.color('yellow') 

	# Write the specified text in 
	# specified font style and size 
	pen.write("I love you", font=( 
	"Times New Roman", 20, "bold"))
	#pen.down()
	#pen.setpos(-54,77)

	#pen.color('blue')
	#pen.write("Will you agree?", font=("Times New Roman",16,"bold")) 
    
	#Give the answer to the confesser
	#turt = turtle.Screen()
    
	#turt.setup(800, 600)
    
	tur=turtle.textinput("Here is the answer box ", "Give your answer, babe: ")
    
	print(tur)
	if(tur=='yes'):
		pen.down()
	    
		pen.setpos(-54,70)
        
		pen.color('blue')

		pen.write("Finally!", font=("Times New Roman",16,"bold"))

    #str(input()) 

# Draw a heart 
heart() 

# Write text 
txt() 
#pen.background_fill('red')
# To hide turtle 
pen.ht()
turtle.done()