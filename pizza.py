# List of possible options
# Could be made into a dictionary later
top = ["Pepperoni", "Sausage", "Olives", "Bell pepper", "Paneer"]
crust = ["Thin Crust", "Neapolitian Style", "New York Style"]
sauce = ["Marinara", "Bechamel", "Pesto", "Barbequeue"]
cheese = ["Mozerella", "Cheddar", "Provolone", "Pecorino-Romano"]


def numberedItemSelect(itemList):
    """
    Prints a numbered list and returns one item
    depending on the number you have entered.
    """
    for itemIndex in range(len(itemList)):
        print(itemIndex + 1, itemList[itemIndex])
    while True:
        try:
            inputIndex = int(input("Choose an item with the number. "))
            item = itemList[inputIndex - 1]
            break
        except IndexError:
            print("Please choose a number from the list!")
    return item


# Returns a variable or a list depending on how many I need
def multipleSelect(n: int, itemList):
    """
    Select single/multiple elements from a given list.
    """
    if n == 1:
        val = numberedItemSelect(itemList)
    else:
        val = []
        m = 0
        while m < n:
            val.append(numberedItemSelect(itemList))
            m += 1
    return val


pizzeriaIsOpen = True

while pizzeriaIsOpen:
    print("MAKE YOUR OWN PIZZA nig—")

    # Set up for multiLIS with numbers and lists
    n = int(input("How many toppings"))
    pizza = {
        "Toppings": [n, top],
        "Crust": [1, crust],
        "Sauce": [1, sauce],
        "Cheese": [1, cheese],
    }

    for components, setupList in pizza.items():
        numItems = setupList[0]
        itemsList = setupList[1]
        pizza[components] = multipleSelect(int(numItems), itemsList)

    print(pizza)

    query = input("Quit? (Y/n)")
    if query in "yY":
        pizzeriaIsOpen = False
