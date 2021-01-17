import sys
import random
from tkinter import *

import csv

import cv2
import os

# counting the numbers


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True


# import details_support

def vp_start_gui():
    global val, w, root
    root = tk.Tk()
    top = Toplevel1(root)
    root.mainloop()


w = None


def create_Toplevel1(rt, *args, **kwargs):
    global w, w_win, root
    # rt = root
    root = rt
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def takeImages(self):
        Id = self.Text1.get();
        name = self.Text2.get();

        print(Id)
        print(name)



        vp_start_gui().quit()


    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("600x450+344+159")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(1, 1)
        top.title("User Details")
        top.configure(background="#3d55cc")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.167, rely=0.044, relheight=0.167
                          , relwidth=0.675)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(cursor="fleur")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.247, rely=0.267, height=31, width=199)
        self.Label1.configure(background="#c91016")
        self.Label1.configure(cursor="fleur")
        self.Label1.configure(font="-family {DejaVu Sans Mono} -size 16")
        self.Label1.configure(text='''Enter Details''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.1, rely=0.311, height=31, width=89)
        self.Label2.configure(text='''ID''')

        self.Label2_1 = tk.Label(top)
        self.Label2_1.place(relx=0.1, rely=0.467, height=31, width=89)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(text='''Name''')

        self.Text1 = tk.Entry(top)
        self.Text1.place(relx=0.333, rely=0.311, relheight=0.076, relwidth=0.543)

        self.Text1.configure(background="white")
        self.Text1.configure(cursor="fleur")
        self.Text1.configure(font="-family {DejaVu Sans Mono} -size 12")
        self.Text1.configure(selectbackground="blue")
        self.Text1.configure(selectforeground="white")
        userid = random.randint(1, 500000)
        self.Text1.insert(INSERT, userid)
        self.Text1.config(state=DISABLED)

        self.Text2 = tk.Entry(top)
        self.Text2.place(relx=0.333, rely=0.467, relheight=0.076, relwidth=0.543)

        self.Text2.configure(background="white")
        self.Text2.configure(font="-family {DejaVu Sans Mono} -size 12")
        self.Text2.configure(selectbackground="blue")
        self.Text2.configure(selectforeground="white")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.417, rely=0.689, height=31, width=121)
        self.Button1.configure(text='''Submit''', command=self.takeImages)

