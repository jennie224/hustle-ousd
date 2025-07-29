# Basic Functions in Python Assignment Jennie Cruz Ramirez

# Step 1 Cat Function
def cat_greeting(word):
    print(f'Cat says {word}')
    print('Cat says nothing')

cat_greeting("meow")

# Step 2
def generate_superhero_power():
    name = "Jennie"
    power = "flying"
    print(f"{name}'s power is {power}")

generate_superhero_power()

# Step 3
def generate_superhero_power1():
    power = "Flying"
    return power
    
print(generate_superhero_power1())

# Step 4
def generate_superhero_power2(user_name, super_power):
    message = user_name + " has the power of " + super_power + "!"
    return message

print(generate_superhero_power2("Jennie", "teleport"))

# Step 5
def cat_greeting_loop():

    greeting = ["meow", "purr", "meiiow", "hiss", "mrrp"]
    for i in greeting:
        print(f'The cat says {i}')

cat_greeting_loop()

# Step 6
def generate_multiple_powers(powers):
    for i in powers:
        print(i)
powers = ["flying", "invisibility", "super strength", "teleportation"]

generate_multiple_powers(powers)
    