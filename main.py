## We all have played snake, water, gun game in our childhood.
# If you haven't google the rules of this game and write a python program capable of playing this game with the user.
'''
1 for snake
-1 for  water
0 for gun
'''
# computer = -1
import random
computer = random.choice([-1, 0, 1]) 
youstr = input("Enter your choice: ")
youDict = {"s":1, "w":-1, "g":0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]


# print(f"You chose {youDict[you]}\n Computer chose{reverseDict[comouter]}")
print(f"You chose {reverseDict[you]}\n Computer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw!")
else:
    if((computer-you)==-1 or (computer-you)==2):
        print("You lose!")
    else:
        print("You win!")

#     if(computer ==-1 and you==1):
#         print("You win!")

#     elif(computer ==-1 and you==0):
#         print("You lose!")

#     elif(computer==1 and you==-1):
#         print("You lose!")

#     elif(computer==1 and you==0):
#         print("You win")

#     elif(computer==0 and you==-1):
#         print("You win!")

#     elif(computer==0 and you==1):
#         print("You lose!")

#     else:
#         print("Something went wrong!")
    









 