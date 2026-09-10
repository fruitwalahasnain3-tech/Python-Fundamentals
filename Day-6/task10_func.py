def student_result():
    marks = [85, 72, 91, 45, 68]
    total = (sum(marks))
    print("Total:",total)
    avg = sum(marks)/len(marks)
    print("Average:",avg)
    high = max(marks)
    print("Highest:",high)
    low = min(marks)
    print("Lowest:",low)
    passed = 0
    failed = 0
    for mark in marks:
        if mark >=50:
            passed += 1
        else:
            failed += 1
    print("Passed Students: " , passed)
    print("Failed Student: " , failed)
        
    return total, avg, high, low, passed, failed
total,avg,high,low, passed, failed = student_result()