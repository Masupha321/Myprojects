def add(a, b):
    return a + b
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero is not allowed"
    return a / b

def calculator(): #function definition
    while True:
        print("\nSimple Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = int(input("\nEnter your choice (1-5): "))

        match choice:
            case 1:
                num1= float(input("Enter first number: "))
                num2= float(input("Enter second number: "))
                print(f"Result: {add(num1, num2)}") #function call inside function definition   
            case 2:
                num1= float(input("Enter first number: "))
                num2= float(input("Enter second number: "))
                print(f"Result: {subtract(num1, num2)}") #function call inside function definition
            case 3:
                num1= float(input("Enter first number: "))
                num2= float(input("Enter second number: "))
                print(f"Result {multiply(num1, num2)}") #function call inside function definition
            case 4:
                num1= float(input("Enter first number: "))
                num2=float(input("Enter second number: "))
                print(f"Result {divide(num1, num2)}") #function call inside function definition
            case 5:
                print("Exiting...Goodbye!")
                break
            case _:
                print("Invalid choice. Please try between 1 and 5.")

calculator() #function call

            

