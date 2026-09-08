import random

random_number = random.randint(1, 100)

while True:
    user_input = input("Enter a number between 1-100: ")

    try:
        gussed_number = int(user_input)
    except ValueError:
        print("please enter a valid Number")
        continue

    if gussed_number < 1 or gussed_number > 100:
        print("Number must be between 1-100")
        continue

    if random_number < gussed_number:
        print("Too High!")
    elif random_number > gussed_number:
        print("Too Low!")
    else:
        print("Congrats you gussed the correct number!!")
        break