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
grades.sort(reverse = True)

print("Sorting Grades from hghest to Lowest...")
print(f"Sorted! --- {grades}")

print()
#remove the two lowest grade now.
# grade.pop will remove the last grade
# grade.pop(3) will also do same bcos of index 
firstDropped = grades.pop()
secondDropped = grades.pop(2)
print(f"Your first grade dropped is {firstDropped}")
print(f"Your second grade dropped is {secondDropped}")

#Output the remaining grades to the user 
print("Your grades left are: " + str(grades))

#Inform the user his highest grade 
print("Your highest grade is " + str(grades[0]) + "\n")

'''Another way to do line 35 is this below, doing it twice: 
firstDropped = grades.pop()
print("Your first removed grade is: " + str(firstDropped))
secondDropped = grades.pop()
print("Your second removed grade is: " + str(secondDropped))
'''
