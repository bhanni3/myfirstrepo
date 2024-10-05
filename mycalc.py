def add(num1, num2):
    return num1 + num2 

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    return num1 / num2

def multiply(num1, num2):
    return num1 * num2

while True:
    print("Welcome to the My Calc🙈")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice in ('1', '2', '3','4'):
        num1 = float(input("Enter the first number :"))
        num2 = float(input("Enter the second number: "))
    
    if choice == '1':
       print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2' :
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3' :
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4' :
        print(num1, "/", num2, "=", divide(num1, num2))
    else :
        print("Invaid choice!:(") 

    continue_or_exit = input("Do you want to continue? (Y/N):")       
    if continue_or_exit.lower() != 'y':
        break 
