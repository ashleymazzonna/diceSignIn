from termcolor import colored
from globals import progress_spinner_validate, progress_spinner_processing, \
    users_info, error_message, grid_bar
from passwordcheck import pw_verification

# get username and password
username = input(colored("Username?\n", "blue"))
password = input("Password?\n")

def create_username():
    new_user = input(colored("Choose a Username\n", "red"))
    # progress_spinner_validate()
    # if new_user_name in users_info.keys():
    #     print(colored("Username not available. Please choose another\n", "red"))
    #     new_user_name = input(colored("Username?\n", "blue"))
    # elif new_user_name not in users_info.keys():
    #     print("Welcome ", new_user_name, " Please choose a strong Password\n")
    # for new_user in users_info.keys():
    if new_user in users_info.keys():
        for new_user in users_info.keys():
            if new_user in users_info.keys():
                print(colored("Username not available. Please choose another\n", "red"))
                new_user = input(colored("Username?\n", "blue"))

    elif new_user not in users_info.keys():
        print("Welcome ", new_user, " Please choose a strong Password\n")
        userpass = input(colored("Choose a Password\n", "yellow"))
        pw_verification(userpass)

# validate username exists in users_ino
def check_user_name(uname):
    # bubble_bar()
    if uname not in users_info.keys():
        user_answer = input("The username entered does not match our records.\n"
                            "[+] Would you like to create and account? Y or N\n")
        if (user_answer == "Y") or (user_answer == "y"):
            # new_user_name = input(colored("Choose a Username\n", "red"))
            grid_bar()
            create_username()

        elif (user_answer == "N") or (user_answer == "n"):
            # grid_bar()
            print(colored("Sorry to see you go", "magenta"))
    elif uname in users_info.keys():
        # check_user_pw(password)
        grid_bar()
        pw_verification(password)

    print(f"welcome {uname}")
    progress_spinner_validate()
    print("Ready to play")

# validate user's password exists in users_info
# def check_user_pw(pword):
#     if pword not in users_info.values():
#         print(colored(error_message, "red"))
#     elif pword == users_info[pword]:
#         print(colored(f"Welcome {username}", "magenta"))


check_user_name(username)

# validate user's password meets security requirements
# def validate_password(pword):
#     # check password length (more than 8 chars)
#     if len(pword) < 0 or pword:
#         print("Please enter a password\n")

    # check password contains numbers, letters and special chars
    # check that password DOES NOT contain illegal chars

# create user account
# check username is available
# check username meets all criteria

