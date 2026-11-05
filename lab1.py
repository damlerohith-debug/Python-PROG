students = []
n = int(input("Enter the number of students:"))
for i in range(n):
    print(f"\Enter details of student{i+1}")
    name = input("Enter the students name:")
    usn = input("Enter the usn:")
    mark1 = float(input("Enter the marks in Course 1:"))
    mark2 = float(input("Enter the marks in Course 2:"))
    mark3 = float(input("Enter the marks in course 3:"))
    total = mark1+mark2+mark3
    average = total/3
    students.append([name,usn,mark1,mark2,mark3,total,average])
print("\n"+"="*94)
print("STUDENT MARKS REPORT")
print("="*94)
print(f"{'Name':<15}{'usn':<15}{'Course 1':>10}"
      f"{'Course 2':>10}{'Course 3':>10}"
      f"{'Total':>10}{'Average':>10}")
print("="*94)

for student in students:
    name,usn,course1,course2,course3,total,average = student
    print(f"{name:<15}{usn:<15}{course1:>10.2f}"
          f"{course2:>10.2f}{course3:>10.2f}"
          f"{total:>10.2f}{average:>10.2f}")
print("="*94)
