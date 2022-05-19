from tkinter import *

class AdminLoginPageView():
    def __init__(self, root, model):
        root.title("Admin Login")
        root.geometry("1366x768")
        root.resizable(0,  0)
        self.model = model

        self.label = Label(root)
        self.label.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./Images/AdminLogin.png")
        self.label.configure(image=self.img)

        self.button_login = Button(root)
        self.button_login.place(relx=0.7, rely=0.5, width=204, height=52)
        self.button_login.configure(relief="flat")
        self.button_login.configure(overrelief="flat")
        self.button_login.configure(activebackground="#ffffff")
        self.button_login.configure(foreground="#ffffff")
        self.button_login.configure(background="#ffffff")
        self.button_login.configure(borderwidth="0")
        self.img_login = PhotoImage(file="./Images/Button_Login.png")
        self.button_login.configure(image=self.img_login)

        self.entry_username = Entry(root)
        self.entry_username.place(relx=0.527, rely=0.646, width=374, height=30)
        self.entry_username.configure(font="-family {Poppins} -size 12")
        self.entry_username.configure(relief="flat")
        self.entry_username.focus()

        self.entry_password = Entry(root)
        self.entry_password.place(relx=0.527, rely=0.846, width=374, height=30)
        self.entry_password.configure(font="-family {Poppins} -size 16")
        self.entry_password.configure(relief="flat")
        self.entry_password.configure(show="*")
        self.entry_password.focus()
