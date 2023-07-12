stack = []
employeeList = []

employeeNum = int(input("Enter number of employees"))
for i in range(employeeNum):
    employeeName = input("Enter employee's name.\n")
    employeeNum = input("Enter employee's number.\n")
    employeeSal = int(input("Enter employee's salary.\n"))

    employee = [employeeName, employeeNum, employeeSal]
    employeeList.append(employee)


def pushData(stack, employeeList):
    if employeeList == []:
        print("You have no employees")
    else:
        for employee in employeeList:
            if employee[2] >= 15000:
                stack.append(employee)


pushData(stack, employeeList)
print(stack)
