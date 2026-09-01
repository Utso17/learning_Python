# x = float(input("What's X? :"))
# y = float(input("what's Y? :"))

# z = x / y

# print((z))

def hello(to = "world"):
    print("Hello,", to)

def main():
    name = input("What's your name? :")
    hello(name)

main()