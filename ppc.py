print("======================================")
print(" PERSONAL POCKET CGPA CALCULATOR")
print("======================================")

grade_points = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 0
}

total_grade_points = 0
total_course_units = 0

number_of_courses = int(input("Enter the number of courses: "))

for i in range(number_of_courses):

    print(f"\nCourse {i + 1}")

    course_unit = int(input("Enter Course Unit: "))
    grade = input("Enter Grade (A-F): ").upper()

    if grade in grade_points:
        total_grade_points += grade_points[grade] * course_unit
        total_course_units += course_unit
    else:
        print("Invalid grade entered.")

cgpa = total_grade_points / total_course_units

print("\n==============================")
print("Total Course Units:", total_course_units)
print("Total Grade Points:", total_grade_points)
print("CGPA:", round(cgpa, 2))

if cgpa >= 4.50:
    print("Class of Degree: First Class")
elif cgpa >= 3.50:
    print("Class of Degree: Second Class Upper")
elif cgpa >= 2.40:
    print("Class of Degree: Second Class Lower")
elif cgpa >= 1.50:
    print("Class of Degree: Third Class")
else:
    print("Class of Degree: Pass")
