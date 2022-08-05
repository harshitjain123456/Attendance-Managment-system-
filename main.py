from tkinter import *
from tkinter import ttk,messagebox
import sqlite3
from tkinter import messagebox
class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1700x800+0+0")
        self.root.configure(background="#96989b")

        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)

         #=================================All vaiable==============

        self.Roll_No_var=StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()



        #================Manage_Frame======================

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#01405f")
        Manage_Frame.place(x=30,y=100,width=460,height=660)

        m_title=Label(Manage_Frame,text=" Manage Students",bg="#01405f",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_Roll=Label(Manage_Frame,text="Roll No.",bg="#01405f",fg="white",font=("times new roman",20,"bold"))
        lbl_Roll.grid(row=1, column=0,pady=10,padx=20,sticky="w")

        txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name= Label(Manage_Frame,text="Name",bg="#01405f",fg="white",font=("times new roman", 20,"bold"))
        lbl_name.grid(row=2,column=0, pady=10, padx=20, sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman", 15, "bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")


        lbl_Email=Label(Manage_Frame,text="Email",bg="#01405f",fg="white",font=("times new roman",20,"bold"))
        lbl_Email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_Email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10, padx=20, sticky="w")


        lbl_Gender= Label(Manage_Frame, text="Gender", bg="#01405f", fg="white", font=("times new roman", 20, "bold"))
        lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var,font=("times new roman", 14, "bold"), values=("Select", "Male", "Female", "Other"),justify=CENTER, width=19, state='readonly')
        combo_gender.grid(row=4, column=1, padx=20, pady=10)
        combo_gender.current(0)
        # combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state='readonly')
        # combo_gender['values']=("Select","male","female","other")
        # combo_gender.grid(row=4,column=1,padx=20,pady=10)
        # combo_gender.current(0)


        lbl_Contact = Label(Manage_Frame, text="Contact", bg="#01405f", fg="white", font=("times new roman", 20, "bold"))
        lbl_Contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_Contact = Entry(Manage_Frame,textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_DOB = Label(Manage_Frame, text="D.O.B", bg="#01405f", fg="white", font=("times new roman", 20, "bold"))
        lbl_DOB.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_DOB = Entry(Manage_Frame, textvariable=self.dob_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_DOB.grid(row=6, column=1, pady=10, padx=20, sticky="w")


        lbl_Address = Label(Manage_Frame, text="Addresss", bg="#01405f", fg="white", font=("times new roman", 20, "bold"))
        lbl_Address.grid(row=7,column=0, pady=10, padx=20, sticky="w")

        self. txt_Address=Text(Manage_Frame,width=30,height=4,font=("",10))
        self. txt_Address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        # ==========================Button Frame===============

        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE)
        btn_Frame.place(x=10, y=520, width=440, height=125)

        Addbtn = Button(btn_Frame, text="Add",command=self.add_student,font=("times new roman",12),bg="#01405f",fg="white").place(x=7, y=8, width=100, height=43)
        updatebtn = Button(btn_Frame, text="Update",command=self.update_data,font=("times new roman",12),bg="#01405f",fg="white").place(x=114, y=8, width=100, height=43)
        deletebtn = Button(btn_Frame, text="Delete",command=self.delete_data,font=("times new roman",12),bg="#01405f",fg="white").place(x=221, y=8, width=100, height=43)
        clearbtn = Button(btn_Frame, text="Clear",command=self.clear,font=("times new roman",12),bg="#01405f",fg="white").place(x=328, y=8, width=100, height=43)

        Add_photo_btn = Button(btn_Frame, text="Add Photo Sample", command=self.add_student,font=("times new roman", 14,"bold"), bg="#ffcd04").place(x=7, y=60, width=207, height=45)
        update_photo_btn = Button(btn_Frame, text="Update Photo Sample", command=self.update_data,font=("times new roman", 14,"bold"), bg="#ffcd04").place(x=221, y=60, width=207, height=45)

        # ================Detail_Frame======================

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#01405f")
        Detail_Frame.place(x=500, y=100, width=1000, height=380)

        lbl_search = Label(Detail_Frame, text="Search_By", bg="#01405f", fg="white",font=("times new roman", 17, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.search_by, width=17, font=("times new roman", 12),values=("Select Option","Roll", "Name", "Contact"), state='readonly')
        combo_search.grid(row=0, column=1, padx=20, pady=10)
        combo_search.current(0)

        txt_search= Entry(Detail_Frame,textvariable=self.search_txt, width=20,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Detail_Frame, text="Search",bg="#96989b", font=("times new roman", 13, "bold"),command=self.search_data).place(x=610,y=10,width=135,height=35)
        showallbtn = Button(Detail_Frame, text="Show All",bg="#96989b", font=("times new roman", 13, "bold"),command=self.fetch_data).place(x=760,y=10,width=135,height=35)

        #====================Table Frame=============
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=60,width=960,height=300)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll",text="Roll No")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact No")
        self.Student_table.heading("dob", text="D.O.B")
        self.Student_table.heading("Address", text="Address")

        self.Student_table['show']='headings'
        self.Student_table.column("roll",width=115)
        self.Student_table.column("name", width=115)
        self.Student_table.column("email", width=115)
        self.Student_table.column("gender", width=115)
        self.Student_table.column("contact", width=115)
        self.Student_table.column("dob",width=115)
        self.Student_table.column("Address", width=115)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

        # ================Detail_Frame======================

        Detail_Frame2 = Frame(self.root, bd=4, relief=RIDGE, bg="#01405f")
        Detail_Frame2.place(x=500, y=480, width=1000, height=280)

        lbl_Year = Label(Detail_Frame2, text="Year ", bg="#01405f", fg="white", font=("times new roman", 20, "bold"))
        lbl_Year.grid(row=0, column=0, pady=30, padx=30, sticky="w")
        txt_Year = Entry(Detail_Frame2, textvariable=self.Roll_No_var, font=("times new roman", 15, "bold"), bd=5,relief=GROOVE)
        txt_Year.grid(row=0, column=1, pady=30, padx=30, sticky="w")

        lbl_Course = Label(Detail_Frame2, text="Course ", bg="#01405f", fg="white", font=("times new roman", 20, "bold"))
        lbl_Course.grid(row=1, column=0, pady=20, padx=30, sticky="w")
        txt_Course = Entry(Detail_Frame2, textvariable=self.Roll_No_var, font=("times new roman", 15, "bold"), bd=5,relief=GROOVE)
        txt_Course.grid(row=1, column=1, pady=20, padx=30, sticky="w")
    #======================================================================================================

    def add_student(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","All fields are required!!!")
        else:
            con=sqlite3.connect(database=r'studentmanagement.db')
            cur=con.cursor()
            try:
                if self.Roll_No_var.get()=="":
                    messagebox.showerror("error","Roll number must be required",parent=self.root)
                else:
                    cur.execute("Select * from student where roll=?",(self.Roll_No_var.get(),))
                    row=cur.fetchone()
                    if row!=None:
                        messagebox.showerror("Error","this roll number already assigned,try different",parent=self.root)
                    else:
                        cur.execute("INSERT into student(roll,name,email,gender,contact,dob,Address) values(?,?,?,?,?,?,?)",(
                            self.Roll_No_var.get(),
                            self.name_var.get(),
                            self.email_var.get(),
                            self.gender_var.get(),
                            self.contact_var.get(),
                            self.dob_var.get(),
                            self.txt_Address.get('1.0',END),
                        ))
                        con.commit()
                        messagebox.showinfo("success","student added successfully",parent=self.root)

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to:{str(ex)}",parent=self.root)
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            #messagebox.showinfo("Success","Record has been inserted")

    def fetch_data(self):
        con=sqlite3.connect(database=r'studentmanagement.db')
        cur=con.cursor()
        cur.execute("select * from student");
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
                con.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_Address.delete("1.0",END)

    def get_cursor(self,ev):
        curosor_row=self.Student_table.focus()
        content=self.Student_table.item(curosor_row)

        row=content['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,row[6])

    def update_data(self):
        con = sqlite3.connect(database=r'studentmanagement.db')
        cur = con.cursor()
        try:
            if self.Roll_No_var.get() == "":
                messagebox.showerror("error", "Roll number must be required", parent=self.root)
            else:
                cur.execute("Select * from student where roll=?", (self.Roll_No_var.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Roll Number", parent=self.root)
                else:
                    cur.execute("UPDATE student set name=?,email=?,gender=?,contact=?,dob=?,Address=? where roll=? ",(
                        self.name_var.get(),
                        self.email_var.get(),
                        self.gender_var.get(),
                        self.contact_var.get(),
                        self.dob_var.get(),
                        self.txt_Address.get('1.0', END),
                        self.Roll_No_var.get()))

                    con.commit()
                    messagebox.showinfo("success", "student update successfully", parent=self.root)
                    self.fetch_data()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)
            con.commit()

    def delete_data(self):
        con = sqlite3.connect(database=r"studentmanagement.db")
        cur = con.cursor()
        try:
            if self.Roll_No_var.get() == "":
                messagebox.showerror("Error", "Select/Enter Student Roll No.", parent=self.root)
            else:
                cur.execute("Select * from student where roll=?", (self.Roll_No_var.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Student Roll No.", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do yoy want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from student where roll=?", (self.Roll_No_var.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Student Deleted Successfully", parent=self.root)
                        self.clear()
        except EXCEPTION as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)
        con.close()
        self.fetch_data()

    def search_data(self):
        con = sqlite3.connect(database=r'studentmanagement.db')
        cur = con.cursor()
        cur.execute("select * from student where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
                con.close()


if __name__=="__main__":
    root = Tk()
    ob = Student(root)
    root.mainloop()

