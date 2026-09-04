name = input("Enter your name: ")


marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks! Marks must be between 0 and 100.")

else:
    if marks >= 90 and marks <= 100:
        grade = "A"

    elif marks >= 80 and marks <= 89:
        grade = "B"

    elif marks >= 70 and marks <= 79:
        grade = "C"

    elif marks >= 60 and marks <= 69:
        grade = "D"

    else:
        grade = "F"

    print(f"Hello {name}!")
    print(f"Your marks are {marks}.")
    print(f"Your grade is {grade}.")