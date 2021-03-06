import random  # Importing random

min_roll = 1   # Min roll value
max_roll = 10  # Max roll value


class Warrior:  # The Warrior class values.
    Name = "warrior"
    HP = 10
    ATK = 10
    DEF = 10
    Damage = random.randint(1, 10)


class Mage:  # The Mage class values.
    Name = "mage"
    HP = 10
    ATK = 10
    DEF = 5
    Damage = random.randint(1, 10)


class Rogue:  # The Rogue class values.
    Name = "rogue"
    HP = 10
    ATK = 10
    DEF = 8
    Damage = random.randint(1, 10)


class Enemy:
    def __init__(self, Name, HP, ATK, DEF, Damage):
        self.Name = Name
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.Damage = Damage


def attack(attacker, attackee):  # The attack function
    hit = random.randint(min_roll, max_roll) + attacker.ATK
    death = 0

    if (hit > attackee.DEF):
        print(attacker.Name, "inflicts", attacker.Damage)

        attackee.HP = attackee.HP - attacker.Damage

        if attackee.HP <= 0:  # if the attackee's health drops below zero
            print("With a forceful attack,", attackee.Name, "dies.")
            death = 1

        else:
            print(attackee.Name, "has", attackee.HP, "HP remaining.")
            death = 0

    else:
        print(attacker.Name, "missed!")

    return death


def fight(player, enemy):# The attack loop
    death = 0

    while death  == 0:

        if death == 0:  # Player attacks the enemy
            death = attack(player, enemy)

        if death == 0:  # Enemy attacks player
            death = attack(enemy, player)

            if death == 1:  # If the player dies, do this.
                print("You're dead")
                death = 1
                player_death = 1
            else:
                player_death = 0

        else:  # If the enemy dies, do this
            print("The enemy is dead")
            death = 1
            player_death = 0

    return player_death


def buff(player):  # Function for buffing the player
    print("\nYou've leveled up!")
    player.HP = player.HP + 10  # Increases player HP by 5
    player.ATK = player.ATK + 10  # Increases player Attack by 5
    player.DEF = player.DEF + 10  # Increases player Defense by 5

    print("HP", player.HP)
    print("Attack", player.ATK)
    print("Defense", player.DEF, "\n\n")


print("Welcome to the game.\n")  # This welcomes you to the game.

enter = input("Please press Enter to continue.")  # Press the Enter key to continue the game.

name = input("Choose your name.\n")  # Choose the name of your character.

answer = 'y'
while answer == 'y':  # Death loop to start over if you die.
    death = 0

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

    enter = input("Please press Enter to continue.\n")  # Press the enter key to continue the game.

    print("An old mage tells you to go to the Dungeon and kill a Skeleton to prove your worth.\n")  # NPC tells you to go kill a monster to prove your worth.

    enter = input("Please press Enter to continue.\n")

    if death == 0:
        skeleton1 = Enemy("The Skeleton", 10, 5, 5, 5)  # This creates a new Skeleton enemy. The order is the Name, HP, ATK, DEF, and Damage.
        death = fight(theClass, skeleton1)

    if death == 0:
        buff(theClass)  # This calls the buff function to give the player a level up (of sorts)

    if death == 0:
        goblin1 = Enemy("The Goblin", 20, 15, 10, 10)  # This creates a new Goblin enemy. The order is the Name, HP, ATK, DEF, and Damage.
        death = fight(theClass, goblin1)

    if death == 0:
        buff(theClass)

    if death == 0:
        boss1 = Enemy("The Boss", 30, 20, 20, 15)
        death = fight(theClass, boss1)

    if death == 1:
        print("You died")

    else:
        print("You won!")

    print("Would you like to play again?")
    answer = input()
