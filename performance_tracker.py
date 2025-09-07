class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        return sum(self.marks) / len(self.marks)
students = []
n = int(input("Enter number of students: "))

for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    marks = list(map(int, input(f"Enter marks of {name}: ").split()))
    students.append(Student(name, marks))

averages = {s.name: round(s.average(), 2) for s in students}
top_student = max(students, key=lambda s: s.average()).name
print("Average Marks:", averages)
print("Top Performer:", top_student)
