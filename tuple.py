# Return a tuple for sorting: first by score (descending), then by name (ascending)

def sort_key(student):
     return (-student[2], student[1])

def sort_students(students):
    return sorted(students, key=sort_key)

students = [
    ("Alice", 22, 95),
    ("Bob", 21, 87),
    ("Charlie", 23, 95),
    ("David", 20, 92),
    ("Eve", 22, 87)
]

sorted_students = sort_students(students)


for name, age, score in sorted_students:
    print(f"Name: {name}, Age: {age}, Score: {score}")