import time
import os

message = "HANGMAN!"
printedMessage = ["","","","","","","","",""]
WIDTH = os.get_terminal_size().columns

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
        printedMessage[row] += (str(characters[char][row])+ " ")

offset = WIDTH

i = 0
while True:
    os.system("clear")
    for row in range(9):
        print(""*offset + printedMessage[row][max(0,offset*-1):WIDTH - offset])

    offset -= 1

    if offset <= ((len(message)+2)*6)*-1:
        offset = WIDTH
    time.sleep(0.05)
    i +=1

    if i == 100:
        break
