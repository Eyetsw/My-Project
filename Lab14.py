

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
import random 

weapons= [rock , scissors , paper]

user = int(input("Enter your weapon 0 = rock , 1 = scissors , 2 =paper :"))
computer = random.randint(0,2)

print(weapons[user])
print("         vs          ")
print(weapons[computer])

print("--------------------------------------------")

if(user == 0):
    if(computer == 0):
       print("you draw")
    if(computer == 1):
        print("you win")
    if(computer == 2):
        print("you lose")
        
if(user == 1):
    if(computer == 1):
       print("you draw")
    if(computer == 2):
        print("you win")
    if(computer == 0):
        print("you lose")
        
if(user == 2):
    if(computer == 2):
       print("you draw")
    if(computer == 0):
        print("you win")
    if(computer == 1):
        print("you lose")
    
       