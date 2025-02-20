def print_even_numbers():
    for num in range(1, 51):
        if num % 2 == 0:
            print(num)



def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

if __name__ == '__main__':
    numbers = [10, 25, 47, 89, 55, 102, 76]
    print("The largest number is:", find_largest(numbers))


            
