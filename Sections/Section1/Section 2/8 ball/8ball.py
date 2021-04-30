"""
Simulates a magic eight ball.
Prompts the user to type a yes or no question and gives
a random answer from a set of prefabricated responses.
"""
# Milestone 1: For the basic version of a program, have it answer only one question.
import random
response_1 = 'As I see it, yes.'
response_2 =  'Ask again later.'
response_3 = 'Better not to tell you now.'
response_4 = 'Concentrate and ask again.'
responde_5 =  'Don\'t count on it. '

question  = input('Ask a yes or no question: ')


def main():
   low = 1
   high = 5
   num = random.randint(low,high)

   if num==1:
       print(response_1)
   elif num==2:
        print(response_2)
   elif num==3:
        print(response_3)
   elif num==4:
        print(response_4)
   elif num==5:
         print(response_5)

main()







