"""Your task: Write a program in the editor, that makes Karel pick up all the beepers on the first row of this world. Karel can end on any square, facing in any direction."""
from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.
def main():
   move()
   pick_3()
   move()
   pick_3()
   move()
   pick_3()
   
def pick_3():
   for x in range(10):
      pick_beeper()
   move()
