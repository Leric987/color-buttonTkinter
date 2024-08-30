from tkinter import *
from random import choice

def click():
    color = choice(colors)
    root['bg'] = color
    btn['text'] = color
    btn['fg'] = color


root = Tk()
root.title('Цветная кнопка')
root.geometry('300x300')
root.resizable(width=False, height=False)
root['bg'] = 'pink'

colors = ['white', 'grey', 'yellow', 'brown']

btn = Button(root, text='Нажмите', font='Arial 15 bold', bg='black', fg='white', command=click)
btn.pack(expand=1, anchor=CENTER)

root.mainloop()