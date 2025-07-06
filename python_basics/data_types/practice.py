students = ["Faustina","safrina","sai","kim","roze"]
print(students[0])
print(students[(len(students)-1)])
print("Length of the tuple : ",len(students))

student = list(students)
student.append("kishore")
students = tuple(student)
print(students)
print("Ram" in students)
s1,s2,*others = students
student_scores = (("Kishore", 92), ("Ram", 85), ("Priya", 78))
for name , score in student_scores : 
    print(f"{name} scored {score}")