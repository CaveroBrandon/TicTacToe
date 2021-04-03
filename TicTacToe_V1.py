# Tic tac toe game, not ussing IA, just random numbers
# This version doesnt have a UI
from random import randint
import sys

global empty_spaces
empty_spaces = {}


def restart_game():
    global empty_spaces
    empty_spaces = {1: 1, 2: 2, 3: 3,
                    4: 4, 5: 5, 6: 6,
                    7: 7, 8: 8, 9: 9}


def show_table():
    print('**************')
    print('|', empty_spaces[1], '|', empty_spaces[2], '|', empty_spaces[3], '|')
    print('-------------')
    print('|', empty_spaces[4], '|', empty_spaces[5], '|', empty_spaces[6], '|')
    print('-------------')
    print('|', empty_spaces[7], '|', empty_spaces[8], '|', empty_spaces[9], '|')
    print('-------------')


def validate_decision():
    try:
        value_to_validate = int(input("Your turn:"))
        if 9 >= value_to_validate >= 1:
            if empty_spaces[value_to_validate] == 'X' or empty_spaces[value_to_validate] == 'O':
                validate_decision()
            else:
                empty_spaces[value_to_validate] = 'X'
                show_table()
        else:
            validate_decision()
    except ValueError:
        print('Your play most be a number')
        validate_decision()


def opponent_plays():
    opponent_game = randint(1, 9)
    if 9 >= opponent_game >= 1:
        if empty_spaces[opponent_game] == 'X' or empty_spaces[opponent_game] == 'O':
            opponent_plays()
        else:
            empty_spaces[opponent_game] = 'O'
            show_table()
    else:
        opponent_plays()


def end_game_verification():
    control = False
    for ele in empty_spaces:
        if str(empty_spaces[ele]).isdigit():
            control = True
    if empty_spaces[1] == empty_spaces[2] == empty_spaces[3] == 'X' or \
            empty_spaces[4] == empty_spaces[5] == empty_spaces[6] == 'X' or \
            empty_spaces[7] == empty_spaces[8] == empty_spaces[9] == 'X' or \
            empty_spaces[1] == empty_spaces[4] == empty_spaces[7] == 'X' or \
            empty_spaces[2] == empty_spaces[5] == empty_spaces[8] == 'X' or \
            empty_spaces[3] == empty_spaces[6] == empty_spaces[9] == 'X' or \
            empty_spaces[1] == empty_spaces[5] == empty_spaces[9] == 'X' or \
            empty_spaces[3] == empty_spaces[5] == empty_spaces[7] == 'X':
        print('CONGRATULATIONS YOU WIN')
        game_control = input('Wanna play again Y/N:')
        if game_control == 'Y' or 'y':
            restart_game()
        elif game_control == 'N' or 'n':
            sys.exit()
    elif empty_spaces[1] == empty_spaces[2] == empty_spaces[3] == 'O' or \
            empty_spaces[4] == empty_spaces[5] == empty_spaces[6] == 'O' or \
            empty_spaces[7] == empty_spaces[8] == empty_spaces[9] == 'O' or \
            empty_spaces[1] == empty_spaces[4] == empty_spaces[7] == 'O' or \
            empty_spaces[2] == empty_spaces[5] == empty_spaces[8] == 'O' or \
            empty_spaces[3] == empty_spaces[6] == empty_spaces[9] == 'O' or \
            empty_spaces[1] == empty_spaces[5] == empty_spaces[9] == 'O' or \
            empty_spaces[3] == empty_spaces[5] == empty_spaces[7] == 'O':
        print('YOU LOSE')
        game_control = str(input('Wanna play again Y/N:'))
        if game_control == 'Y' or 'y':
            restart_game()
        elif game_control == 'N' or 'n':
            sys.exit()
    if not control:
        print('IT IS A TIE')
        game_control = str(input('Wanna play again Y/N:'))
        if game_control == 'Y' or 'y':
            restart_game()
        elif game_control == 'N' or 'n':
            sys.exit()
            

def fun_button1():
    if(boton1['text'] == '-'):
       boton1.configure(text = 'X')
def fun_button2():
    if(boton2['text'] == '-'):
       boton2.configure(text = 'X')
def fun_button3():
    if(boton3['text'] == '-'):
       boton3.configure(text = 'X')
def fun_button4():
    if(boton4['text'] == '-'):
       boton4.configure(text = 'X')   
def fun_button5():
    if(boton5['text'] == '-'):
       boton5.configure(text = 'X')
def fun_button6():
    if(boton6['text'] == '-'):
       boton6.configure(text = 'X')
def fun_button7():
    if(boton7['text'] == '-'):
       boton7.configure(text = 'X')
def fun_button8():
    if(boton8['text'] == '-'):
       boton8.configure(text = 'X')
def fun_button9():
    if(boton9['text'] == '-'):
       boton9.configure(text = 'X')



restart_game()
show_table()
while True:
    end_game_verification()
    validate_decision()
    end_game_verification()
    opponent_plays()
