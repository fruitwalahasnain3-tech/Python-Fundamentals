students = (
    ("Hasnain", 85),
    ("Ali", 72),
    ("Ahmed", 91),
    ("Rahul", 45),
    ("Sara", 68)
)


for name,marks in students:
    if marks > 50 :
        print(name,marks,"Pass")
    else:
        print(name,marks,"Fail")


passed = 0
failed = 0
for name, marks in students:
    if marks > 50:
        passed += 1
    else:
        failed += 1

print("Total Passed:", passed)
print("Total Failed:", failed)