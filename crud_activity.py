# CRUD Activity by Jennie Cruz Ramirez

# Step 1: Create an empty list
cookbook = []

# Step 2: Add a recipe
def create(recipe):
    cookbook.append(recipe)

# Step 3: Read a recipe
def read(index):
    if index < len(cookbook):
        return cookbook[index]
    else:
        print("Please pick an index within the range")
        read(index)

# Step 4: Update a recipe
def update(index, recipe):
    if index >= 0 and index < len(cookbook):
        old_recipe = cookbook[index]
        cookbook[index] = recipe
        print("Updated recipe at index " + str(index) + " from " + old_recipe + " to " + recipe + ".")
    else:
        print("Please pick an index within the range.")

# Step 5: Delete a recipe
def destroy(index):
    if index >= 0 and index < len(cookbook):
        removed = cookbook.pop(index)
        print("Removed recipe: " + removed)
    else:
        print("Please pick an index within the range.")

# Step 6: Show all recipes
def list_all_recipes():
    if len(cookbook) == 0:
        print("Your cookbook is empty.")
    else:
        print("Here are your recipes:")
        for i in range(len(cookbook)):
            print(str(i) + ". " + cookbook[i])

# Step 7: Run the menu
def main():
    while True:
        print("\nCookbook Menu")
        print("1. Add a Recipe")
        print("2. Read a Recipe")
        print("3. Update a Recipe")
        print("4. Delete a Recipe")
        print("5. Display All Recipes")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            recipe = input("Enter the name of the recipe: ")
            create(recipe)
        elif choice == "2":
            index = input("Enter the index of the recipe to read: ")
            if index.isdigit():
                read(int(index))
            else:
                print("Please enter a number.")
        elif choice == "3":
            index = input("Enter the index of the recipe to update: ")
            recipe = input("Enter the new recipe name: ")
            if index.isdigit():
                update(int(index), recipe)
            else:
                print("Please enter a number.")
        elif choice == "4":
            index = input("Enter the index of the recipe to delete: ")
            if index.isdigit():
                destroy(int(index))
            else:
                print("Please enter a number.")
        elif choice == "5":
            list_all_recipes()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1–6.")

# Start the app
main()