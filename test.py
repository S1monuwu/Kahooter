from time import sleep
import random
import string
from kahoot import *
from os import system, name

bot = client()

code = 3584339

letters = string.ascii_lowercase
result_str = ''.join(random.choice(letters) for i in range(8))
randomname = (result_str)
name = randomname

lines = open('funnynames.txt').read().splitlines()
myline =random.choice(lines)
print(myline)

bot.join(code, name)

def joinHandle():
    pass

bot.on("joined", joinHandle)



while True:

    try:

        sleep(0)

    except Exception as e: print(e)

