import random

emoji = {
    "p": "📃",
    "r": "🪨",
    "s": "✂️",
}
choice = ["r", "p", "s"]

while True:

    computer_choice = random.choice(choice)
    user_input = input("What do you want to play? (r/p/s): ").lower()

    if user_input not in choice:
        print("invalid input")
        continue

    print(f'Computer choosed: {emoji[computer_choice]}')
    print(f'You choosed: {emoji[user_input]}')

    if user_input == computer_choice:
        print("It's a tie!")
    elif \
            user_input == 'p' and computer_choice == 'r' or \
            user_input == 's' and computer_choice == 'p' or \
            user_input == 'r' and computer_choice == 's':

        print("You win!")
    else:
        print("you lose!")

    while True:

        ask = input("Do you want to continue? (y/n): ").lower()
        if ask in ["y", "n"]:
            break
        print("Please enter (y/n)")

    if ask == "n":
        break
