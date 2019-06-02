import time
import sys
import random
import os

# init colours
redColour = "\u001b[31m"
blueColour = "\u001b[34m"
whiteColour = "\u001b[37m"
resetColour = "\u001b[0m"
UNDERLINE = "\033[4m"

listOfWord = [
    ["lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop", "laptop", "dog", "cat", "lemon",
     "cabel", "mirror", "hat"],
    ["Awkward", "ELEFANT", "Bagpipes", "stronghold", "jogging", "beekeeper"],
    ["xylophone", "zigzagging", "jawbreaker", "Oxygen", "megahertz", "jiujitsu"]]

##global Variables
word = ""
searchedWord = list("")
board = list("")
columns = os.get_terminal_size().columns
attempt = 0


def init():
    # os.system("clear")
    global word
    # user picks difficulty
    slowPrint("Select difficulty: ".center(columns), 0.03)
    slowPrint("1 - Easy", 0.05)
    slowPrint("2 - Middle", 0.05)
    slowPrint("3 - Hard", 0.05)

    while True:
        try:
            # userInput = int(input("Select difficulty 1 - EASY  2 - MIDDLE  3 - HARD "))
            difficulty = int(input(": "))
        except Exception as e:
            slowPrint("Please pick a number", 0.05)
            continue

        if difficulty == 1:
            i = random.randint(0, len(listOfWord[0]) - 1)
            word = listOfWord[0][i]
            print(word)
            break
        elif difficulty == 2:
            i = random.randint(0, len(listOfWord[1]) - 1)
            word = listOfWord[1][i]
            print(word)
            break
        elif difficulty == 3:
            i = random.randint(0, len(listOfWord[2]) - 1)
            word = listOfWord[2][i]
            print(word)
            break
        else:
            slowPrint("only between 1 - 3", 0.05)
    main()


def main():
    global searchedWord, board
    searchedWord = list(word)
    board = list("_" * len(searchedWord))
    print("\n\n\n\n" + UNDERLINE + redColour + "YourBoard".center(columns) + resetColour + str(board).center(
        columns) + "\n\n")
    slowPrint("You will have 5 attempts. Good luck!\n", 0.05)
    getInput()


# checking for valid userinput
def getInput():
    slowPrint("Start guessing:  ", 0.05)

    userinput = input()
    while len(userinput) != 1:
        slowPrint("\ninvalid selection. Try again:  ", 0.05)
        userinput = input()
    slowPrint("Checking input .......\n", 0.05)
    compareChar(userinput)


# printing lines slowly in command
def slowPrint(string, timer):
    for x in string:
        print(x, end="", flush=True)
        time.sleep(timer)
    print("\n")


# comparing input and printin board again
def compareChar(userinput):
    global attempt
    guessedCorrectly = False
    i = 0
    while i < len(searchedWord):
        if searchedWord[i] == userinput or searchedWord[i] == userinput.upper():
            if searchedWord[i] == userinput.upper():
                board[i] = userinput.upper()
            else:
                board[i] = userinput
            guessedCorrectly = True
        i += 1

    if guessedCorrectly == True:
        # slowPrint(("Nice, you guesses it right\n"),0.05)
        print("\n\n\n\n" + UNDERLINE + redColour + "YourBoard".center(columns) + resetColour + str(board).center(
            columns) + "\n\n")
    else:
        slowPrint("Sorry, try again\n", 0.05)
        attempt += 1

        # check if user WON
    i = 0
    won = False
    while i < len(searchedWord):
        for c in board:
            if c != searchedWord[i]:
                won = False
                i = len(searchedWord)
                break
            else:
                won = True
                i += 1

    if won == True:
        winnerWinnerChickenDinner()

    if attempt == 5:
        loser()
        return

    getInput()


def winnerWinnerChickenDinner():
    slowPrint("YOU ARE WINNER", 0.05)
    restarter()


def loser():
    slowPrint("YOUR FUCKER LOST", 0.05)
    restarter()


def restarter():
    while True:
        selection = input("PRESS Q TO QUIT OR R TO RESTART:    ")
        if selection is "Q" or selection is "q":
            print("\n" + redColour + "Quitting".center(columns) + resetColour)
            os.system("clear")
            sys.exit()
        if selection is "R" or selection is "r":
            slowPrint("\n" + redColour + "Restarting game".center(columns) + resetColour, 0.05)
            init()
            break


##STARTING INTRO
def intro():
    message = "HANGMAN!"
    printedMessage = ["", "", "", "", "", "", "", "", ""]

    characters = {" ": [" ",
                        " ",
                        " ",
                        " ",
                        " ",
                        " ",
                        " ",
                        " ",
                        " "],
                  "H": ["*        *",
                        "*        *",
                        "*        *",
                        "*        *",
                        "**********",
                        "*        *",
                        "*        *",
                        "*        *",
                        "*        *"],

                  "A": ["**********",
                        "*        *",
                        "*        *",
                        "*        *",
                        "**********",
                        "*        *",
                        "*        *",
                        "*        *",
                        "*        *"],

                  "N": ["**       *",
                        "* *      *",
                        "*  *     *",
                        "*   *    *",
                        "*    *   *",
                        "*     *  *",
                        "*      * *",
                        "*       **",
                        "*        *"],

                  "G": ["**********",
                        "*         ",
                        "*         ",
                        "*         ",
                        "*    *****",
                        "*        *",
                        "*        *",
                        "*        *",
                        "**********"],

                  "M": ["*       **",
                        "**     * *",
                        "* *   *  *",
                        "*  * *   *",
                        "*   *    *",
                        "*        *",
                        "*        *",
                        "*        *",
                        "*        *"],

                  "A": ["**********",
                        "*        *",
                        "*        *",
                        "*        *",
                        "**********",
                        "*        *",
                        "*        *",
                        "*        *",
                        "*        *"],

                  "N": ["**       *",
                        "* *      *",
                        "*  *     *",
                        "*   *    *",
                        "*    *   *",
                        "*     *  *",
                        "*      * *",
                        "*       **",
                        "*        *"],

                  "!": ["    **    ",
                        "    **    ",
                        "    **    ",
                        "    **    ",
                        "    **    ",
                        "    **    ",
                        "    **    ",
                        "   ****   ",
                        "   ****   "
                        ]

                  }

    for row in range(9):
        for char in message:
            printedMessage[row] += (str(characters[char][row]) + " ")

    offset = columns

    i = 0
    while True:
        os.system("clear")
        for row in range(9):
            print("" * offset + printedMessage[row][max(0, offset * -1):columns - offset])

        offset -= 1

        if offset <= ((len(message) + 2) * 6) * -1:
            offset = columns
        time.sleep(0.05)
        i += 1

        if i == 100:
            print("\n\n\n\n")
            break


intro()
init()
main()
