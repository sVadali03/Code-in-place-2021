from karel.stanfordkarel import *

"""
File: 2021.py
--------------------
When you finish writing this file, Karel should be able to place 20 beepers,
then 21 beepers, and end facing East to the right of the 21 beepers.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    place_20_beepers()
    place_21_beepers()
    
def place_20_beepers():
    for x in range(20):
        put_beeper()
    move()
def place_21_beepers():
    for x in range(21):
        put_beeper()
    move()
    

if __name__ == '__main__':
    run_karel_program('3x3.w')
