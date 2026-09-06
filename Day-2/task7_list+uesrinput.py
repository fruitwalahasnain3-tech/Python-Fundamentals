marks = []

for i in range(5):
    mark = int(input("Enter Marks: "))
    marks.append(mark)

print(marks)

total = sum(marks)
print("Total Marks: ",total)

avg = sum(marks)/len(marks)
print("Average Marks: ",avg)

maximum = max(marks)
print("Maximum Marks: ",maximum)

minimum = min(marks)
print("Minimum Marks: ",minimum)

passed = 0
failed = 0

for mark in marks:
    if mark >= 50:
        passed += 1
    else:
        failed += 1
print(f"Total Passed {passed}")
print(f"Total failed {failed}")
