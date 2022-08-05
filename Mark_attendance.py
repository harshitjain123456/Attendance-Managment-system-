from tkinter import *
from tkinter import ttk,messagebox
import sqlite3
from tkinter import messagebox
class Faculty:
    def __init__(self,root):
        self.root = root
        self.root.title("Attendance Management System")
        self.root.geometry("1700x800+0+0")
        self.root.configure(background="#96989b")

        title=Label(self.root,text="Mark Attendance",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)



if __name__=="__main__":
    root = Tk()
    ob = Faculty(root)
    root.mainloop()