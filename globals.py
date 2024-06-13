import time
from time import sleep
import sys
import random

from alive_progress import alive_bar
from progress.spinner import MoonSpinner, PixelSpinner
from termcolor import colored

pictureValues = [
    "🍓 = 1",
    "🍒 = 2",
    "🫐 = 3",
    "🍑 = 4",
    "🍫 = 5",
    "🍇 = 6",
]
die_values_2 = {
    "1️⃣ 🎲 = 1",
    "2️⃣ = 2",
    "3️⃣ = 3",
    "4️⃣ = 4",
    "5️⃣ = 5",
    "6️⃣ = 6"
}
pictures = [
    "🍓",
    "🍒",
    "🫐",
    "🍑",
    "🍫",
    "🍇",
]

# print(len(pictures) -1)
# print(pictures[1])
# print(pictures[5])
# print(random.choice(pictures))
#
# members = ['harry', 'hermione', 'ron', 'draco', 'luna', 'ashley', 'gianna', 'aislynn',
#            'jasmire', 'luna', 'hope', 'michael', 'freya', 'atrid', 'olaf', 'ragnar', 'spencer', 'donna', 'joey', 'noah', 'greyson']
# passwords = ['pass123', 'newpass123', '123pass', 'hello123', '123hello', '123newpass',
#              'pw12345', '12345pw', 'signin123', '123signin', 'saved123', '123saved']
# current_time = time.ctime()

users_info = {
    "harry": "pass123",
    "hermione": "newpass123",
    "ron": "123pass",
    "draco": "hello123",
    "luna": "123hello",
    "ashley": "123newpass",
    "gianna": "pw12345",
    "aislynn": "12345pw",
    "jasmire": "signin123",
    "spencer": "123signin",
    "hope": "saved123",
    "faith": "123saved",
    "michael": "saved123"

}
# print(users_info)

def progress_spinner_processing():
    with MoonSpinner('Processing…') as bar:
        for i in range(100):
            time.sleep(0.01)
            bar.next()
    # cursor up one line
    sys.stdout.write('\x1b[1A')
    # delete last line
    sys.stdout.write('\x1b[2K')

def progress_spinner_validate():
    with MoonSpinner('Validating information…') as bar:
        for i in range(100):
            time.sleep(0.02)
            bar.next()
    # cursor up one line
    sys.stdout.write('\x1b[1A')
    # delete last line
    sys.stdout.write('\x1b[2K')

def dice_spinner():
    with PixelSpinner('Rolling') as bar:
        for i in range(100):
            time.sleep(0.02)
            bar.next()
    # cursor up one line
    sys.stdout.write('\x1b[1A')
    # delete last line
    sys.stdout.write('\x1b[2K')

def grid_bar():
    with alive_bar(100) as grid_bar:   # default setting
        for i in range(100):
            sleep(0.03)
            grid_bar()
            # cursor up one line
            sys.stdout.write('\x1b[1A')
            # delete last line
            sys.stdout.write('\x1b[2K')
        # call after consuming one item

# using bubble bar and notes spinner
# def bubble_bar():
#     with alive_bar(200, bar = 'bubbles', spinner = 'notes2') as bubble_bar:
#         for i in range(200):
#             sleep(0.03)
#         bubble_bar()


error_message = "Information could not be validated. Please check your username or password is correct and try again."

diceArr = ["🀙", "🀚", "🀛", "🀜", "🀝", "🀞"] # array option
#  legend

diePic = "🎲"
die1 = "1️⃣ 🀙"
dice1A = "🎲 = 1"
die2 = "2️⃣ 🀚"
die3 = "3️⃣ 🀛"
die4 = "4️⃣ 🀜"
die5 = "5️⃣ 🀝"
die6 = "6️⃣ 🀞"
# print(diePic)
# print(die1, die2, die3, die4, die5, die6)
# print(diePic)
# print(diceArr)
# picArr = [
#     "🐟",
#     "🐳",
#     "🐋",
#     "🦈",
#     "🍇",
#     "🍓",
#     "🫐",
#     "🍒",
#     "🍑",
#     "🍫",
#     "🍬",
#     "🍭",
# ]

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z']
specialChars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "~", "`", "?", "/", "<", ">"]
illegalChars = ["{", "}", "[", "]", "|", ";", ":", "'", '"']


