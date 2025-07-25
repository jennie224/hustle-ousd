# -- Functions Activity Jennie Cruz Ramirez ---

# Menu Dictionary
menu = {'Pizza': 2.99, 'Burger': 3.99, 'Hot dog': 1.99, 'Cheese': 0.59, 'Ice cream': 1.49, 'Churro': 0.79, 'Soda': 0.89}

# Total Price of Two Items
def total_price(item1, item2):
    total_sum = menu[item1] + menu[item2]
    return total_sum
print(total_price('Pizza', 'Burger'))
#sentence = f'The total price of {menu['item1']} and {menu['item2']} is {total_sum}"
#print(sentence)


# Next Function
def price_difference(item1, item2):
    total_difference = menu[item1] - menu[item2]
    return abs(total_difference)
print(price_difference('Pizza', 'Burger'))

#Next function
def inflation(item1, multiplier): 
    #inflated_price = menu[item1] * 1.5
    #return inflated_price
   menu.update({item1: menu[item1] * int(multiplier)})
   print(menu)
print(inflation("Churro", 2))

#Last Function
def deflation(item1, divisor):
    menu.update({item1: menu[item1]/int(divisor)})
    print(menu)
print(deflation("Soda", 2))


#My own function
#This function will identify the cost of an item while the restaurant is currently in its happy hours.
def happy_hour(item1):
    discount = menu[item1]/2
    print(f'The price of {item1} is ${discount} during happy hours!')
print(happy_hour('Pizza'))



#teju's lesson
#def greet_student(name):
    #message = ("Hello, " + name + "! Welcome to Week 4.")
    #return message
#print(greet_student("Teju"))
