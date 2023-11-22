def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        return "cannot divide by 0"
    return x / y

while True:
    print("options:")
    print("enter 'add' for addition")
    print("enter 'subtract' for subtract") 
    print("enter 'multiply' for multiply")
    print("enter 'divide' for divide")  
    print("enter 'quit to exit")

    user_input = input(":")
    if user_input == "quit":
        break
    elif user_input in ("add","subtract","multiply","divide"):
        num1 = float(input("enter 1st number: "))
        num2 = float(input("enter 2nd number: "))

        if user_input == "add":
            print("result:", add(num1,num2))
        if user_input == "subtract":
            print("result:", subtract(num1,num2))
        if user_input == "multiply":
            print("result:", multiply(num1,num2))
        if user_input == "divide":
            print("result:", divide(num1,num2))
    else:
            print("invalid input")