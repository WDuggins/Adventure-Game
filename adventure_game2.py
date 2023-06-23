import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


def intro(items, creature, who):
    print_pause("You find yourself standing in an open field, \n"
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + who + " is somewhere around here, \n"
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("All you have is a rusty old dagger.")


def house(items, creature, who):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens\n"
                "and out steps a " + who + ".")
    print_pause("Eep! This is the " + who + "'s house!")
    print_pause("The " + who + " attacks you!")
    fight_run(items, creature, who)


def fight_run(items, creature, who):
    action = input("Would you like to (1) fight, or (2) run away?\n").lower()
    if action == "1":
        if "sword" in items:
            print_pause("As the " + who + " moves to attack,\n"
                        "you unsheath your new sword.")
            print_pause("The Sword of Olympus gleams with power\n"
                        "as you brace yourself for the attack.")
            print_pause("The " + who + " knows he is\n"
                        "no match for you and takes off.")
            print_pause("You have rid the village of the evil " + who + ".\n"
                        "You are victorious!")
            play_again(items, creature, who)
        else:
            print_pause("You do your best...")
            print_pause("but your dagger is no match for\n"
                        "the wicked " + who + ".")
            print_pause("You have been defeated!")
            play_again(items, creature, who)
    elif action == "2":
        print_pause("You scream and run back out to the field.")
        direction(items, creature, who)
    else:
        print_pause("Sorry, that is not an option.")
        fight_run(items, creature, who)


def cave(items, creature, who):
    print_pause("You peer cautiously into the cave.")
    if "sword" in items:
        print_pause("You've been here before.\n"
                    "There's nothing left in the cave.")
        print_pause("You walk back out to the field.")
        direction(items, creature, who)
    else:
        print_pause("The cave is actually small. Your eye\n"
                    "catches something shiny behind a rock.")
        print_pause("You have located the magical Sword of Olympus!")
        print_pause("You discard your pathetic dagger\n"
                    "and take the sword with you.")
        print_pause("You walk back out to the field.")
        items.append("sword")
        direction(items, creature, who)


def direction(items, creature, who):
    place = input("Enter 1 to knock on the door of the house.\n"
                  "Enter 2 to peer into the cave.\n")
    if place == '1':
        house(items, creature, who)
    elif place == '2':
        cave(items, creature, who)
    else:
        print_pause("I'm sorry. That is not an option.")
        direction(items, creature, who)


def play_game():
    items = []
    creature = ["gorgon", "fairy", "troll", "wolf", "dragon", "pirate"]
    who = random.choice(creature)
    intro(items, creature, who)
    direction(items, creature, who)


def play_again(items, creature, who):
    response = input("Do you want to play again? y or n\n").lower()
    if "y" in response:
        print_pause("Excellent! Restarting the game...")
        play_game()
    elif "n" in response:
        print_pause("Very well then. Good game.")
    else:
        print_pause("I'm sorry. That is not a choice.")
        play_again(items, creature, who)


play_game()
