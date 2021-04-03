# Tic tac toe game, not ussing IA, just random numbers
from tkinter import *

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


root = Tk()
root.geometry('150x160+0+0')
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
