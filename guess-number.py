#LINK==>http://www.codeskulptor.org/#user42_gETf5E8HI1gt1JP.py

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math
test=0
# helper function to start and restart the game
def new_game():
    print "New Game Started"
    # initialize global variables used in your code here
    global secret_number
    global test
    test=0
    # secret_number=range100()
    # remove this when you add your code    


# define event handlers for control panel
def range100():
    global secret_number,test
    test=8
    # button that changes the range to [0,100) and starts a new game 
    secret_number=random.randrange(0,99)
    return secret_number
    # remove this when you add your code    

def range1000():
    global secret_number,test
    test=11
    # button that changes the range to [0,1000) and starts a new game     
    secret_number=random.randrange(0,999)
    

def input_guess(guess):
    global secret_number,test
    print "Guess was " + guess
    test=test-1
    print "number of remaining guess :", test
    # main game logic goes here	
    if int(guess)==secret_number:
        print "correct!"
    elif int(guess)<secret_number:
        print "higher!"
    elif int(guess)>secret_number:
        print "lower!"
    else:
        print "Out of Range!"
    if test==0:
        new_game()
        
    # remove this when you add your code
    

    
# create frame
frame=simplegui.create_frame("Guess The Number",200,200)
frame.add_button("Range in [0,100]",range100)
frame.add_button("Range in [0,1000]",range1000)
frame.add_input("Enter a Guess",input_guess,100)

# register event handlers for control elements and start frame


# call new_game 
new_game()

