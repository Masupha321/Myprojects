def calculate_average(num1, num2, num3, num4):
    return (num1 + num2 + num3 + num4) / 4
def main():
    try:
        num1 = float(input("Enter the first number"))
        num2 = float(input("Enter the second number"))
        num3 = float(input("Enter the third number"))
        num4 = float(input("Enter the fourth number"))

        average = calculate_average(num1, num2, num3, num4)
        print(f"The average of the numbers is:, {average}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

    if __name__ == "__main__":
        main()
        
