import random

while True:
    roll = input(str("Roll the dice (y/n): "))
    roll = roll.lower()
    dice_roll_1 = random.randint(1,6)
    dice_roll_2 = random.randint(1, 6)

    dice_roll = (f'{dice_roll_1}, {dice_roll_2}')

    if roll == "y":
        print(dice_roll)
    elif roll == "n":
        print("Thank you")
        break
    else:
        print("Invalid Choice!")
