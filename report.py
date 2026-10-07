import matplotlib.pyplot as plt
students=[{"name": "Alice","marks": 90},{"name": "Bob","marks": 30},{"name": "Charlie","marks": 95},{"name": "David","marks": 76},{"name": "Eve","marks": 40}  ]
def average_marks(students):
    total_marks = 0
    for student in students:
        total_marks += int(student["marks"])
    average = total_marks / len(students)
    return average

for student in students:
    if(student["marks"]>40):
        print(student["name"],"has passed the exam")
    else:
        print(student["name"],"has failed the exam")

student_names = [student["name"] for student in students]
student_marks = [int(student["marks"]) for student in students]

plt.bar(student_names, student_marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Performance")
plt.show()