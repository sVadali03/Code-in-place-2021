import random

HEADS_WEIGHT = 0.7
def main():
    
    if random.random() < HEADS_WEIGHT:
        print("Heads!")
    else:
        print("Tails!")
    
if __name__ == "__main__":
    main()
