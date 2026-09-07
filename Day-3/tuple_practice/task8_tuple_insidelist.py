students = [
    ("Hasnain", 85),
    ("Ali", 72),
    ("Ahmed", 91)
]
# method1
# name0 , marks0 = students[0]
# name1 , marks1 = students[1]
# name2 , marks2 = students[2]
# print(name0,marks0)
# print(name1,marks1)
# print(name2,marks2)

# method2
for name,marks in students:
    print(name,marks)