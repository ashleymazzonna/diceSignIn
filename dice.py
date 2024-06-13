from termcolor import colored
from globals import progress_spinner_validate, progress_spinner_processing, \
    users_info, error_message, grid_bar
from passwordcheck import pw_verification

# get username and password
username = input("Username?\n")
password = input("Password?\n")

# validate username exists in users_ino
def check_user_name(uname):
    # bubble_bar()
    if uname not in users_info.keys():

        user_answer = input("The username entered does not match our records.\n"
                            "[+] Would you like to create and account? Y or N\n")
        # grid_bar()
        # progress_spinner_validate()
        if (user_answer == "Y") or (user_answer == "y"):
            # create_username()
            # print("Temp Message Display")
            new_user_name = input(colored("Choose a Username\n", "red"))
            grid_bar()
            for username in users_info.keys():
                if new_user_name in users_info.keys():
                    print(colored("Username not available. Please choose another\n", "red"))
                    new_user_name = input(colored("Username?\n", "blue"))
            else:
                print("Welcome ", new_user_name, " Please choose a strong Password\n")
                userpass = input(colored("Choose a Password\n", "blue"))
                pw_verification(userpass)
        elif (user_answer == "N") or (user_answer == "n"):
            # grid_bar()
            print(colored("Sorry to see you go", "magenta"))

        else:
            check_user_pw(password)

# validate user's password exists in users_info
def check_user_pw(pword):
    if pword not in users_info.values():
        print(colored(error_message, "red"))
    elif pword == users_info[pword]:
        print(colored(f"Welcome {username}", "magenta"))

check_user_name(username)

# validate user's password meets security requirements
def validate_password(pword):
    # check password length (more than 8 chars)
    if len(pword) < 0 or pword:
        print("Please enter a password\n")

    # check password contains numbers, letters and special chars
    # check that password DOES NOT contain illegal chars

def create_username():
        new_user_name = input(colored("Choose a Username\n", "red"))
        progress_spinner_validate()
        if new_user_name in users_info.keys():
            print(colored("Username not available. Please choose another\n", "red"))
            new_user_name = input(colored("Username?\n", "blue"))
        elif new_user_name not in users_info.keys():
            print("Welcome ", new_user_name, " Please choose a strong Password\n")



# create user account
# check username is available
# check username meets all criteria

