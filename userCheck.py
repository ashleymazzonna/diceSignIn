# from termcolor import colored
# from globals import progress_spinner_validate, progress_spinner_processing, \
#     users_info, specialChars, illegalChars, error_message, grid_bar
# # from passwordcheck import pw_verification
#
# # get username and password
# username = input("Username?\n")
# password = input("Password?\n")
#
# # validate username exists in users_ino
# def check_user_name(uname):
#     # grid_bar()
#     if uname not in users_info.keys():
#
#         user_answer = input("The username entered does not match our records.\n"
#                             "[+] Would you like to create and account? Y or N\n")
#         progress_spinner_processing()
#         # grid_bar()
#         if (user_answer == "Y") or (user_answer == "y"):
#             # create_username()
#             # print("Temp Message Display")
#             newUsername = input("What would you like your username to be?")
#                 if newUsername in users_info.keys():
#                     print(colored("That username is already taken\n Username?", "red"))
#                 else:
#                     check_user_pw(password)
#
#         elif (user_answer == "N") or (user_answer == "n"):
#             # progress_spinner_processing()
#             grid_bar()
#             print(colored("Sorry to see you go", "magenta"))
#
# # validate user's password exists in users_info
# def check_user_pw(pword):
#     if pword not in users_info.values():
#         print(colored(error_message, "red"))
#     elif pword == users_info[pword]:
#         print(colored(f"Welcome {username}", "magenta"))
#
# check_user_name(username)
#
# # validate user's password meets security requirements
# def validate_password(pword):
#     # check password length (more than 8 chars)
#     if len(pword) < 0 or pword:
#         print("Please enter a password")
#
#     # check password contains numbers, letters and special chars
#     # check that password DOES NOT contain illegal chars
#
#
#
# # create user account
# # check username is available
# # check username meets all criteria
#
