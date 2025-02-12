num = int(input("Enter the number:"))

if num == 0:
    print("The number is zero, neither positive or negative.")
elif num > 0 and num % 2 == 0:
    print("The number is even and positive.")
elif num < 0 and num % 2 != 0:
    print("The number is odd and negative.")
else:
    print("The number does not match any specific condition")