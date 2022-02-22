from random import randint


def roll_dice():
    dice = randint(1,6)
    print(f"The dice rolled {dice}")

def play_again():
    while True:
        play_again = str(input("Would you like to play again? (y/n)\n")).lower()
        play_again.strip()
        if play_again == 'y':
            roll_dice()
        else:
            print("Ok. Thanks for playing!")
            break

opt = str(input("Hello. Would you like to roll the dice? (y/n)\n")).lower()
opt.strip()


if opt == 'y':
    roll_dice()
    play_again()
elif opt == 'n':
    print("Ok. Thanks for playing!")
else:
    print("Invalid option.")
