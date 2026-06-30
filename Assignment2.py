students_info = {
    "Aarav": {"age": 20, "major": "Computer Science", "gpa": 3.8},
    "Bhavya": {"age": 22, "major": "Mathematics", "gpa": 3.4},
    "Chirag": {"age": 19, "major": "Physics", "gpa": 3.9},
    "Divya": {"age": 21, "major": "Biology", "gpa": 3.7},
    "Esha": {"age": 23, "major": "Chemistry", "gpa": 3.5}
}

#1. What is Aarav's major? Write the Python code to get it.
print("\n1.Aarav's major is:", students_info["Aarav"]["major"])

# 2. How old is Chirag? Write the Python code to find his age.
print("\n2.Chirag's Age is:", students_info["Chirag"]["age"])

# 3. Get Bhavya's GPA using Python.
print(f"\n3.Bhavya's GPA is {students_info['Bhavya']['gpa']}")
## Can't use double quotes to call "Bhavya" and "gpa" here because of f string. Reason: It won't know where to end the f string.

# 4. Add a new student "Farhan" with age 24, major "Engineering", and GPA 3.6.
print(f"\n4.Before Addition : {students_info}")
students_info["Farhan"]={"age":24, "major": "Engineering", "gpa":3.6}
print(f"\nAfter Addition : {students_info}")

# 5. Update Divya's GPA to 3.9.
print(f"\n5.Before Change : {students_info['Divya']}")
students_info["Divya"]["gpa"]=3.9
print(f"\nAfter Change : {students_info['Divya']}")

# 6. Write Python code to list all the student names.
#Method1
for i in students_info:
    print(f"\n {i}")

#Method2
print(f"\n {students_info.keys()}")

# 7. Write Python code to find the average GPA of all students.
#Method1
s = 0
for i in students_info:
    s = s + students_info[i]["gpa"]
print(f"The average is: {s/len(students_info)}")

#Method2
avg = sum(i["gpa"] for i in students_info.values())/len(students_info)
print(avg)

# 8. Remove Esha from the dictionary.
r = students_info.pop("Esha")
print(f"Removed entry : {r}")


# 9. Check if "Gaurav" is in the dictionary.
print("Gaurav is present in students info dict" if "Gaurav" in students_info.values() else "Gaurav is NOT present in students info dict")