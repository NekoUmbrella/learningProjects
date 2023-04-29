top = [ "Pepperoni", "Sausage", "Olives", "Bell pepper", "Paneer" ]
crust = [ "Thin Crust", "Neapolitian Style", "New York Style" ]
sauce = [ "Marinara", "White", "Pesto", "Barbequeue" ]
cheese = [ "Mozerella", "Cheddar", "Provolone", "Pecorino-Romano" ]

def listItemSelect(l1):
        for i in range(len(l1)):
            print(i+1, l1[i])
        while True:
            try:
                x = int(input("Choose an item with the number. "))
                val = l1[x-1]
                break
            except IndexError:
                print("Please choose a number from the list!")
        return val

pizzeriaIsOpen = True

def multilIS(n,l1):
     if n == 1:
         val = listItemSelect(l1)
     else: 
         val = []
         m = 0
         while m < n:
             val.append(listItemSelect(l1))
             m += 1
     return val


while pizzeriaIsOpen:
     print("MAKE YOUR OWN PIZZA NIGGER")
     n = int(input("How many toppings"))
     pizza = {
          'Toppings':[n,top],
          'Crust':[1,crust],
          'Sauce':[1, sauce],
          'Cheese':[1, cheese]
     }
     
     for i in pizza.keys():
         pizza[i] = multilIS(pizza[i][0],pizza[i][1])
         print(pizza)

     query = input("Quit? (Y/n)")
     if query in 'Nn':
         break
