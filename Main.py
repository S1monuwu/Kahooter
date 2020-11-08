from time import sleep
import random
import string
from kahoot import client
from os import system, name
import shutil
import os
try:
    os.remove("backup.txt")
except:
    sleep(0)

movie = 0
script = 0
usenamelist = False
comfirm = "N"
firstry = 1
random_name = 'False'
while comfirm == 'N' or comfirm == 'n':
    if firstry == 0:
        # ------------------------Clear Screen-----------------------------#
        print("                                                          ")
        print("                                                          ")
        print("                                                          ")
        print("                                                          ")
        print("                                                          ")
        print("                                                          ")

        print("                                                          ")
        print("                                                          ")
        print("                                                          ")
        print("                                                          ")
        print("                                                          ")
        print("                                                          ")

        print("                                                          ")
        print("                                                          ")
        print("                                                          ")
        print("                                                          ")
        print("                                                          ")
        print("                                                          ")

        print("                                                          ")
        print("                                                          ")
        print("                                                          ")
        print("                                                          ")
        print("                                                          ")
        print("                                                          ")

        print("                                                          ")
        print("                                                          ")
        print("                                                          ")
        print("                                                          ")
        print("                                                          ")
        print("                                                          ")

        print("                                                          ")
        print("                                                          ")
        print("                                                          ")
        print("                                                          ")
        print("                                                          ")
        print("                                                          ")
        # ------------------------------------------------------------------#

    bot = client()

    code = int(input("Kahoot Code : "))

    AmountOfBots = int(input("Amount Of Bots? Max 2000 : "))
    if int(AmountOfBots) > 2000:
        AmountOfBots = 2000

    beemovie = input('Script Mode? Y or N : ')
    if beemovie == 'Y' or beemovie == 'y':
        beemovie = True
        movie = input("What Script? 1: Bee Movie, 2: Never Gonna Give You Up, 3: Iconic Vines : " )

    if movie == '1':
        script = 'beemovie.txt'

    if movie == '2':
        script = 'RickRole.txt'

    if movie == '3':
        script = 'vines.txt'
    if beemovie != True:
        usenamelist = input('Would you like to use a name list? Y or N: ')

    if usenamelist == 'Y' or usenamelist == 'y':
        usenamelist = True
        namelist = input('What namelist would you like to use? Example: funnynames.txt: ')

    if usenamelist != True and beemovie != True:
        random_name = input("Random String As Name? Y Or N : ")

    if random_name == 'Y' or random_name == 'y':
        randomlength = int(input('How long will the random name be? : '))
        random_name = True

    if random_name == True:
        name = None
    else:
        if usenamelist != True and beemovie != True:
            name = input("Bots names? : ")



    delay = 0

    if beemovie == True:
        delay = 0.5

    # ------------------------Clear Screen-----------------------------#

    print("                                                          ")
    print("                                                          ")
    print("                                                          ")
    print("                                                          ")
    print("                                                          ")
    print("                                                          ")

    print("                                                          ")
    print("                                                          ")
    print("                                                          ")
    print("                                                          ")
    print("                                                          ")
    print("                                                          ")

    print("                                                          ")
    print("                                                          ")
    print("                                                          ")
    print("                                                          ")
    print("                                                          ")
    print("                                                          ")

    print("                                                          ")
    print("                                                          ")
    print("                                                          ")
    print("                                                          ")
    print("                                                          ")
    print("                                                          ")

    print("                                                          ")
    print("                                                          ")
    print("                                                          ")
    print("                                                          ")
    print("                                                          ")
    print("                                                          ")

    print("                                                          ")
    print("                                                          ")
    print("                                                          ")
    print("                                                          ")
    print("                                                          ")
    print("                                                          ")
    # ------------------------------------------------------------------#

    print("Code = " + str(code))

    print("                                                          ")

    print("Random String As Name = " + str(random_name))

    print("                                                          ")
    if random_name == True:
        sleep(0)

    else:
        if usenamelist == True:
            print("Namelist = " + namelist)
        else:
            if beemovie == True:
                print('Movie mode = True')
            else:
                print("Names = " + name)


        print("                                                          ")

    print("Amount Of Bots = " + str(AmountOfBots))

    print("                                                          ")

    comfirm = input("Is this correct? Y or N: ")
    firstry = 0
botcount = 1
AmountOfBots = AmountOfBots + 1
if beemovie == True:
    shutil.copy(script, 'backup.txt')
while botcount != AmountOfBots:
    if random_name == True:
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(randomlength))
        randomname = (result_str)
        name = randomname
    else:
        if usenamelist == True:
            lines = open('funnynames.txt').read().splitlines()
            myline = random.choice(lines)
            name = myline
    if AmountOfBots == 2:
        botcount = ""

    if beemovie == True:
        with open("backup.txt", "r") as file:
            first_line = file.readline()
        name = first_line
        with open('backup.txt', 'r') as fin:
            data = fin.read().splitlines(True)
        with open('backup.txt', 'w') as fout:
            fout.writelines(data[1:])


    bot = client()
    if beemovie == True:
        n = str(random.randint(0, 9))
        bot.join(code, name + " " + n + n)
    else:
        bot.join(code, name + str(botcount))

    def joinHandle():
        pass
    bot.on("joined", joinHandle)
    if botcount != "":
        botcount = botcount + 1
    if random_name == True:
        print(botcount)
    else:
        if AmountOfBots != 0:
            print(name + str(botcount))

    if botcount == "":
        AmountOfBots = ""
    sleep(delay)

try:
    os.remove("backup.txt")
except:
    sleep(0)

print("done ;)")

