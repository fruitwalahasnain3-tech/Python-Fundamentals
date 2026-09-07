subjects = ("Python", "Database", "Mathematics")
 
for i in subjects:
    print(subjects.index(i) , i)

for index, subject in enumerate(subjects):
    print(index,subject)
