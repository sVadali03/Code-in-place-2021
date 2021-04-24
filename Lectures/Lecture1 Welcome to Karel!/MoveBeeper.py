from karel.stanfordkarel import *

"""
File: MoveBeeper.py
------------------------------
Karel will move the beeper up to the top of its column.
Karel starts in the bottom left corner, facing East, in front of the beeper, and Karel will end in the top right corner facing East.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    move()
    pick_beeper()
    turn_left()
    move()
    move()
    put_beeper()
    turn_right()
    move()
# A function that tells karel to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
    

if __name__ == "__main__":
    run_karel_program()
