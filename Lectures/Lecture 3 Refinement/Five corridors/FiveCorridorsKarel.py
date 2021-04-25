from karel.stanfordkarel import *

"""
File: FiveCorridorsKarel.py
-----------------------
Karel traverse 5 variable length corridors and place beepers at the ends of them if there aren't already beepers there.
"""

def main():
    do_corridor()
    for i in range(4):
        turn_left()
        move()
        turn_right()
        do_corridor()

def do_corridor():
    # Precondition: Karel is facing East in column 1; postcondition: Karel is facing East in col 1, corridor has beeper at the end of it.
    move_to_wall()
    if no_beepers_present():
        put_beeper()
    turn_around()
    move_to_wall()
    turn_around()

def move_to_wall():
    while front_is_clear():
        move()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

if __name__ == "__main__":
    run_karel_program()
