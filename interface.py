
import chain

from tkinter import *

screen = Tk()
screen.geometry("500x1000")
text = Text(screen, height = 50, width = 100)
text.pack()


def apress():
    text.insert(END, chain.make_song())

btn = Button(screen, text = 'Generate song', width = 15, command = apress) 
btn.pack()

mainloop()