from tkinter import *
from random import randint
def rollthedice():
    text.delete(0.0, END)
    text.insert(END, str(randint(1,6)))
screen = Tk()
screen.title("Dice")
text = Text(screen, width=1, height=1)
button_A = Button(screen, text="Press!", command=rollthedice)
text.pack()
button_A.pack()