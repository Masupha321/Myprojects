# def print_numbers_skip_multiples_of_7():
#    for i in range(1, 51):     
#         if i % 7 == 0:
#             continue
#         print(i)

def print_numbers(): # function definition
    for masupha in range(1, 51):
        if masupha % 7 == 0:
            continue
        if masupha % 2 == 0:
          print(masupha)

print_numbers() # function call 