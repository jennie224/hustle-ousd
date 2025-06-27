# -- Functions Activity Made by Jennie Cruz Ramirez ---

# Step 1 : Menu Dictionary
menu = {'Pizza': 2.99, 'Burger': 3.99, 'Hot dog': 1.99, 'Cheese': 0.59, 'Ice cream': 1.49, 'Churro': 0.79, 'Soda': 0.89}

# Step 2: Total Price of Two or More Items
def total_price(*items):
    total = 0
    missing = []
    for item in items:
        if item in menu:
            total += menu[item]
        else:
            missing.append(item)
    if missing:
        return f"Error: {', '.join(missing)} not found in menu."
    item_list = ', '.join(items)
    return f"The total price of {item_list} is {total:.2f}"

# Step 3: Price Difference
def price_difference(item1, item2):
    if item1 not in menu or item2 not in menu:
        return f"Error: One or both items not found in menu."
    diff = abs(menu[item1] - menu[item2])
    return f"The difference between {item1} and {item2} is {diff:.2f}"

# Step 4: Inflation (increase price)
def inflation(item, multiplier):
    if item not in menu:
        return f"Error: {item} not found in menu."
    menu[item] *= multiplier
    return menu

# Step 5: Deflation (decrease price)
def deflation(item, divisor):
    if item not in menu:
        return f"Error: {item} not found in menu."
    if divisor == 0:
        return "Error: Cannot divide by zero."
    menu[item] /= divisor
    return menu

# Step 6: Unique Function

def boost_prices(power):
    for item in menu:
        menu[item] = round(menu[item] ** power, 2)
    return menu


print(total_price("Pizza", "Soda"))
print(total_price("Pizza", "Cake"))  # Should show error for Cake
print(price_difference("Burger", "Cheese"))
print(price_difference("Burger", "Cake"))  # Should show error
print(inflation("Churro", 2))
print(deflation("Soda", 2))
print(boost_prices(2))  # Squares every price