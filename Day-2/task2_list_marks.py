marks = [85, 72, 91, 66, 78]

print("List", marks)
print("First Marks ", marks[0])
print("Last Marks",marks[-1])
marks.append(55)
print("Add a new mark " , marks)
marks.remove(91)
print("Remove one mark " , marks)
print("Total marks",sum(marks))
print("Average Marks: " , sum(marks) / len(marks))