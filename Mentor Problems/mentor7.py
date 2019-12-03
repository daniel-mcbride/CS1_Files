def class_average():
    gradesList = []
    numStudents = 10

    while len(gradesList) < numStudents:
        studentGrade = input("Please input a grade: ")        
        print("Enter EXIT to quit the program")
        
        if studentGrade.lower() == "exit":
            break
        else:
            studentGrade = int(studentGrade)
            if studentGrade >= 0 and studentGrade <= 100:
                gradesList.append(studentGrade)
            else:
                print("Invalid grade")

    classTotal = 0
    
    for grade in gradesList:
        classTotal += grade
    
    classAverage = classTotal / numStudents

    if classAverage >= 70:
        return "passed"
    else:
        return "failed"

print(class_average())
