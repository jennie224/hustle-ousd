# Lab: Practice with Loops by Jennie Cruz Ramirez

# Task 1: Voting Eligibility Checker
def voting_eligibility():
    checking = "yes"
    while checking.lower() == "yes":
        age = int(input("What is your age: "))
        if age >= 18:
            print("Yes, you can vote.")
        else:
            print("You can't vote.")
        checking = input("Would you like to check another age? (yes/no): ")

# Task 2: Number Positivity/Negativity Checker
def number_check():
    list1 = [3, -1, 0, 6, -4]
    for x in list1:
        if x > 0:
            print(f"{x} is positive.")
        elif x < 0:
            print(f"{x} is negative.")
        else:
            print(f"{x} is zero.")

# Task 3: Minecraft Inventory Checker
def minecraft_blocks():
    inventory = ["coal", "dirt", "gravel", "diamond", "stone"]
    for block in inventory:
        print(f"You found a {block} block!")
        if block == "diamond":
            print("Jackpot!")

# === Main Program ===
print("Which task would you like to run?")
print("1 - Voting Eligibility Checker")
print("2 - Number Positivity/Negativity Checker")
print("3 - Minecraft Inventory Checker")

choice = input("Enter 1, 2, or 3: ")

if choice == "1":
    voting_eligibility()
elif choice == "2":
    number_check()
elif choice == "3":
    minecraft_blocks()
else:
    print("Invalid choice.")