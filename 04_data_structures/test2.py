students = ["Dev", "Rahul", "Aman"]

#Adding "Priya"

students.append("Priya")
print(students)

#insert "neha" at index 1

students.insert(1, 'Neha')
print(students)

#Remove Rahul

students.remove("Rahul")  #Here I make a mistake I give here Index
print(students)

#count how many times dev appears

student = ["Dev", "Rahul", "Riya", "Dev", "Gaurav", "Dev"]
print(student.count("Dev")) #Here I forget s

#sort the list

list = [9, 7, 8, 5, 3, 5, 6, 4, 2, 1, 0]

list.sort()
print(list)

# reverse the list

list.sort(reverse=True)
print(list)

#make a copy in new_student

new_student = students.copy()
new_student.append("Riya")

print(new_student)

# Print both list

print(students)
print(new_student)

