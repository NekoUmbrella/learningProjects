customerList = []
stack = []

customerNum = int(input("How many customers?"))
for i in range(customerNum):
    customerName = input("Enter customer's name. ")
    roomType = input("Enter the room type. ")
    customer = [customerName, roomType]
    customerList.append(customer)


def push_Cust(stack, customerList):
    for i in customerList:
        if i[1] == "deluxe":
            stack.append(customer[0])


def pop_Cust(stack):
    if stack == []:
        print("Underflow")
    else:
        print(stack.pop())


push_Cust(stack, customerList)
print(stack)
