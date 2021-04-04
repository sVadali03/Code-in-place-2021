# Your task: Write a program in the editor, that makes Karel pick up a beeper and go back into its house.

"""People around the world are staying at home to reduce the spread of COVID-19. Karel is doing their part by sheltering in place!
Karel starts off in the corner of its house as shown in the world. The problem Karel needs to solve is to collect some food, represented (as all objects in Karel's world are) by a beeper, from outside the doorway and then to return to its initial position.
You can assume that every part of the world is always the same. The house is exactly this size, the door is always in the position shown, and the beeper is just outside the door. Thus, all you have to do is write the sequence of commands necessary to have Karel
- Move to the beeper,
- Pick it up, and
- Return to its starting point.
Even though the program is only a few lines, it is still worth getting at least a little practice in decomposition. In your solution, include a function for moving to the package, and returning to the starting point.
"""
from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.
def main():
   move()
   move()
   turn_right()
   move()
   turn_left()
   move()
   pick_beeper()
   turn_right()
   turn_left()
   turn_left()
   turn_left()
   move()
   move()
   move()
   turn_right()
   move()


def turn_right():
   turn_left()
   turn_left()
   turn_left()


def turn_around():
   turn_left()
   turn_left()
