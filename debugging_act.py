# Debugging Activity Jennie Cruz Ramirez

# Case 1 ------
print("Case 1: ---------")
# Encountered a ZeroDevisionError comes up by dividing by 0, fixed by dividing by 5.
x = 10
y = 5
result = x / y
print("Result:", result)

# Case 2 -----
print("Case 2: ---------")
# Index out of range error, happens when accessing something that is out of range, fixed by changing numbers[i+1] to numbers[i] so the index stays within the valid range of the list.
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
   print(numbers[i])

# Case 3---- 
print("Case 3: ---------")
# Syntax error, happens when ur missing something like for this case we are missing a colon. I fixed it by adding one to (radius):
def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area
radius = 5
print(calculate_area(radius))


# Case 4-----
print("Case 4: ---------")
# Syntax error, happens when ur missing something like for this case we are missing two colons, one after the if condition and one after the else statement. I fixed it by adding both colons.
def is_even(number):
   if number % 2 == 0:
       return True
   else:
       return False
 
print(is_even(4))
print(is_even(7))

# Case 5----
print("Case 5: ---------")
# Syntax error, happens when something is missing in ur code for it to work like in this case its a colon missing. I fixed it by adding one to range(5):
for i in range(5):
   print(i)

# Case 6 ------
print("Case 6: ---------")
# Syntax error, happens when were trying to combine a string with a variable. I fixed it by adding a + to "hello" and name.
def greet(name):
   return "Hello, " + name
 
print(greet("Alice"))

# Case 7 -----
print("Case 7: ---------")
# Indentation error, happens when your code isnt indented to the function. I fixed it by indenting the sum for the for loop.
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number
print("Sum of numbers:", sum)

# Case 8 -----
# Recursion error, the original code factorial(n+1), made n increase and caused infinite recursion, so I fixed it by changing it to factorial(n-1) to make n decrease toward the base case.
print("Case 8: ---------")
def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n-1)
 
print(factorial(5))

# Case 9 -------
print("Case 9: ---------")
# Logical error, happens when something seems right but in reality there is something wrong with the code. I fixed it by removing the or in the "Alice", or "Bob" string and adding a comma instead.
name = input("Enter your name: ")
if name in ("Alice", "Bob"):
   print("Hello, " + name)
else:
   print("Hello, stranger!")

# Case 10 ------
# Zero divison error, happens because we cannot divide by 0. I fixed it by dividing by 2.
print("Case 10: ---------")

def divide_numbers(x, y):
   result = x / y
   return result
 
num1 = 10
num2 = 2
print(divide_numbers(num1, num2))