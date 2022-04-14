import time
import random

# Choose a random weapon
defense = ["knife", "sword", "gun", "dagger"]
weapon = random.choice(defense)
enemy = []


# Print and pause messages so as to be readable
def print_pause(message):
    print(message)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response


# game introduction
def intro():
    print_pause("While cycling home from a Game session "
                "with your friends,\n")
    print_pause("You mysteriously find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.\n")
    print_pause("Rumor has it that a terrifying figure is somewhere around "
                "the vicinity, and has been scaring the nearby village.\n")
    print_pause("In front of you is a house.\n")
    print_pause("To your right is a dark cave.\n")
    print_pause(f"In your hand you hold your trusty "
                "(but not very effective) " + weapon + ".\n")
    choice()


# making a choice
def choose():
    print_pause("What would you like to do?")
    choice = input("Enter 1 to knock on the door of the house.")
    ("Enter 2 to peer into the cave.")
    ("Enter 3 to hide")


# knocking on the door
def knock():
    print_pause("You approach the door of the house.\n")
    print_pause("You are about to knock when the door opens and "
                "out steps a terrifying creature.\n")
    print_pause("Eep! This is the monsters's house!\n")
    print_pause("The monster attacks you!\n")
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
    choice()


# hide because of fear
def hide():
    print_pause("you hide beside your bicycle and scream for help!\n")
    print_pause("the creature comes close, throws "
                "away your bicycle and eats you up!\n")
    print_pause("You have been defeated!\n")
    play_game_again()


# fighting the creature
def fight():
    fight_choice = input("Would you like to (1) fight or (2) run away?\n")
    if fight_choice == '1':
        if 'sword' in weapon:
            print_pause("As the creature moves to attack, you unsheath"
                        " your new sword\n")
            print_pause("The sword of Ogoroth shines brightly in your"
                        " hand as you brace yourself for the attack.\n")
            print_pause("But the creature takes one look at your shiny"
                        " new " + weapon + " and runs away!\n")
            print_pause("You have rid the town of the terrifying creature"
                        ". You are victorious!\n")

        else:
            print_pause("You do your best...\n")
            print_pause("But your " + weapon + " "
                        "is no match for the creature.\n")
            print_pause("You have been defeated!\n")
        play_game_again()

    elif fight_choice == '2':
        print_pause("You run back into the field. Luckily, "
                    "you don't seem to have been followed.\n")
        choice()

    else:
        print_pause("choose the correct option\n")
        fight()


# choose betweeon playing again or ending the game
def play_game_again():
    play_again = valid_input("Would you like to play again? "
                             "pick 'yes' or 'no'.\n",
                             "yes", "no")
    if "no" in play_again:
        print_pause("GAME OVER")
        exit()
    elif "yes" in play_again:
        print_pause("Excellent! Restarting the game...")
        intro()


# making a choice
def choice():
    print_pause("What would you like to do?\n")
    choice_option = input("1. knock on the door of the house.\n"
                          "2. peer into the cave.\n"
                          "3. hide\n")
    if choice_option == '1':
        knock()
        fight()
    elif choice_option == '2':
        cave()
    elif choice_option == '3':
        hide()

    else:
        print_pause("pick the correct option")
        choice()


intro()
choice()
