import random

'''
Milestone 2: If you have extra time, see if you can repeatedly answer questions 
until the user enters no question 
(i.e. they press enter without pressing anything)
'''

#Creating a list of responses. Simpler this way 
responses = ['As I see it, yes.','Ask again later.','Better not to tell you now.','Cannot predict now.','Concentrate and ask again.','Don\'t count on it.','Outlook good.','My sources say no.','Reply hazy, try again.','Very doubtful.']
low=1 
length_of_responses = len(responses) #Returns the number of elements in a list
high = length_of_responses #The highest number is the length_of_responses

random_responses = random.randint(low,high)
question = input('Ask a yes or no question: ')
while question!='':
     print(random.choice(responses))
     question = input('Ask a yes or no question: ')










