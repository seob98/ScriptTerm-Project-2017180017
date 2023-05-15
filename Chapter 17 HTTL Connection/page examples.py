from tkinter import *
import tkinter.ttk

window = Tk()
window.title('exmaple')
notebook = tkinter.ttk.Notebook(window, width=800,height=600)
notebook.pack()

frame1 = Frame(window)
notebook.add(frame1, text='1페이지')
Label(frame1, text='1페이지 내용', fg='red', font='helvetica 48').pack()
frame1 = Frame(window)
notebook.add(frame1, text='2페이지')
Label(frame1, text='2페이지 내용', fg='blue', font='helvetica 48').pack()
frame1 = Frame(window)
notebook.add(frame1, text='3페이지')
Label(frame1, text='3페이지 내용', fg='green', font='helvetica 48').pack()
frame1 = Frame(window)
notebook.add(frame1, text='4페이지')
Label(frame1, text='4페이지 내용', fg='black', font='helvetica 48').pack()

window.mainloop()