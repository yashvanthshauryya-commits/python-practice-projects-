students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

marks = []

for i in range(students):
    row = []
    print("\nStudent", i + 1)

    for j in range(subjects):
        m = int(input("Enter marks: "))
        row.append(m)

    marks.append(row)

print("\nStudent Marks Matrix:")

for row in marks:
    print(row)

print("\nStudent Averages:")

for i in range(students):
    total = 0

    for j in range(subjects):
        total += marks[i][j]

    avg = total / subjects
    print("Student", i + 1, "Average:", avg)

print("\nSubject Averages:")

for j in range(subjects):
    total = 0

    for i in range(students):
        total += marks[i][j]

    avg = total / students
    print("Subject", j + 1, "Average:", avg)

top = 0

for i in range(students):
    total = 0

    for j in range(subjects):
        total += marks[i][j]

    if total > top:
        top = total
        topper = i + 1

print("\nTop Performer: Student", topper)
print("Total Marks:", top)