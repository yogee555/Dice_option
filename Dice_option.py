# Dice cricket
# Gaming application which simulates dice cricket where user get a chance to roll a dice and keep scoring
# until rolls gets an option which is deemend to be out.
import random
print("welcome to dice cricket,good luck: )")
dice_option = 0
score = 0
while dice_option !=5:
    user_rolls = input("Please enter R to roll the dice, Q to quite the game: ").upper()
    if user_rolls == 'R':
        dice_option = random.randint(1,6)
        if dice_option !=5:
            score = score+dice_option
            print(f"you scored {dice_option} runs,your currect score is {score}")
        else:
            print(f"sorry,you are declared to out,your final score is {score}")
            break
    elif user_rolls== 'Q':
        print("you have declared to quit the game,see you soon again")
        break
print("**************Game over***********")