# Tic tac toe game, not ussing IA, just random numbers
from tkinter import *
from tkinter import messagebox
from random import randint


global occupied_spaces
occupied_spaces = []


def restar_game():
    boton1.configure(text = '-', state = ACTIVE)
    boton2.configure(text = '-', state = ACTIVE)
    boton3.configure(text = '-', state = ACTIVE)
    boton4.configure(text = '-', state = ACTIVE)
    boton5.configure(text = '-', state = ACTIVE)
    boton6.configure(text = '-', state = ACTIVE)
    boton7.configure(text = '-', state = ACTIVE)
    boton8.configure(text = '-', state = ACTIVE)
    boton9.configure(text = '-', state = ACTIVE)
    occupied_spaces = []

def verify_winner():
    if  boton1['text'] == boton2['text'] == boton3['text'] == 'X' or \
       boton4['text'] == boton5['text'] == boton6['text'] == 'X' or \
       boton7['text'] == boton8['text'] == boton9['text'] == 'X' or \
       boton1['text'] == boton4['text'] == boton7['text'] == 'X' or \
       boton2['text'] == boton5['text'] == boton8['text'] == 'X' or \
       boton3['text'] == boton6['text'] == boton9['text'] == 'X' or \
       boton1['text'] == boton5['text'] == boton9['text'] == 'X' or \
       boton3['text'] == boton5['text'] == boton7['text'] == 'X':
        option = messagebox.askquestion(title = 'Game over', message = 'The winner is X, Wanna play again?')
        if option == 'yes':
            restar_game()
        else:
            root.destroy()
            import main
    elif boton1['text'] == boton2['text'] == boton3['text'] == 'O' or \
       boton4['text'] == boton5['text'] == boton6['text'] == 'O' or \
       boton7['text'] == boton8['text'] == boton9['text'] == 'O' or \
       boton1['text'] == boton4['text'] == boton7['text'] == 'O' or \
       boton2['text'] == boton5['text'] == boton8['text'] == 'O' or \
       boton3['text'] == boton6['text'] == boton9['text'] == 'O' or \
       boton1['text'] == boton5['text'] == boton9['text'] == 'O' or \
       boton3['text'] == boton5['text'] == boton7['text'] == 'O':
        option = messagebox.askquestion(title = 'Game over', message = 'The winner is O, Wanna play again?')
        if option == 'yes':
            restar_game()
        else:
            root.destroy()
            import main
        

def opponent_plays():
    n = randint(1,9)
    if len(occupied_spaces) != 9:
        if (n not in occupied_spaces):
            occupied_spaces.append(n)
            if (n == 1):
                boton1.configure(text = 'O', state = DISABLED)
            elif (n == 2):
                boton2.configure(text = 'O', state = DISABLED)
            elif (n == 3):
                boton3.configure(text = 'O', state = DISABLED)
            elif (n == 4):
                boton4.configure(text = 'O', state = DISABLED)
            elif (n == 5):
                boton5.configure(text = 'O', state = DISABLED)
            elif (n == 6):
                boton6.configure(text = 'O', state = DISABLED)
            elif (n == 7):
                boton7.configure(text = 'O', state = DISABLED)
            elif (n == 8):
                boton8.configure(text = 'O', state = DISABLED)
            elif (n == 9):
                boton9.configure(text = 'O', state = DISABLED)
            verify_winner()
        else:
            opponent_plays()
    else:
        root.destroy()


def fun_button1():
    if(boton1['text'] == '-'):
        boton1.configure(text = 'X', state = DISABLED)
        occupied_spaces.append(1)
        opponent_plays()
    verify_winner()
def fun_button2():
    if(boton2['text'] == '-'):
       boton2.configure(text = 'X', state = DISABLED)
       occupied_spaces.append(2)
       opponent_plays()
    verify_winner()
def fun_button3():
    if(boton3['text'] == '-'):
       boton3.configure(text = 'X', state = DISABLED)
       occupied_spaces.append(3)
       opponent_plays()
    verify_winner()
def fun_button4():
    if(boton4['text'] == '-'):
       boton4.configure(text = 'X', state = DISABLED)
       occupied_spaces.append(4)
       opponent_plays()
    verify_winner()
def fun_button5():
    if(boton5['text'] == '-'):
       boton5.configure(text = 'X', state = DISABLED)
       occupied_spaces.append(5)
       opponent_plays()
    verify_winner()
def fun_button6():
    if(boton6['text'] == '-'):
       boton6.configure(text = 'X', state = DISABLED)
       occupied_spaces.append(6)
       opponent_plays()
    verify_winner()
def fun_button7():
    if(boton7['text'] == '-'):
       boton7.configure(text = 'X', state = DISABLED)
       occupied_spaces.append(7)
       opponent_plays()
    verify_winner()
def fun_button8():
    if(boton8['text'] == '-'):
       boton8.configure(text = 'X', state = DISABLED)
       occupied_spaces.append(8)
       opponent_plays()
    verify_winner()
def fun_button9():
    if(boton9['text'] == '-'):
       boton9.configure(text = 'X', state = DISABLED)
       occupied_spaces.append(9)
       opponent_plays()
    verify_winner()


root = Tk()
root.title('TIC TAC TOE')


#Buttons definitions
boton1 = Button(root, text = '-', command = fun_button1, height = 3, width = 6)
boton2 = Button(root, text = '-', command = fun_button2, height = 3, width = 6)
boton3 = Button(root, text = '-', command = fun_button3, height = 3, width = 6)
boton4 = Button(root, text = '-', command = fun_button4, height = 3, width = 6)
boton5 = Button(root, text = '-', command = fun_button5, height = 3, width = 6)
boton6 = Button(root, text = '-', command = fun_button6, height = 3, width = 6)
boton7 = Button(root, text = '-', command = fun_button7, height = 3, width = 6)
boton8 = Button(root, text = '-', command = fun_button8, height = 3, width = 6)
boton9 = Button(root, text = '-', command = fun_button9, height = 3, width = 6)


#Buttons positioning
boton1.grid(row=0, column=0)
boton2.grid(row=0, column=1)
boton3.grid(row=0, column=2)
boton4.grid(row=1, column=0)
boton5.grid(row=1, column=1)
boton6.grid(row=1, column=2)
boton7.grid(row=2, column=0)
boton8.grid(row=2, column=1)
boton9.grid(row=2, column=2)


root.mainloop()
