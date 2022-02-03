#Grade Sorter APP
#initialise list and get user's input 

grades = []

grade = int(input("Enter your first grade here: "))
grades.append(grade)

grade = int(input("Enter your second Grade here: "))
grades.append(grade)

grade = int(input("Enter your Third Grade here: "))
grades.append(grade)

grade = int(input("Enter your Last Grade here: "))
grades.append(grade)

#Display What the user entered 
print()
# print("your grades entered are " + str(grades))
print(f"your grades entered are {grades}")

#sort grades from highest to Lowest 
#grades.sort() will sort from lowest to highest 
#reverst = True sorts the opposite 
grades.sort()

print("Sorting Grades from hghest to Lowest...")
print(f"Sorted! --- {grades}")


