symbol = {
    "add": "+",
    "sub": "-",
    "multiply": "*",
    "division": "/"
}
choice = ["+", "-", "*", "/"]

def input_check(input_num):
    while True:
        try:
            return float(input(input_num))
        except ValueError:
            print("Input a number that is a digit!")

num_1 = input_check("Enter the 1st Number: ")

while True:
    operations = input("What do you want to do? (+,-,*,/): ")
    if operations not in choice:
        print("Please choose a correct operation!")
    else:
        break

num_2 = input_check("Enter the 2nd Number: ")

# Calculations
add = num_1 + num_2
sub = num_1 - num_2
multiply = num_1 * num_2

if operations == "+":
    print(f'{num_1} {operations} {num_2} = {add}')
elif operations == "-":
    print(f'{num_1} {operations} {num_2} = {sub}')
elif operations == "*":
    print(f'{num_1} {operations} {num_2} = {multiply}')
else:
    if num_2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        division = num_1 / num_2
        print(f'{num_1} {operations} {num_2} = {division}')