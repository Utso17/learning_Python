def get_number():
    x = float(input("Pease enter the 1st number: "))
    y = float(input("Please enter the 2nd number: "))

    return x,y

def add():
    num1 , num2 = get_number()
    z = num1 + num2
    return z

def sub():
    num1, num2 = get_number()
    z = num1 - num2
    return z

def mul1():
    num1, num2 = get_number()
    z = num1 * num2
    return z

def div():
    num1, num2 = get_number()
    z = num1 / num2
    return z

def main():
    a = int(input("Please choose what you want to do?\n" \
                  "1 = Add\n" \
                  "2 = Subtract\n" \
                  "3 = Multiply\n" \
                  "4 = Divide\n" \
                  "Enter choice (1-4): "))

    if a == 1:
        return add()
    elif a == 2:
        return sub()
    elif a == 3:
        return mul()
    elif a == 4:
        return div()
    else:
        return "Wrong input"

result = main()
print("Result is:", result)