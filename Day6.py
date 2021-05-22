# Day 6 Project: Karel



# These are the directions to get Reeborg's World ( https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json )

def turnRight():
    turn_left()
    turn_left()
    turn_left()
def hurdle():
    move()
    turn_left()
    move()
    turnRight()
    move()
    turnRight()
    move()
    turn_left()
for steps in range(6):    
    hurdle()
# for the Hurdle 2 example in Reeborg's World
while True: 
        hurdle()
        if at_goal():
            break

# for the Hurdle 3 example
def turnRight():
    turn_left()
    turn_left()
    turn_left()
def hurdle():
    turn_left()
    move()
    turnRight()
    move()
    turnRight()
    move()
    turn_left()
    

while not at_goal(): 
    if wall_in_front():
       hurdle()
    elif front_is_clear():
        move()