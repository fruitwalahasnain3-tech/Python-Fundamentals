marks = [84,75,88,45,90,39]
passed = 0
failed = 0

print(marks)

for marks in marks:
    if marks >=50:
        passed += 1
        # print(f"Marks {passed}. Student is passed successfully.")
    else:
        failed += 1
        # print(f"Marks {failed}. Student is Failed.")

print(f"Total Passed: {passed}")
print(f"Total Failed: {failed}")