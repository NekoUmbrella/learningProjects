# List of possible options
# Could be made into a dictionary later
top = ["Pepperoni", "Sausage", "Olives", "Bell pepper", "Paneer"]
crust = ["Thin Crust", "Neapolitian Style", "New York Style"]
sauce = ["Marinara", "White", "Pesto", "Barbequeue"]
cheese = ["Mozerella", "Cheddar", "Provolone", "Pecorino-Romano"]


# Prints all items in a numbered list and asks you to choose a value according to the numbers
def numListSoloSelect(l1: list):
    for i in range(len(l1)):
        print(i + 1, l1[i])
    while True:
        try:
            x = int(input("Choose an item with the number. "))
            val = l1[x - 1]
            break
        except IndexError:
            print("Please choose a number from the list!")
    return val


# Returns a variable or a list depending on how many I need
def multiLSS(n: int, l1: list):
    if n == 1:
        val = numListSoloSelect(l1)
    else:
        val = []
        m = 0
        while m < n:
            val.append(numListSoloSelect(l1))
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

    for i, j in pizza.items():
        pizza[i] = multiLSS(j[0], j[1])

    query = input("Quit? (Y/n)")
    if query in "Nn":
        break
