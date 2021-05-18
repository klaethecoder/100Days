# Day 6 Project: Karel



# These are the directions to get Reeborg's World ( https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json )

def turnRight():
    turn_left()
    turn_left()
    turn_left()
def goForIt():
    move()
    turn_left()
    move()
    turnRight()
def connect():
    move()
    turnRight()
    move()
    turn_left()
   
def hurdle():
    goForIt()
    move()
    turnRight()
    move()
    turn_left()
    goForIt()
    
hurdle()
connect()
hurdle()
connect()
hurdle()
connect()