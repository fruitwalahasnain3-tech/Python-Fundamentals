student_marks = {
    "Python": 85,
    "Database": 72,
    "Mathematics": 91
}

passed = 0
failed = 0

for sub,marks in student_marks.items():
    if marks > 50:
        passed += 1 
    else:
        failed += 1

print("Passed Subjects: ",passed)
print("Failed Subjects: ",failed)