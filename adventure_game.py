import time
import random

# Choose a random weapon and a random enemy
defense = ["knife", "sword", "gun", "dagger"]
enemies = ['gorgon', 'troll', 'pirate', 'dragon', 'monster']


# Print and pause messages so as to be readable
def print_pause(message):
    print(message)
    time.sleep(2)


def valid_input(prompt, option1):
    while True:
        response = input(prompt).lower()
        if response in option1:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response


# game introduction
def intro():
    global weapon
    weapon = random.choice(defense)
    global enemy
    enemy = random.choice(enemies)
    print_pause("While cycling home from a Game session "
                "with your friends,\n")
    print_pause("You mysteriously find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.\n")
    print_pause("Rumor has it that a " + enemy + " is somewhere around "
                "the vicinity, and has been scaring the nearby village.\n")
    print_pause("In front of you is a house.\n")
    print_pause("To your right is a dark cave.\n")
    print_pause(f"In your hand you hold your trusty "
                "(but not very effective) " + weapon + ".\n")
    choose()


# making a choice
def choose():
    print_pause("What would you like to do?\n")
    print_pause("Enter 1 to knock on the door of the house.\n")
    print_pause("Enter 2 to peer into the cave.\n")
    print_pause("Enter 3 to hide\n")
    choice()


# knocking on the door
def knock():
    print_pause("You approach the door of the house.\n")
    print_pause("You are about to knock when the door opens and "
                "out steps a " + enemy + ".\n")
    print_pause("Eep! This is the " + enemy + " house!\n")
    print_pause("The " + enemy + " attacks you!\n")
    print_pause("You feel a bit under-prepared for this, "
                "what with only having a tiny " + weapon + ".\n")


# entering a cave
def cave():
    print_pause("You peer cautiously into the cave.\n")
    print_pause("It turns out to be only a very small cave.\n")
    print_pause("Your eye catches a glint of metal behind a rock.\n")
    print_pause("You have found the magical Sword of Ogoroth!\n")
    print_pause("You discard your silly old " + weapon + " "
                "and take the sword with you.\n")
    print_pause("You walk back out out to the field.\n")
    choose()


# hide because of fear
def hide():
    print_pause("you hide beside your bicycle and scream for help!\n")
    print_pause("the " + enemy + " comes close, throws "
                "away your bicycle and eats you up!\n")
    print_pause("You have been defeated!\n")
    play_game_again()


# fighting the creature
def fight():
    response = valid_input("Would you like to (1) fight or (2) run away?\n",
                           ['1', '2'])
    if response == '1':
        if 'sword' in weapon:
            print_pause("As the " + enemy + " moves to attack, you unsheath"
                        " your new sword\n")
            print_pause("The sword of Ogoroth shines brightly in your"
                        " hand as you brace yourself for the attack.\n")
            print_pause("But the " + enemy + " takes one look at your shiny"
                        " new " + weapon + " and runs away!\n")
            print_pause("You have rid the town of the " + enemy + ""
                        ". You are victorious!\n")

        else:
            print_pause("You do your best...\n")
            print_pause("But your " + weapon + " "
                        "is no match for the " + enemy + ".\n")
            print_pause("You have been defeated!\n")
        play_game_again()

    elif response == '2':
        print_pause("You run back into the field. Luckily, "
                    "you don't seem to have been followed.\n")
        choose()

    else:
        print_pause("choose the correct option\n")
        fight()


# choose betweeon playing again or ending the game
def play_game_again():
    response = valid_input("Would you like to play again? "
                           "Please say 'yes' or 'no'.\n", "yes or no")
    if "no" in response:
        print_pause("GAME OVER\n")
        exit()
    elif "yes" in response:
        global weapon
        print_pause("Excellent! Restarting the game...\n")
        enemies = ['gorgon', 'troll', 'pirate', 'dragon', 'monster']
        defense = ["knife", "sword", "gun", "dagger"]
        intro()


# making a decision
def choice():
    response = valid_input("Please enter 1, 2 or 3.\n", "1 2 3")
    if response == '1':
        knock()
        fight()
    elif response == '2':
        cave()
    elif response == '3':
        hide()

    else:
        print_pause("pick the correct option")
        choice()


intro()
choose()
