student_marks = {
    "Python": 85,
    "Database": 72,
    "Mathematics": 91
}

for sub,marks in student_marks.items():
    if marks > 50:
        print(sub,":",marks,"Pass")
    else:
        print(sub,":",marks,"Fail")