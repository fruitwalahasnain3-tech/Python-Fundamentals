def student_result(m1,m2,m3):
    total = m1+m2+m3
    print("Total: ",total)
    average = total/3
    print(f"Average: {average:.2f}")
    highest = max(m1,m2,m3)
    print("Highest: ",highest)
    lowest = min(m1,m2,m3)
    print("Lowest: ",lowest)

    return total, average, highest, lowest
   

total, average, highest, lowest = student_result(84,75,91)