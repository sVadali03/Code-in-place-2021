from karel.stanfordkarel import *

"""
File: TensKarel.py
-----------------------
Place 10 beepers in all spots on the bottom row of any sized world.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        place_beepers_10()
        move()
    place_beepers_10()

def place_beepers_10():
    for x in range(10):
        put_beeper()
    

if __name__ == "__main__":
    run_karel_program('TensKarel1.w')
