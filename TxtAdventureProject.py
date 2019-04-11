import random  # Importing random
min_roll = 1  # Min roll value
max_roll = 10 # Max roll value


def attack(attacker,attackee):  # Attack function
    hit = random.randint(min_roll,max_roll)
     if(hit + ):
         print("The attack hits")
     else(hit < 10):
        print("The attack misses")


print("Welcome to the game.\n")  # This welcomes you to the game.

enter = input("Please press Enter to continue.")  # Press the Enter key to continue the game.

name = input("Choose your name.\n")  # Choose the name of your character.


class Warrior:  # The Warrior class values.
    HP = 10
    ATK = 10
    DEF = 10

class Mage:  # The Mage class values.
    HP = 10
    ATK = 10
    DEF = 5

class Rogue:  # The Rogue class values.
    HP = 10
    ATK = 10
    DEF = 8


user_class = input("Choose a class between Warrior, Mage, or Rogue.\n")   # Input what class you want to be.

while(user_class != 'Warrior' and user_class != 'Mage' and user_class != 'Rogue'):  # If you input another class other than the 3 specified, it gives that print statement and re-runs the class input.
    print("You did not choose from the required classes, try again.")
    user_class = input()

if user_class.lower() == 'warrior':  # Sets the user input to the class
    theClass = Warrior()
elif user_class.lower() == 'mage':
    theClass = Mage()
elif user_class.lower() == 'rogue':
    theClass = Rogue()
else:
    print("Something's wrong.")
    exit()


print("You are now ready to play.\n")  # Tells the user that they are ready to play the game.

enter = input("Please press Enter to continue.\n") # Press the enter key to continue the game.

print("You must go to the Dungeon and kill a Skeleton to prove your worth.\n")  # NPC tells you to go kill a monster to prove your worth.


class Skeleton:  # The Skeleton class values.
    HP = 10
    ATK = 10
    DEF = 0

