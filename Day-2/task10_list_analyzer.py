marks = [84, 72, 91, 45, 67, 38, 95]

print(marks)

total = sum(marks)
print("Total Marks: ", total)

avg = sum(marks)/len(marks)
print(f"Average Marks:{avg:.2f}")

high = max(marks)
print(f"Highest Marks: ", high)

low = min(marks)
print("Lowest Marks: ",low)

passed = 0
failed = 0

for mark in marks:
    if mark >=50 :
        passed += 1
    else:
        failed += 1

print("Passed Students:", passed)
print("Failed Students:", failed)

marks.sort()
print("Sorted Marks: ", marks)

marks.reverse()
print("Reversed marks: ", marks)
