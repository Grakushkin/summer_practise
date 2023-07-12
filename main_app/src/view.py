from tkinter import *
from controller import *

root = Tk()
root['bg'] = '#82807a'
root.title('Название программы')
root.geometry('300x250')

root.resizable(width = False, height = False)

canvas = Canvas(root, height =300, width=250)
canvas.pack()

frame = Frame(root, bg='white')
frame.place(relx=0.15, relwidth = 0.7, relheight = 1)

title = Label(frame, text = 'Выберите действие',font = 40,bg = 'green')
title.pack()
btn_1 = Button(frame, text ='Линейный график', width = 20, command = linear_diagram)
btn_1.pack()
btn_2 = Button(frame, text ='Столбчатая диаграмма ', width = 20, command = bar_diagram)
btn_2.pack()
btn_3 = Button(frame, text ='Круговая диаграмма', width = 20, command = pie_diagram)
btn_3.pack()


def start() -> None:
    '''Start the event loop'''
    root.mainloop()

