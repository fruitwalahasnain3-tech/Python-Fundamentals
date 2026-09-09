students = {
    "Hasnain": 85,
    "Ali": 45,
    "Ahmed": 91,
    "Rahul": 38,
    "Sara": 68
}

for name,marks in students.items():
    print(name,":",marks)

print("\n","---Pass/Fail---")
for name,marks in students.items():
    if marks > 50:
        print(name,":",marks,"Pass")
    else:
        print(name,":",marks,"Fail")

print("\n","---Count---")
passed = 0
failed = 0

for marks in students.values():
    if marks > 50:
        passed += 1
    else:
        failed += 1

print("Passed subjects: " , passed)
print("Failed subjects: " , failed)


print("\n","---Heigest/Lowest---")
print("Highest marks: ",max(students.values()))
print("Lowest marks",min(students.values()))