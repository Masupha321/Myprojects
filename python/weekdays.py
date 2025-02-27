def print_day_of_week(day_number):
    match day_number:
        case 1:
            print("The day is Monday")
        case 2:
            print("The day is Tuesday")
        case 3:
            print("The day is Wednesday")
        case 4:
            print("The day is Thursday")
        case 5:
            print("The day is Friday")
        case 6:
            print("The day is Saturday")
        case 7:
            print("The day is Sunday")
        case _:
            print("Invalid input! Please enter a valid number between 1 and 7")
            