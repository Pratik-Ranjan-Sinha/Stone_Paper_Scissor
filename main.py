# code for Stone, Paper and Scissor Game.

import random
from colorama import init
from termcolor import colored

choice = ['STONE','PAPER','SCISSOR']
randomData = random.choice(choice) # now this is a better fuction that i found which will only select the random value that only i want of my choice
# print(randomData)
# randomData = random.randint(1,3) # this function will be used to generate random numbers in python.
print(colored("***** Your Input Should Only Be STONE, PAPER and SCISSOR *****",'green'))
print(colored("------------------------------------ !! WARNING !! ------------------------------------",'red'))
print(colored("This is a Case Sensitive Program So use STONE, PAPER and SCISSOR exact as it is written",'red'))
userInput = input(colored("Enter your Selection : ",'green'))

if(userInput == 'STONE' or userInput == 'PAPER' or userInput == 'SCISSOR'):
    if(userInput == 'STONE' and randomData == 'STONE'):
        print(colored("Its a Tie",'yellow'))
        print("Computer Selected : ",randomData)
    elif(userInput == 'STONE' and randomData == 'PAPER'):
        print(colored("Computer Wins",'cyan'))
        print("Computer Selected : ",randomData)
    elif(userInput == 'PAPER' and randomData == 'PAPER'):
        print(colored("Its a Tie",'yellow'))
        print("Computer Selected : ",randomData)
    elif(userInput == 'PAPER' and randomData == 'SCISSOR'):
        print(colored("Computer Wins", 'cyan'))
        print("Computer Selected : ",randomData)
    elif(userInput == 'SCISSOR' and randomData == 'SCISSOR'):
        print(colored("Its a Tie",'yellow'))
        print("Computer Selected : ",randomData)
    elif(userInput == 'SCISSOR' and randomData == 'STONE'):
        print(colored("Computer Wins", 'cyan'))
        print("Computer Selected : ",randomData)
    elif(userInput == 'STONE' and randomData == 'SCISSOR'):
        print(colored("Human Wins", 'green'))
        print("Computer Selected : ",randomData)
    elif(userInput == 'SCISSOR' and randomData == 'PAPER'):
        print(colored("Human Wins", 'green'))
        print("Computer Selected : ",randomData)
    elif(userInput == 'PAPER' and randomData == 'STONE'):
        print(colored("Human Wins", 'green'))
        print("Computer Selected : ",randomData)
else:
    print(colored("Re-Enter your Selection",'red'))


