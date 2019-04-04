print("Welcome to the game")

name = input("Choose your name\n")
print(name)

user_class = input("Choose a class between Warrior, Mage, or Rouge\n")
print(user_class)
while(user_class is not 'Warrior' or user_class is not 'Mage' or user_class is not 'Rouge'):
    print("You did not choose from the required classes, try again")
    user_class = input()
