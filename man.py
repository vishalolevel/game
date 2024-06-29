import random
n = ["rock","paper","scissors"]
b = input("choose rock,paper,scissors: ")
computer_choice = random.choice(n)
print("your choice:",b)
print("computer_choice :",computer_choice )
if b == computer_choice:
    print("it is tie:")
elif b == "rock" and computer_choice == "scissors" or b == "scissors" and computer_choice == "paper" or b == "paper" and computer_choice == "rock":
    print("you win")
else:
    print("computer win")    


