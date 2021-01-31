from tkinter import*
from django import forms
root = Tk()
root.geometry('500x500')
root.title("Add students")

label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="First name ",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Last Name ",width=20,font=("bold", 10))
label_2.place(x=80,y=130)

entry_2 = Entry(root)
entry_2.place(x=240,y=130)

label_3 = Label(root, text="Roll number ",width=20,font=("bold", 10))
label_3.place(x=80,y=130)

entry_3 = Entry(root)
entry_3.place(x=240,y=130)

label_4 = Label(root, text="Email",width=20,font=("bold", 10))
label_4.place(x=68,y=180)

entry_4 = Entry(root)
entry_4.place(x=240,y=180)

label_5 = Label(root, text="Gender",width=20,font=("bold", 10))
label_5.place(x=70,y=230)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label_6 = Label(root, text="Age:",width=20,font=("bold", 10))
label_6.place(x=70,y=280)


entry_6 = Entry(root)
entry_6.place(x=240,y=280)
CLASS_CHOICES= [
    ('BSCS', 'BSCS 1ST SEMESTER'),
    ('BSCS', 'BSCS 2ND SEMESTER'),
    ('BSCS', 'BSCS 3RD SEMESTER'),
('BSCS', 'BSCS 4TH SEMESTER'),
    ('BSCS', 'BSCS 5TH SEMESTER'),
    ('BSCS', 'BSCS 6TH SEMESTER'),
('BSCS', 'BSCS 7TH SEMESTER'),
    ('BSCS', 'BSCS 8TH SEMESTER'),
    
('BSIT', 'BSIT 1ST SEMESTER'),
    ('BSIT', 'BSIT 2ND SEMESTER'),
    ('BSIT', 'BSIT 3RD SEMESTER'),
('BSIT', 'BSIT 4TH SEMESTER'),
    ('BSIT', 'BSIT 5TH SEMESTER'),
    ('BSIT', 'BSIT 6TH SEMESTER'),
('BSIT', 'BSIT 7TH SEMESTER'),
    ('BSIT', 'BSIT 8TH SEMESTER'),

('BSSE', 'BSSE 1ST SEMESTER'),
    ('BSSE', 'BSSE 2ND SEMESTER'),
    ('BSSE', 'BSSE 3RD SEMESTER'),
('BSSE', 'BSSE 4TH SEMESTER'),
    ('BSSE', 'BSSE 5TH SEMESTER'),
    ('BSSE', 'BSSE 6TH SEMESTER'S),
('BSSE', 'BSSE 7TH SEMESTER'),
    ('BSSE', 'BSSE 8TH SEMESTER'),
    ]
    Class= forms.CharField(label='Select class', widget=forms.Select(choices=CLASS_CHOICES))

SESSION_CHOICES= [
    ('SESSION', '2017-2021'),
 ('SESSION 1','2018-2022'),
 ('SESSION 2', '2019-2023'),
 ('SESSION 3', '2020-2024'),

Class= forms.CharField(label='Select session', widget=forms.Select(choices=SESSION_CHOICES))

Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)
root.mainloop()
"Student register successfully")