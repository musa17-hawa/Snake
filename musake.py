
import turtle
import random #We'll need this later in the lab
import time
turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500

UP_EDGE = SIZE_Y/2
DOWN_EDGE = -SIZE_Y/2
RIGHT_EDGE = SIZE_X/2
LEFT_EDGE = -SIZE_X/2

#drawing border
turtle.pu()
turtle.goto(RIGHT_EDGE,UP_EDGE)
turtle.pd()
turtle.goto(LEFT_EDGE,UP_EDGE)
turtle.goto(LEFT_EDGE,DOWN_EDGE)
turtle.goto(RIGHT_EDGE, DOWN_EDGE)
turtle.goto(RIGHT_EDGE, UP_EDGE)
turtle.pu()
turtle.home()
turtle.pd()



turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window size.
turtle.penup()

SQUARE_SIZE = 22
START_LENGTH = 10


#Initialize lists
pos_list = []
stamp_list = []
current_stamps = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")



#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for counter in range(START_LENGTH):
	x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
	y_pos=snake.pos()[1] 

	#Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
	# You're RIGHT!
	x_pos+=SQUARE_SIZE 

	my_pos=(x_pos,y_pos) #Store position variables in a tuple
	snake.goto(my_pos[0],my_pos[1]) #Move snake to new (x,y)
   
	#Append the new position tuple to pos_list
	pos_list.append(my_pos) 

	#Save the stamp ID! You'll need to erase it later. Then append
	# it to stamp_list.             
	stamp_id = snake.stamp()
	stamp_list.append(stamp_id)


UP_ARROW = "Up" #Make sure you pay attention to upper and lower case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!



#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####YOUR CODE HERE!!


UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3


direction = UP

def up():
	global direction #snake direction is global (same everywhere)
	direction=UP #Change direction to up#Update the snake drawing <- remember me later
	print("You pressed the up key!")

#2. Make functions down(), left(), and right() that change direction
####YOUR CODE HERE!!


def down():
	global direction
	direction = DOWN
	print('You Pressed the down KEY')

def left():
	global direction
	direction = LEFT
	print('You Pressed the left KEY')

def right():
	global direction
	direction = RIGHT
	print('You Pressed the right KEY')



turtle.onkeypress(up, UP_ARROW) # Create listener for up key
#3. Do the same for the other arrow keys
####YOUR CODE HERE!!

turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)

turtle.listen()




def move_snake():

	my_pos = snake.pos()
	x_pos = my_pos[0]
	y_pos = my_pos[1]
	
	if direction==RIGHT:
		snake.goto(x_pos + SQUARE_SIZE, y_pos)
	elif direction==LEFT:
		snake.goto(x_pos - SQUARE_SIZE, y_pos)


	#4. Write the conditions for UP and DOWN on your own
	##### YOUR CODE HERE
	elif direction==UP:
		snake.goto(x_pos, y_pos + SQUARE_SIZE)
	elif direction==DOWN:
		snake.goto(x_pos, y_pos - SQUARE_SIZE)

	#Stamp new element and append new stamp in list
	#Remember: The snake position changed - update my_pos()

	# make head
	my_pos=snake.pos() 
	pos_list.append(my_pos)
	new_stamp = snake.stamp()
	stamp_list.append(new_stamp)
	######## SPECIAL PLACE - Remember it for Part 5
	global food_stamps, food_pos
	#If snake is on top of food item
	if snake.pos() in food_pos:
		food_ind=food_pos.index(snake.pos()) #What does this do?
		food.clearstamp(food_stamps[food_ind]) #Remove eaten food stamp
		food_pos.pop(food_ind) #Remove eaten food position
		food_stamps.pop(food_ind) #Remove eaten food stamp
	#HINT: This if statement may be useful for Part 8
		make_food()

	else:
		# remove tail
		old_stamp = stamp_list.pop(0)
		snake.clearstamp(old_stamp)
		pos_list.pop(0)


		#Add new lines to the end of the function
	#Grab position of snake
	new_pos = snake.pos()
	new_x_pos = new_pos[0]
	new_y_pos = new_pos[1]

	# The next three lines check if the snake is hitting the right 
	# edge.
	if new_x_pos >= RIGHT_EDGE:
		print("Game Over!!")
		quit()

		# You should write code to check for the left, top, and bottom edges.
		##### YOUR CODE HERE

	elif new_x_pos <= LEFT_EDGE:
		print("Game Over!!")
		quit()

	elif new_y_pos >= UP_EDGE:
		print("Game Over!!")
		quit()

	elif new_y_pos <= DOWN_EDGE:
		print("Game Over!!")
		quit()
	elif pos_list[-1] in pos_list[0:-1]:
		time.sleep(10)
	turtle.ontimer(move_snake,TIME_STEP)


turtle.register_shape("trash.gif") 
						#Add trash picture
						# Make sure you have downloaded this shape 
						# from the Google Drive folder and saved it
						# in the same folder as this Python script

food = turtle.clone()
food.shape("trash.gif") 

#Locations of food
food_pos = []
food_stamps = []

# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don’t forget to hide the food turtle!


def make_food():
	#The screen positions go from -SIZE/2 to +SIZE/2
	#But we need to make food pieces only appear on game squares
	#So we cut up the game board into multiples of SQUARE_SIZE.
	min_x=-int(SIZE_X/2/SQUARE_SIZE)-1
	max_x=int(SIZE_X/2/SQUARE_SIZE)+1
	min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
	max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
	
	#Pick a position that is a random multiple of SQUARE_SIZE
	food_x = (random.randint(min_x,max_x)*SQUARE_SIZE)
	food_y = (random.randint(min_y,max_y)*SQUARE_SIZE)
	new_food_location = (food_x, food_y)
	##1.YOUR CODE HERE: Make the food turtle go to the randomly-generated position 
	food.goto(food_x, food_y)

	##2.YOUR CODE HERE: Add the food turtle's position to the food positions list
	food_pos.append(new_food_location)
	##3.YOUR CODE HERE: Add the food turtle's stamp to the food stamps list
	food_stamps.append(food.stamp())
	

move_snake()



make_food()

turtle.mainloop()