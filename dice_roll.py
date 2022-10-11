import random

def roll_dice():
    min_val = 1
    max_val = 6

    roll_again = "yes"

    while roll_again == "yes" or roll_again == "y":
        print("Rolling The Dices...")
        print("The Values are :")
        
        #generating and printing 1st random integer from 1 to 6

        result = random.randint(min_val, max_val)
        if result==6:
            print("Hurray!its a six!!")
        else:
            print(result)
        
        
        roll_again = input("Roll the Dices Again?") 

if __name__=="__main__":
    roll_dice()