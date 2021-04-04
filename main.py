# Tic tac toe game, not ussing IA, just random numbers
from random import randint
from tkinter import *
import sys


def fun_console_version():
    root.destroy()
    import TicTacToe_V1


def fun_gui_version():
    root.destroy()
    import TicTacToe_V2


def fun_exit():
    root.destroy()


root = Tk()
root.title('TIC TAC TOE')
#root. geometry('350x150+250+200')

label1 = Label(root, text = 'Choose one option')

#Buttons definitions
boton1 = Button(root, text = 'Console Version', command = fun_console_version, height = 3, width = 20)
boton2 = Button(root, text = 'Gui Version', command = fun_gui_version, height = 3, width = 20)
boton3 = Button(root, text = 'EXIT', command = fun_exit, height = 1, width = 10)

#Buttons positioning
boton1.grid(row = 1, column = 0)
boton2.grid(row = 2, column = 0)
boton3.grid(row = 3, column = 0)
                


label1.grid(row = 0, column = 0)


root.mainloop()
