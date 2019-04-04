print("Welcome to the game")

name = input("Choose your name\n")
print(name)

class Warrior:
    HP = 200
    ATK = 300
    DEF = 150

class Mage:
    HP = 100
    ATK = 200
    DEF = 0

class Rouge:
    HP = 150
    ATK = 250
    DEF = 100

user_class = input("Choose a class between Warrior, Mage, or Rouge\n")
print(user_class)

while(user_class != 'Warrior' and user_class != 'Mage' and user_class != 'Rouge'):
    print("You did not choose from the required classes, try again")
    user_class = input()


