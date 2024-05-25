# password generator using python
from tkinter import *
import random , string

root = Tk()
root.geometry("400x290")
root.title("Password generator By -  Mehak khan")

# main_title = Frame(root, bg="pink",borderwidth=3)
# Label(main_title, text="PASSWORD GENERATOR",font="comicsensms 25 bold",background="light pink").pack()
# main_title.pack()


title = StringVar()
title_label = Label(root,textvariable=title,font="comicsensms 15 bold").pack(anchor=CENTER,pady=4)
title.set("Password strength")

def select_level():
    select_level = choice.get()

choice = IntVar()
R1 = Radiobutton(root, text="POOR", variable=choice,  value=1, command=select_level,font="comicsensms 10 bold").pack(anchor=CENTER,pady=2)
R2 = Radiobutton(root, text="AVERAGE", variable=choice,  value=2, command=select_level,font="comicsensms 10 bold").pack(anchor=CENTER,pady=2)
R3 = Radiobutton(root, text="ADVANCE", variable=choice,  value=3, command=select_level,font="comicsensms 10 bold").pack(anchor=CENTER,pady=2)

label_choice = Label(root)
label_choice.pack()

password_length = StringVar()
password_length.set("Password length")
lenght_title = Label(root,  textvariable=password_length,font="comicsensms 15 bold").pack(anchor=CENTER)

value = IntVar()
spin_lenght = Spinbox(root, from_=8,to=24,textvariable=value,width=13).pack()

def call_back():
    Isum.config(text=password_generator())

pasword_generate_button = Button(root,text="Generate Password" ,bd=5,height=2,command=call_back)
pasword_generate_button.pack(anchor=CENTER,pady=10)
password = str(call_back)

Isum = Label(root, text="",font="comicsensms 14 bold",foreground="blue")
Isum.pack(side=BOTTOM,anchor=CENTER,pady=4)

# logic 
poor = string.ascii_uppercase + string.ascii_lowercase
average = string.ascii_uppercase + string.ascii_lowercase + string.digits
Symbols ="@#$%^&*_+"
advance = poor + average + Symbols


def password_generator():
    if(choice.get()==1):
        return"".join(random.sample(poor,value.get()))
    elif(choice.get()==2):
        return"".join(random.sample(average,value.get()))
    elif(choice.get()==3):
        return"".join(random.sample(advance,value.get()))


root.mainloop()