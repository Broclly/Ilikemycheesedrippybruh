import random
import time
import os
from colorama import Fore
import rich
import rich.color
import subprocess
import assets.ascii
import assets.splash

directoryLocation = ""

player1 = {
    "name": "Default",
    "color" : 3
}
player2 = {
    "name": "Default",
    "color" : 3
}

color = ["[medium_spring_green]","[bright_red]","[deep_sky_blue4]","[gray100]"]

nameFlair1 = [color[player1["color"]]]
nameFlair2 = [color[player2["color"]]]

logsDir = "logs/"

class Game:
    def __init__(self):
        self.totalStix = 0
        self.check = True
    def classicSetup(self):
        global piles
        piles = [1,3,5]
    def player1Classic(self):
        self.totalStix = sum(piles)
        if self.totalStix == 0:
            self.check = False
            return
        invalidChoice  = True
        iterator = 0
        for x in piles:
            if int(piles[iterator]) < 1:
                print(f"Pile{1+iterator}")
                print("Empty!")
            else:
                print(f"Pile{1+iterator}:")
                print("*" *int(piles[0+iterator]))
            iterator += 1
        rich.print(f"{color[player1.get("color")]}It is {player1['name']}'s turn currently...")
        while invalidChoice == True:
            try:
                pileChoice = int(input(f"{player1["name"]}, which pile would you like to take from?\n"))
            except:
                print("")
            try:
                if piles[pileChoice-1] < 1:
                    print("That pile is empty!")
                else:
                    break
            except:
                print("An error occured while processing your choice. Please try again!")
        while invalidChoice == True:
            stixAmnt = input("How many do you wanna take? (# or 'max')\n")
            if stixAmnt == "max":
                break
            elif int(stixAmnt) > piles[pileChoice-1]:
                print("That's too many!")
                stixAmnt = "ERROR!"
            else:
                break

        if stixAmnt != "max":
            if int(stixAmnt) > piles[pileChoice-1]:
                print("That's not a valid")
            print(int(stixAmnt))
            piles[pileChoice-1] = piles[pileChoice-1] - int(stixAmnt)
            time.sleep(1)
        elif stixAmnt == "max":
            piles[pileChoice-1] = 0
            time.sleep(1)
        global lastPlayer
        lastPlayer = player1["name"]
        os.system('cls')
        if self.totalStix == 0:
            self.check = False

    def player2Classic(self):
        self.totalStix = sum(piles)
        if self.totalStix == 0:
            self.check = False
            return
        invalidChoice  = True
        iterator = 0
        for x in piles:
            if int(piles[iterator]) < 1:
                print(f"Pile{1+iterator}")
                print("Empty!")
            else:
                print(f"Pile{1+iterator}:")
                print("*" *int(piles[0+iterator]))
            iterator += 1
        rich.print(f"{color[player2.get("color")]}It is {player2['name']}'s turn currently...")
        while invalidChoice == True:
            try:
                pileChoice = int(input(f"{player2["name"]}, which pile would you like to take from?\n"))
            except:
                print("Error!")
            try:
                if piles[pileChoice-1] < 1:
                    print("That pile is empty!")
                else:
                    break
            except:
                print("An error occured while processing your choice. Please try again!")
        while invalidChoice == True:
            stixAmnt = input("How many do you wanna take? (# or 'max')\n")
            if stixAmnt == "max":
                break
            elif int(stixAmnt) > piles[pileChoice-1]:
                print("That's too many!")
                stixAmnt = "ERROR!"
            else:
                break
        # Error handling for 
        if stixAmnt != "max":
            if int(stixAmnt) > piles[pileChoice-1]:
                print("That's not a valid")
            piles[pileChoice-1] = piles[pileChoice-1] - int(stixAmnt) 
            time.sleep(1)
        elif stixAmnt == "max":
            piles[pileChoice-1] = 0
            time.sleep(1)
        global lastPlayer
        lastPlayer = player2["name"]
        os.system('cls')

    def extremeSetup(self):
        global piles
        piles = [1,3,5,7,9,11,13,15,17,19,21,23,25]
    def player1Extreme(self):
        self.totalStix = sum(piles)
        if self.totalStix == 0:
            self.check = False
            return
        invalidChoice  = True
        iterator = 0
        for x in piles:
            if int(piles[iterator]) < 1:
                print(f"Pile{1+iterator}")
                print("Empty!")
            else:
                print(f"Pile{1+iterator}:")
                print("*" *int(piles[0+iterator]))
            iterator += 1
        rich.print(f"{color[player1.get("color")]}It is {player1['name']}'s turn currently...")
        while invalidChoice == True:
            try:
                pileChoice = int(input(f"{player1["name"]}, which pile would you like to take from?\n"))
            except:
                print("")
            try:
                if piles[pileChoice-1] < 1:
                    print("That pile is empty!")
                else:
                    break
            except:
                print("An error occured while processing your choice. Please try again!")
        while invalidChoice == True:
            stixAmnt = input("How many do you wanna take? (# or 'max')\n")
            if stixAmnt == "max":
                break
            elif int(stixAmnt) > piles[pileChoice-1]:
                print("That's too many!")
                stixAmnt = "ERROR!"
            else:
                break

        if stixAmnt != "max":
            if int(stixAmnt) > piles[pileChoice-1]:
                print("That's not a valid")
            print(int(stixAmnt))
            piles[pileChoice-1] = piles[pileChoice-1] - int(stixAmnt)
            time.sleep(1)
        elif stixAmnt == "max":
            piles[pileChoice-1] = 0
            time.sleep(1)
        global lastPlayer
        lastPlayer = player1["name"]
        os.system('cls')
        if self.totalStix == 0:
            self.check = False

    def player2Extreme(self):
        self.totalStix = sum(piles)
        if self.totalStix == 0:
            self.check = False
            return
        invalidChoice  = True
        iterator = 0
        for x in piles:
            if int(piles[iterator]) < 1:
                print(f"Pile{1+iterator}")
                print("Empty!")
            else:
                print(f"Pile{1+iterator}:")
                print("*" *int(piles[0+iterator]))
            iterator += 1
        rich.print(f"{color[player2.get("color")]}It is {player2['name']}'s turn currently...")
        while invalidChoice == True:
            try:
                pileChoice = int(input(f"{player2["name"]}, which pile would you like to take from?\n"))
            except:
                print("Error!")
            try:
                if piles[pileChoice-1] < 1:
                    print("That pile is empty!")
                else:
                    break
            except:
                print("An error occured while processing your choice. Please try again!")
        while invalidChoice == True:
            stixAmnt = input("How many do you wanna take? (# or 'max')\n")
            if stixAmnt == "max":
                break
            elif int(stixAmnt) > piles[pileChoice-1]:
                print("That's too many!")
                stixAmnt = "ERROR!"
            else:
                break
        # Error handling for 
        if stixAmnt != "max":
            if int(stixAmnt) > piles[pileChoice-1]:
                print("That's not a valid")
            piles[pileChoice-1] = piles[pileChoice-1] - int(stixAmnt) 
            time.sleep(1)
        elif stixAmnt == "max":
            piles[pileChoice-1] = 0
            time.sleep(1)
        global lastPlayer
        lastPlayer = player2["name"]
        os.system('cls')

games = Game()

def ctpd(): # Locates where the script is currently running, and then changes to parent directory of the file
    directoryLocation = os.path.realpath(__file__)
    fileName = os.path.basename(__file__)
    os.chdir(directoryLocation[0:-(len(fileName))])
ctpd()
def randomizer():
    randNum = random.randint(5,10)
    piles = [randNum, randNum, randNum]

def startMenu(): # Basically just a menu that displays when the game starts up
    invalidOperation = 1
    print("Welcome to Joshua's Nim Game!")
    time.sleep(1/2)
    print("")
    print("1. Start!") # Pretty self explanitory
    print("2. How To Play") # Explains how to play
    print("3. Options") # Allows you to customize sticks per pile, how many piles, gamemode etc
    print("4. Credits") # Credits

    while invalidOperation == 1:
        operation = input("Select an operation: ")
        if operation == "1":
            os.system('cls')
            invalidOperation = 0
            initalizer()
        elif operation == "2":
            os.system('cls')
            invalidOperation = 0
            instructions()
        elif operation == "4":
            os.system('cls')
            invalidOperation = 0
            credits()
        else:
            print("Invalid operation!")
            invalidOperation = 1

def initalizer(): # Inital game setup
    username1 = input("Player #1, enter your name: ")
    username2 = input("Player #2, enter your name: ")
    confirmation = input(f"Current users are {username1} and {username2}, is this correct? (y/n)")
    player1.update({"name" : username1})
    player2.update({"name" : username2})

    if confirmation == "y":
        print("Alright then!")
        confirmation = input(f"{username1}, would you like to add some" + Fore.LIGHTYELLOW_EX + " flair?" + Fore.WHITE  + "(y/n)")
        if confirmation == "y":
            print("Which color would you like?\n")
            rich.print(color[0] + "1. Mint Green")
            rich.print(color[1] + "2. Bold Red")
            rich.print(color[2] + "3. Striking Blue")
            operation = input(Fore.WHITE + "Pick a color!")
            if operation == "1" or operation == "2" or operation == "3":
                print("Got it! I'll put it in as your color!")
                player1.update({"color": (int(operation) - 1)})
            else:
                print("Changed your mind? No worries!")

        confirmation = input(f"{username2}, would you like to add some" + Fore.LIGHTYELLOW_EX + " flair?" + Fore.WHITE  + "(y/n)")
        if confirmation == "y":
            print("Which color would you like?\n")
            rich.print(color[0] + "1. Mint Green")
            rich.print(color[1] + "2. Bold Red")
            rich.print(color[2] + "3. Striking Blue")
            operation = input(Fore.WHITE + "Pick a color!")
            if operation == "1" or operation == "2" or operation == "3":
                print("Got it! I'll put it in as your color!")
                player2.update({"color": int(operation) - 1})
            else:
                print("Changed your mind? No worries!")
                confirmation = "y"
    else:
        print("No worries! Let's try this again shall we?")
        time.sleep(1)
        os.system('cls')
        initalizer()
    rich.print(f"Currently, {player1["name"]}'s will look like {color[player1.get("color")]} {player1["name"]}" + color[3] + " got it?")
    rich.print(f"As well, {player2["name"]}'s will look like{color[player2.get("color")]} {player2["name"]}" + color[3] + " got it?")
    input("Perfect! Now, I'll wait for your final confirmation, and the games will begin!")
    os.system('cls')
    print("Loading gamemodes...")
    time.sleep(2)
    print("Done!")
    time.sleep(1/2)
    os.system('cls')
    gameplay()

def gameplay(): # Gameplay manager
    totalStix = 1
    print("Gamemodes currently available:")
    print("1. Classic")
    print("2. Extreme")
    gamemodeSelect = int(input("Which one shall you choose?"))
    os.system('cls')
    loadingScreens()
    if gamemodeSelect == 1:
        games.classicSetup()
        while True:
            games.player1Classic()
            games.player2Classic()
            if games.check == False:
                break
    elif gamemodeSelect == 2:
        games.extremeSetup()
        while True:
            games.player1Extreme()
            games.player2Extreme()
            if games.check == False:
                break
    print(f"Dang, unfortunate for you {lastPlayer}, because you lost!!")
    saveConfirm  = input("Would you like to save the game? (y/n)")
    if saveConfirm == "y":
        os.system('cls')
        saveFile()
        os.system('cls')
        startMenu()
    else:
        print("Sending you back to the menu for now!")
        time.sleep(1)
        os.system('cls')
        startMenu()

def instructions(): # Instructs the player on how the nim game works if they select the "How to Play" option in menu.
    invalidOperation = 1
    print("How to play:")
    print("Nim is a two-player game played with sticks. The sticks are divided into piles. The players alternate turns. On each player's turn they may remove any number of sticks from one of \nthe piles, up to the number of sticks remaining in that pile; but they can only take from a single pile on a given turn.")
    print("\nThe goal is to take the last stick. Whoever takes the last stick loses.")
    print("Rule is that you can't remove any sticks from a pile with none. So if a pile is empty, you can't try and take some from that pile.")
    time.sleep(2)
    while invalidOperation == 1:
        confirmation = input("\n\nReady to play? (y/n)")
        if confirmation == "y":
            invalidOperation = 0
            print("Alright, here we go!")
            time.sleep(1)
            os.system('cls')
            initalizer()
        elif confirmation == "n":
            invalidOperation = 0
            print("No? Back to the menu we go!")
            time.sleep(1)
            os.system('cls')
            startMenu()
        else:
            invalidOperation = 1

def credits(): # Credits for stuff
    print("Creator of this game: Joshua Xavier Pilon")
    print("Help contributed by: Pranushan Piruthviraj, Coby Johns, Michael Pilon, Anurag Nagra, and like 30 people on stack overflow")
    print("Made with GNU v3 License, feel free to go wild!")
    input("\n\n\nPress enter to head back...")
    os.system('cls')
    startMenu()

def loadingScreens(): # Randomized loading screens
    splashMax = random.randint(3,5)
    splashes = 0
    splashRarity = 0
    from assets.splash import splashTextCommon,splashTextLegendary,splashTextRare
    while splashMax != splashes:
        splashRarity = random.randint(0,10)
        print(splashRarity)
        if splashRarity == 10:
            selectedSplash = random.randint(0,5)
            print(splashTextLegendary[selectedSplash])
            time.sleep(1/2)
        elif splashRarity > 6:
            selectedSplash = random.randint(0,5)
            print(splashTextRare[selectedSplash])
            time.sleep(1/2)
        else:
            selectedSplash = random.randint(0,5)
            print(splashTextCommon[selectedSplash])
            time.sleep(1/2)
        splashes += 1
        if splashes == splashMax:
            print("Done!")
            time.sleep(2)
            os.system('cls')
            break

def saveFile(): # Saves files 
    saveName = input("What do you wanna save ur file as? (note: if an existing file with the same names exists, it will erase it.)")
    print("Alright, lemme save it!")
    time.sleep(1)
    save = open("logs/" + saveName + ".txt",'w')
    save.write(f"{lastPlayer} has won the game!\nThe players for this game were: {player1['name']} and {player2['name']}!")
    print("Alright, that's done!")
    time.sleep(1)

startMenu()
