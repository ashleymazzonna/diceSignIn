import random
from termcolor import colored
from globals import progress_spinner_processing, dice_spinner, grid_bar
from userCheck import create_user_name, user_name_check


#print(pictureValues) #for testing only

#users signs in
def user_data():

    user_answer = input(colored("++ Do you have an account?\n Yes, Y, y \n No, N, n\n", "blue"))
    # create if for Yes
    if user_answer =="Yes" or user_answer =="Y" or user_answer =="y":
        uname = input(colored("++ Username\n", "green"))
        pword = input(colored("++ Password\n", "magenta"))
        user_name_check(uname,pword)
    elif user_answer =="No" or user_answer =="N" or user_answer =="n":
        get_user_answer = input(colored("++ Do you want to create account? Yes, Y, y \n No, N, n\n", "green"))
        if get_user_answer == "Y" or get_user_answer == "y" or get_user_answer =="Yes" or get_user_answer =="yes":
            create_user_name()
        else:
            print(colored("-- Sorry to see you go.\n-- Come back soon", "red"))
            exit()

#user1, user2, die1, die2
def game_start():
        start_game = input(colored("++ Shall we play a game Bitches\n Yes, Y or y to play No, N or n to exit\n", "yellow"))
        if start_game == "Y" or start_game == "y" or start_game == "Yes" or start_game == "yes":
            user_data()
            die_one = random.choice(pictures)
            die_two = random.choice(pictures)
            # print(dice_spinner())
            #print(die_two, die_one) # for testing only
            print("User One Rolling")
            # progress_spinner_processing()
            grid_bar()
            print(die_one, die_two)

        else:
            print("goodbye")


#need to address what happens after sign in if there is UID and PW don't match - loop 3x then exit

#user_one rolls

# def user_one_rolls(die_2, die_2):
#     # get current score
#     print(dice_spinner())
#     die_1 = random
    #user one rolls
#
# def user_two_rolls(die_1, die_2):
    # get current score

#user_two rolls

#check one against two

game_start()
#user_data()


