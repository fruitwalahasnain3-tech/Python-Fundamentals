students = {"Hasnain", "Ali", "Ahmed", "Rahul", "Sara"}
passed = {"Hasnain", "Ahmed", "Sara"}

print(students)
print(passed)

fail = students.difference(passed)
print("Failed  Student: ", fail)

totalStu = len(students)
print("Total Student: ",totalStu)

totalPassed = len(passed)
print("Total Student Passed: ",totalPassed)

print("Total Student Failed: ",len(fail))