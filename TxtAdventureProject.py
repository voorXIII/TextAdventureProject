print("Welcome to the game.\n")

enter = input("Please press Enter to continue.")

name = input("Choose your name.\n")

class Warrior:
    HP = 200
    ATK = 300

class Mage:
    HP = 100
    ATK = 200

class Rouge:
    HP = 150
    ATK = 250

user_class = input("Choose a class between Warrior, Mage, or Rouge.\n")

while(user_class != 'Warrior' and user_class != 'Mage' and user_class != 'Rouge'):
    print("You did not choose from the required classes, try again.")
    user_class = input()

print("You are now ready to play.\n")

enter = input("Please press Enter to continue.\n")

print("You must go to the Dungeon and kill a Skeleton to prove your worth.\n")

class Skeleton
    HP = 100
    ATK = 50


