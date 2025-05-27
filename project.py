'''
    1 for snake
    -1 for water
    0 for gun 


'''
import random
computer = random.choice([-1,0,1])
youstr = input("Please Enter Your Choice:")

youDict = {"S":1 , "W":-1 , "G":0}
reverseDict = {1:"Snake" , -1:"Water" , 0:"Gun"}
you = youDict[youstr]

print(f"You Choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if(computer==you):
    print("It's a Draw Match")
else:    
    if(computer==-1 and you==1):
        print("Congratulations!!!You won")
    elif(computer==-1 and you==0):
        print("You Lose.Better Luck Next Time!")
    elif(computer==1 and you==-1):
        print("You Lose.Better Luck Next Time!")
    elif(computer==1 and you==0):
        print("Congratulations!!!You won")   

    elif(computer==0 and you==-1):
        print("Congratulations!!!You won") 
    elif(computer==0 and you==1):
        print("You Lose.Better Luck Next Time!")                
    else:
        print("Something Went Wrong!!!")
