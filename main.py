import random
'''
1 for snake
-1 for water 
0 for gun
'''
computer = random.choice([1, -1, 0])
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

if(youstr not in youDict):
    print("Invalid input! Please enter s, w, or g.")

you = youDict[youstr]


# By now we have 2 numbers (variables), computer and you

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(you == computer):
    print("It's a tie")
else:
    if(computer == -1 and you == 1):
        print("You win")

    elif(computer == -1 and you == 0):
        print("You Loose")
    
    elif(computer == 1 and you == -1):
        print("You loose")
    
    elif(computer == 1 and you == 0):
        print("You win")

    elif(computer == 0 and you == -1):
        print("You win")

    elif(computer == 0 and you == 1):
        print("You loose")

    else:
        print("Something Wrong\nGotta check out")

