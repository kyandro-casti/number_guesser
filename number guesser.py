import random

def guess_number():
    answer = random.randint(1, 100)
    print("the number you are seeking lies between 1 and 100")


    try:
        playerguess = int(input("take your guess"))
        if(answer > playerguess):
            print(f"too bad you were too high. the number was {answer}")
        elif(answer < playerguess):
            print(f"too bad you were too low. the number was {answer}")
        else:
            print(f"that's right the number was indeed {answer}")
    except ValueError:
        print("wrong type of input. you don't get to know the number for that")

guess_number()