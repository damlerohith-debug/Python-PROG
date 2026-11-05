n = int(input("Enter the number of students:")) 
for i in range (1, n+1):
    usn = input("Enter usn:")
    name = input("Enter students name:")
    marks1 = int(input("Enter marks1:"))
    marks2 = int(input("Enter marks2:"))
    marks3 = int(input("Enter marks3:"))
    Total = marks1 + marks2 + marks3
    Average = (marks1 + marks2 + marks3)/3
    print("students name=",name)
    print("usn=",usn)
    print("marks1=",marks1)
    print("marks2=",marks2)
    print("marks2=",marks3)
    print("Total=",Total)
    print("Average=",Average)