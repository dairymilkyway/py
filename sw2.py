name = input("Enter your name: ")
age = float(input("Enter your age: "))
grade1 = float(input("Input Grade1 "))
grade2 = float(input("Input Grade2 "))
grade3 = float(input("Input Grade3 "))

average = (grade1 + grade2 + grade3) / 3

if average >= 75:
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Your average grade is: {average}")
    print(f"Remarks : Passed")
else:
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Your average grade is: {average}")
    print(f"Remarks : Failed")

