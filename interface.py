
import chain

from tkinter import *


screen = Tk()
screen.geometry("500x1000")
text = Text(screen, height = 50, width = 100)
text.pack()


def apress():
	text.insert(END,"\n\n\n")
	text.insert(END,chain.make_song())


def addtweet():
	text.insert(END,"\n\n\n")
	text.insert(END,chain.make_tweet())


btn = Button(screen, text = 'Generate song', width = 20, command = apress) 
btn.pack(side=LEFT)

btn2 = Button(screen, text = 'Generate tweet', width = 20, command = addtweet)
btn2.pack(side=RIGHT)

mainloop()