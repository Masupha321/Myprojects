mark = float(input("Enter the students mark:"))
if mark < 50:
    print("Fail")
elif 50 <= mark <= 60:
    print("Average Pass")
elif 61 <= mark <=100:
    print("Pass")
else:
    print("Invalid mark")