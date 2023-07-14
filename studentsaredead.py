def studentProfiler(ordinal):
    name = input("Enter " + str(ordinal) + " student's name.")
    grade = input("Enter " + str(ordinal) + " student's grade.")
    section = input("Enter " + str(ordinal) + " student's section.")
    rollno = input("Enter " + str(ordinal) + " student's roll number.")

    return [name, grade, section, rollno]


j = [1, 2, 3]


def ordinalStudentAdder():
    studentList = []
    studentNum = int(input("Enter number of total students."))
    n = 0
    ordinals = ["1st", "2nd", "3rd"]

    while n < studentNum:
        onesPlace = n % 10
        if onesPlace < 3:
            p = ordinals[onesPlace]
            studentList.append(studentProfiler(p))
            n += 1
        elif onesPlace >= 3:
            tempOrdinal = str(onesPlace + 1) + "th"
            studentList.append(studentProfiler(tempOrdinal))
            n += 1

    print(studentList)


ordinalStudentAdder()
