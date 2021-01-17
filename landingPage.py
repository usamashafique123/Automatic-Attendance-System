
import sys
import tkinter.messagebox
import camera_test
import detail


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


# import _support




def vp_start_gui():
    global val, w, root

    root = tk.Tk()

    top = Toplevel1(root)

    # _support.init(root, top)

    root.mainloop()

    w = None


def create_Toplevel1(rt, *args, **kwargs):
    global w, w_win, root
    # rt = root

    root = rt

    w = tk.Toplevel(root)

    top = Toplevel1(w)

    # _support.init(w, top, *args, **kwargs)

    return (w, top)


def destroy_Toplevel1():
    global w

    w.destroy()

    w = None


class Toplevel1:
    def quit(self):
        msg = tkinter.messagebox.askyesno("Quit", "Are you sure you want to quit?")
        if msg:
            exit()

    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'

        _fgcolor = '#000000'  # X11 color: 'black'

        _compcolor = '#d9d9d9'  # X11 color: 'gray85'

        _ana1color = '#d9d9d9'  # X11 color: 'gray85'

        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("600x450+353+181")

        top.minsize(1, 1)

        top.maxsize(1351, 738)

        top.resizable(1, 1)

        top.title("Face Detection Attendance System")

        top.configure(background="#0065d8")

        self.Canvas1 = tk.Canvas(top)

        self.Canvas1.place(relx=0.133, rely=0.044, relheight=0.18, relwidth=0.752)

        self.Canvas1.configure(borderwidth="2")

        self.Canvas1.configure(cursor="fleur")

        self.Canvas1.configure(relief="ridge")

        self.Canvas1.configure(selectbackground="blue")

        self.Canvas1.configure(selectforeground="white")

        self.Label1 = tk.Label(self.Canvas1)

        self.Label1.place(relx=0.2, rely=0.247, height=41, width=259)

        self.Label1.configure(activebackground="#ed051c")

        self.Label1.configure(activeforeground="white")

        self.Label1.configure(background="#d31b1b")

        self.Label1.configure(font="-family {Abyssinica SIL} -size 14 -weight bold")

        self.Label1.configure(text='''Welcome''')

        self.Label2 = tk.Label(top)

        self.Label2.place(relx=0.317, rely=0.933, height=21, width=249)

        self.Label2.configure(background="#8c70d8")

        self.Label2.configure(text='''Digital Attendance System''')

        self.Canvas2 = tk.Canvas(top)
        self.Canvas2.place(relx=0.083, rely=0.311, relheight=0.18, relwidth=0.218)

        self.Canvas2.configure(borderwidth="2")

        self.Canvas2.configure(relief="ridge")

        self.Canvas2.configure(selectbackground="blue")

        self.Canvas2.configure(selectforeground="white")

        self.Button3 = tk.Button(self.Canvas2)

        self.Button3.place(relx=0.0, rely=0.617, height=21, width=129)

        self.Button3.configure(text='''Check Camera''')

        self.Button3.configure(command=camera_test.camer)

        self.Canvas3 = tk.Canvas(top)

        self.Canvas3.place(relx=0.417, rely=0.311, relheight=0.18, relwidth=0.218)

        self.Canvas3.configure(borderwidth="2")

        self.Canvas3.configure(cursor="fleur")

        self.Canvas3.configure(relief="ridge")

        self.Canvas3.configure(selectbackground="blue")

        self.Canvas3.configure(selectforeground="white")

        self.Button4 = tk.Button(self.Canvas3)

        self.Button4.place(relx=0.0, rely=0.617, height=21, width=129)

        self.Button4.configure(text='''Enter New Record''')
        self.Button4.configure(command = detail.vp_start_gui)

        self.Canvas4 = tk.Canvas(top)

        self.Canvas4.place(relx=0.733, rely=0.311, relheight=0.18, relwidth=0.218)

        self.Canvas4.configure(borderwidth="2")

        self.Canvas4.configure(relief="ridge")

        self.Canvas4.configure(selectbackground="blue")

        self.Canvas4.configure(selectforeground="white")

        self.Button5 = tk.Button(self.Canvas4)

        self.Button5.place(relx=0.0, rely=0.617, height=21, width=129)

        self.Button5.configure(text='''Train Model''')

        self.Canvas5 = tk.Canvas(top)

        self.Canvas5.place(relx=0.25, rely=0.622, relheight=0.18, relwidth=0.218)

        self.Canvas5.configure(borderwidth="2")

        self.Canvas5.configure(relief="ridge")

        self.Canvas5.configure(selectbackground="blue")

        self.Canvas5.configure(selectforeground="white")

        self.Button6 = tk.Button(self.Canvas5)

        self.Button6.place(relx=0.0, rely=0.617, height=21, width=129)

        self.Button6.configure(text='''Mark Attendance''')


        self.Canvas6 = tk.Canvas(top)

        self.Canvas6.place(relx=0.583, rely=0.622, relheight=0.18, relwidth=0.218)

        self.Canvas6.configure(borderwidth="2")

        self.Canvas6.configure(relief="ridge")

        self.Canvas6.configure(selectbackground="blue")

        self.Canvas6.configure(selectforeground="white")

        self.Button7 = tk.Button(self.Canvas6)

        self.Button7.place(relx=0.0, rely=0.617, height=21, width=129)

        self.Button7.configure(command=self.quit)

        self.Button7.configure(text='''Quit''')
        #


