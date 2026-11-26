# A. Tuple operations
n = int(input("How many tuple elements?"))
values = tuple(int(input(f"Enter element {i + 1} :"))for i in range (n))
print("Tuple :",values)
print("Maximum:",max(values))
print("Minimum:",min(values))

item = int(input("Enter an element to count: "))
print("Count :",values.count(item))
item = int(input("Enter an element to find index: "))
if item in values:
    print("Index :",values.index(item))
else:
    print("Element not found")

# B. Set operations 
set1 = set(map(int,input("Enter Set 1 integers:" " ").split()))
set2 = set(map(int,input("Enter Set 2 integers: ").split()))
print("Union    :",set1 | set2)
print("Intersection    :",set1 & set2)
print("Difference(S1-S2) :",set1 - set2)
print("Symmetric difference  :",set1 ^ set2)

#C. Employee dictionary operations
employees = {101:"Asha",102:"Ravi"}

emp_id = int(input("Enter new Employee ID: "))
employees[emp_id] = input("Enter employee name: ")

emp_id = int(input("Enter Employee ID to update:" ))
if emp_id in employees:
    employees[emp_id] = input("Enter updated name: ")
else:
    print("Employee ID not found")

emp_id = int(input("Enter Employee ID to delete: "))
if emp_id in employees:
    del employees[emp_id]
else:
    print("Employee ID not found")

emp_id =int(input("Enter Employee ID to search: "))
if emp_id in employees:
    print("Employee name:",employees[emp_id])
else:
    print("Employee not found")

print("Employee records:", employees)