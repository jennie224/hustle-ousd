# Lab 3 Jennie Cruz

#Task 1 Working with String
food = "wet burrito" # String Value
print(food[0:3]) # Print First 3 Characters of the String
print(food[-3:]) # Print Last 3 Characters of the String
first_last = food[0] + food[-1] # Combine First and Last character of the String
print(first_last) # 
food_list = food.split() # Split the String into a List of Words
print(food_list)
joined_food = ' '.join(food_list) #Join the lists Back into a Single String
print(joined_food)

# Task 2 Working with Lists
number_list = [1, 2, 3, 4, 5, 6] # A Variable With 6 Integers
number_list.append(89) # Add a New Integer at the End of the List
print(number_list)
number_list.insert(3, 1000) # Add an Element at the 3rd index of the List
print(number_list)
number_list.pop() # Remove the Last Integer from the List
print(number_list)
number_list.remove(number_list[1]) # Remove the Second Integer from the List
print(number_list)
print(number_list[:3]) # List Slicing to Print the FIRST 3 Integers in the List (it can also be like this print(number_list[0:3]) )
print(number_list[-3:]) # List Slicing to Print the LAST 3 Integers in the List 


# Task 3 Working with Dictionaries
books = {'Dr. Seuss': 'Cat in the Hat', 'Tui T. Sutherland': 'Wings of Fire Dragonslayer', 'Mary Pope Osborne': 'Magic Tree House Dinosaurs Before Dark', ' Oxfard University Press': 'Oxfard Atlas of The World'}
# Variable Named Books With 4 Key-value Pairs Containing Author Names as the KEYS and Book Titles as VALUES
print(books.keys()) # Print a List of All the Keys in the Dictionary Only
print(books.values()) # Print a List of All the Values in the Dictionary Only
print(books.get("Mary Pope Osborne")) # Retrieve the Value for a Specific Key in the Dictionary (which means to only print one specific value from the chosen key)
books.pop( 'Mary Pope Osborne') # Method to Remove the 3rd Key-Value Pair from the Dictionary
print(books)
del books["Dr. Seuss"] # Keyword to Remove the 1st Key-Value Pair from the Dictionary
print(books)



