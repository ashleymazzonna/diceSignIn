from termcolor import colored
from globals import users_info, specialChars, illegalChars, progress_spinner_validate

# GLOBALS
# new_pass_word = input("Choose a password \n")  # GET USER INPUT - WILL BE PASSED IN THROUGH PARAMETER
pw_holder = []  # HOLDS ALL THE PW CHARACTERS
pw_letters = []  # HOLDS THE LETTERS FROM THE PW
pw_numbs = []  # HOLDS THE NUMBERS FROM THE PW
sc_holder = []  # HOLDS SPECIAL CHARS IN PW
ic_holder = []  # HOLD ILLEGAL CHARS IN PW

# def confirm_pw(user_pw):
#     # 1 confirm the password is in users info
#     if user_pw != users_info.values():
#         print("Not a match")
#     # 2 confirm the password meets the requirements
#     elif user_pw == users_info.values():
#         pw_verification(user_pw)
#         print("match")
# confirm_pw(new_pass_word)

def pw_verification(user_pw):
    pw_length = (len(user_pw))
    # CHECKS THE TOTAL LENGTH OF PW
    if pw_length < 10:
        print(colored("Password must be at least 10 characters", "red"))
    else:
        for element in range(0, len(user_pw)):
            pw_holder.append(user_pw[element])
    #  CHECKS FOR NUMBERS AND LETTERS
    for el in range(0, len(pw_holder)):
        #  print(pw_holder[el])
        if pw_holder[el].isdigit():
            pw_numbs.append(pw_holder[el])
        # ADDS NUMBERS TO NUMBER PW_NUMBS
        elif pw_holder[el].isalpha():
            pw_letters.append(pw_holder[el])  # ADDS LETTERS TO LETTERS PW_LETTERS

    # FOR TESTING ONLY
    charsNumb = (len(pw_numbs))  # COUNT THE AMOUNT OF NUMBERS
    charsLet = (len(pw_letters))  # COUNT THE AMOUNT OF LETTERS

    #  CHECKS FOR AT LEAST 1 NUMBER
    if charsNumb == 0:
        print(colored("Password must contain at least 1 Number", "red"))
    #  CHECKS FOR AT LEAST 1 LETTER
    if charsLet == 0:
        print(colored("Password must contain at least 1 Letter\n", "red"))

    #  CHECKS FOR SPECIAL CHARACTERS
    for char in range(0, len(specialChars)):
        for el in range(0, len(pw_holder)):
            if pw_holder[el] == specialChars[char]:  # ADDS SPECIAL CHARACTERS TO SC_HOLDER
                sc_holder.append(specialChars[char])
    if sc_holder == 0:
        print("Password must have a special character\n")

    for char in range(0, len(illegalChars)):
        for el in range(0, len(pw_holder)):
            if pw_holder[el] == illegalChars[char]:
                ic_holder.append(illegalChars[char])
    if ic_holder != 1:
        print(colored("Password cannot contain", 'red'))
        print(illegalChars)

    # FOR TESTING ONLY
    scCount = (len(sc_holder))  # COUNT THE AMOUNT OF SPECIAL CHARACTERS
    icCount = len(ic_holder)    # COUNT THE AMOUNT OF illegal CHARACTERS

    # print(colored(f"\nFull password \n{pw_holder}", "white"))

    # print(colored(f"\nFull password length: {pw_length}\n", "white"))  # FOR TESTING ONLY
    #
    # print(colored(pw_letters,"yellow"))
    # print(colored(f"Letters: {charsLet}\n", "yellow"))
    #
    # print(colored(pw_numbs,"magenta"))
    # print(colored(f"Numbers: {charsNumb}\n", "magenta"))
    #
    # print(colored(sc_holder, "blue"))
    # print(colored(f"Special Chars: {scCount}\n", "blue"))
    #
    # print(colored(ic_holder, "red"))
    # print(colored(f"Illegal Characters: {icCount}\n", "red"))

    # for element in range(0, len(user_pw)):
    #     print(user_pw[element])
    #     if user_pw[element].isdigit():
    #         print(colored("This is a number", "magenta"))  # for testing
    #     elif user_pw[element].isalpha():
    #         print(colored("This is a letter", "yellow"))  # for testing
    # print(f"This is your new password {new_pass_word}") # for testing only

# pw_verification(new_pass_word)

