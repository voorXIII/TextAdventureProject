import random  # Importing random

min_roll = 1   # Min roll value
max_roll = 10  # Max roll value

print("Welcome to the game.\n")  # This welcomes you to the game.

enter = input("Please press Enter to continue.")  # Press the Enter key to continue the game.

name = input("Choose your name.\n")  # Choose the name of your character.


class Warrior:  # The Warrior class values.
    HP = 10
    ATK = 10
    DEF = 10
    Damage = random.randint(1, 10)


class Mage:  # The Mage class values.
    HP = 10
    ATK = 10
    DEF = 5
    Damage = random.randint(1, 10)


class Rogue:  # The Rogue class values.
    HP = 10
    ATK = 10
    DEF = 8
    Damage = random.randint(1, 10)


class Skeleton:
    def __init__(self, Name, HP, ATK, DEF, Damage):
        self.Name = Name
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.Damage = Damage

def attack(attacker, attackee):
    hit = random.randint(min_roll, max_roll) + attacker.ATK

    if (hit > attackee.DEF):
        print("It hits.")
        print(attacker.Name, "inflicts", attacker.Damage)

        attackee.HP = attackee.HP - attacker.Damage

        if attackee.HP <= 0:  # if the attackee's health drops below zero
            print("With one more attack,", attackee.Name, "falls to the floor, dead.")
        else:
            print(attackee.Name, "has", attackee.HP, "HP remaining.")
    else:
        print("You missed.")


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


print("This is your HP.", theClass.HP)  # Tells you your HP value
print("This is your Attack.", theClass.ATK)  # Tells you your Attack value
print("This is your Defense.", theClass.DEF)  # Tells you your Defense value

enter = input("Please press Enter to continue.\n")

print("You are now ready to play.\n")  # Tells the user that they are ready to play the game.

enter = input("Please press Enter to continue.\n") # Press the enter key to continue the game.

print("An old mage tells you to go to the Dungeon and kill a Skeleton to prove your worth.\n")  # NPC tells you to go kill a monster to prove your worth.

skeleton1 = Skeleton("The Skeleton", 10, 4, 5, 5)  # This creates a new Skeleton enemy. The order is the Name, HP, ATK, DEF, and Damage.



