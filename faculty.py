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

        title=Label(self.root,text="Faculty Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)

         #=================================All vaiable==============

        self.department_var = StringVar()
        self.dept_list = []
        self.fetch_dept()
        self.employee_id_var=StringVar()
        self.fac_name_var = StringVar()
        self.fac_email_var = StringVar()
        self.fac_gender_var = StringVar()
        self.fac_contact_var = StringVar()
        self.fac_dob_var = StringVar()
        self.fac_doj_var = StringVar()
        self.ptype = StringVar()
        self.pnumber = StringVar()
        self.department_Name = StringVar()
        self.department_Id = StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()



        #================Manage_Frame======================

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#01405f")
        Manage_Frame.place(x=30,y=100,width=460,height=660)

        m_title=Label(Manage_Frame,text=" Manage Faculty",bg="#01405f",fg="white",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_Department=Label(Manage_Frame,text="Department",bg="#01405f",fg="white",font=("times new roman",15,"bold"))
        lbl_Department.grid(row=1, column=0,pady=6,padx=20,sticky="w")
        # txt_Department=Entry(Manage_Frame,textvariable=self.department_var,font=("times new roman",10,"bold"),width=25,bd=5,relief=GROOVE)
        # txt_Department.grid(row=1,column=1,pady=6,padx=20,sticky="w")
        txt_Department = ttk.Combobox(Manage_Frame, textvariable=self.department_var, values=self.dept_list, state='readonly',width=17,justify=CENTER, font=("times new roman",14,"bold"))
        txt_Department.grid(row=1,column=1,padx=20,pady=6)
        txt_Department.current(0)

        lbl_Employee_id= Label(Manage_Frame,text="Employee Id",bg="#01405f",fg="white",font=("times new roman", 15,"bold"))
        lbl_Employee_id.grid(row=2,column=0, pady=6, padx=20, sticky="w")
        txt_Employee_id=Entry(Manage_Frame,textvariable=self.employee_id_var,font=("times new roman", 10, "bold"),width=25, bd=5,relief=GROOVE)
        txt_Employee_id.grid(row=2,column=1,pady=6,padx=20,sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", bg="#01405f", fg="white",font=("times new roman", 15, "bold"))
        lbl_name.grid(row=3, column=0, pady=6, padx=20, sticky="w")
        txt_name = Entry(Manage_Frame, textvariable=self.fac_name_var, font=("times new roman", 10, "bold"),width=25, bd=5,relief=GROOVE)
        txt_name.grid(row=3, column=1, pady=6, padx=20, sticky="w")

        lbl_Email=Label(Manage_Frame,text="Email",bg="#01405f",fg="white",font=("times new roman",15,"bold"))
        lbl_Email.grid(row=4,column=0,pady=6,padx=20,sticky="w")
        txt_Email=Entry(Manage_Frame,textvariable=self.fac_email_var,font=("times new roman",10,"bold"),width=25, bd=5,relief=GROOVE)
        txt_Email.grid(row=4,column=1,pady=6, padx=20, sticky="w")


        lbl_Gender= Label(Manage_Frame, text="Gender", bg="#01405f", fg="white", font=("times new roman", 15, "bold"))
        lbl_Gender.grid(row=5, column=0, pady=6, padx=20, sticky="w")
        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.fac_gender_var,font=("times new roman",14,"bold"),values=("Select","Male","Female","Other"),justify=CENTER,width=17,state='readonly')
        combo_gender.grid(row=5,column=1,padx=20,pady=6)
        combo_gender.current(0)


        lbl_Contact = Label(Manage_Frame, text="Contact No.", bg="#01405f", fg="white", font=("times new roman", 15, "bold"))
        lbl_Contact.grid(row=6, column=0, pady=6, padx=20, sticky="w")
        txt_Contact = Entry(Manage_Frame,textvariable=self.fac_contact_var, font=("times new roman", 10, "bold"),width=25, bd=5, relief=GROOVE)
        txt_Contact.grid(row=6, column=1, pady=6, padx=20, sticky="w")

        lbl_DOB = Label(Manage_Frame, text="D.O.B (dd-mm-yyyy)", bg="#01405f", fg="white", font=("times new roman", 15, "bold"))
        lbl_DOB.grid(row=7, column=0, pady=6, padx=20, sticky="w")
        txt_DOB = Entry(Manage_Frame, textvariable=self.fac_dob_var,font=("times new roman", 10, "bold"),width=25, bd=5, relief=GROOVE)
        txt_DOB.grid(row=7, column=1, pady=6, padx=20, sticky="w")

        lbl_DOJ = Label(Manage_Frame, text="D.O.J (dd-mm-yyyy)", bg="#01405f", fg="white",font=("times new roman", 15, "bold"))
        lbl_DOJ.grid(row=8, column=0, pady=6, padx=20, sticky="w")
        txt_DOJ = Entry(Manage_Frame, textvariable=self.fac_doj_var, font=("times new roman", 10, "bold"),width=25, bd=5,relief=GROOVE)
        txt_DOJ.grid(row=8, column=1, pady=6, padx=20, sticky="w")

        lbl_ProofType = Label(Manage_Frame, text="Proof Type", bg="#01405f", fg="white",font=("times new roman", 15, "bold"))
        lbl_ProofType.grid(row=9, column=0, pady=6, padx=20, sticky="w")
        # txt_ProofType = Entry(Manage_Frame, textvariable=self.ptype, font=("times new roman", 10, "bold"),width=25, bd=5,relief=GROOVE)
        # txt_ProofType.grid(row=9, column=1, pady=6, padx=20, sticky="w")
        txt_ProofType = ttk.Combobox(Manage_Frame, textvariable=self.ptype,font=("times new roman", 14, "bold"), values=("Select", "Adhar Card","Pan Card"),justify=CENTER, width=17, state='readonly')
        txt_ProofType.grid(row=9, column=1, padx=20, pady=6)
        txt_ProofType.current(0)

        lbl_Proof_Number = Label(Manage_Frame, text="Proof Number", bg="#01405f", fg="white", font=("times new roman", 15, "bold"))
        lbl_Proof_Number.grid(row=10, column=0, pady=6, padx=20, sticky="w")
        txt_Proof_Number = Entry(Manage_Frame, textvariable=self.pnumber, font=("times new roman", 10, "bold"),width=25, bd=5,relief=GROOVE)
        txt_Proof_Number.grid(row=10, column=1, pady=6, padx=20, sticky="w")

        lbl_Address = Label(Manage_Frame, text="Addresss", bg="#01405f", fg="white", font=("times new roman", 15, "bold"))
        lbl_Address.grid(row=11,column=0, pady=6, padx=20, sticky="w")
        self. txt_Address=Text(Manage_Frame,width=31,height=2,font=("times new roman",10))
        self. txt_Address.grid(row=11,column=1,pady=6,padx=20,sticky="w")

        # ==========================Button Frame===============

        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE)
        btn_Frame.place(x=10, y=545, width=440, height=105)

        Addbtn = Button(btn_Frame, text="Add",command=self.add_faculty,font=("times new roman",12),bg="#01405f",fg="white").place(x=7, y=6, width=100, height=40)
        updatebtn = Button(btn_Frame, text="Update",command=self.update_data,font=("times new roman",12),bg="#01405f",fg="white").place(x=114, y=6, width=100, height=40)
        deletebtn = Button(btn_Frame, text="Delete",command=self.delete_data,font=("times new roman",12),bg="#01405f",fg="white").place(x=221, y=6, width=100, height=40)
        clearbtn = Button(btn_Frame, text="Clear",command=self.clear,font=("times new roman",12),bg="#01405f",fg="white").place(x=328, y=6, width=100, height=40)

        Add_photo_btn = Button(btn_Frame, text="Add Photo Sample", command=self.add_faculty,font=("times new roman", 14,"bold"), bg="#ffcd04").place(x=7, y=55, width=207, height=40)
        update_photo_btn = Button(btn_Frame, text="Update Photo Sample", command=self.update_data,font=("times new roman", 14,"bold"), bg="#ffcd04").place(x=221, y=55, width=207, height=40)

        # ================Detail_Frame======================

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#01405f")
        Detail_Frame.place(x=500, y=100, width=1000, height=660)

        lbl_search = Label(Detail_Frame, text="Search By", bg="#01405f", fg="white",font=("times new roman", 17, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.search_by, font=("times new roman", 12),values=("Select Option","Roll", "Name", "Contact"), width=17, state='readonly')
        combo_search.grid(row=0, column=1, padx=20, pady=10)
        combo_search.current(0)

        txt_search= Entry(Detail_Frame,textvariable=self.search_txt, width=20,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_search.place(x=350,y=12,width=235,height=28)

        searchbtn = Button(Detail_Frame, text="Search",bg="#96989b", font=("times new roman", 13, "bold"),command=self.search_data).place(x=610,y=10,width=135,height=35)
        showallbtn = Button(Detail_Frame, text="Show All",bg="#96989b", font=("times new roman", 13, "bold"),command=self.fetch_data).place(x=760,y=10,width=135,height=35)

        #====================Table Frame=============
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=60,width=960,height=300)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
        self.Faculty_table=ttk.Treeview(Table_Frame,columns=("department", "empid", "name", "email", "gender", "contact", "dob", "doj", "proofType", "proofNumber", "Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Faculty_table.xview)
        scroll_y.config(command=self.Faculty_table.yview)
        self.Faculty_table.heading("department", text="Department")
        self.Faculty_table.heading("empid",text="Employee No")
        self.Faculty_table.heading("name", text="Name")
        self.Faculty_table.heading("email", text="Email")
        self.Faculty_table.heading("gender", text="Gender")
        self.Faculty_table.heading("contact", text="Contact No")
        self.Faculty_table.heading("dob", text="D.O.B")
        self.Faculty_table.heading("doj", text="D.O.J")
        self.Faculty_table.heading("proofType", text="Proof Type")
        self.Faculty_table.heading("proofNumber", text="Proof Number")
        self.Faculty_table.heading("Address", text="Address")

        self.Faculty_table['show']='headings'
        self.Faculty_table.column("department",width=115)
        self.Faculty_table.column("empid", width=115)
        self.Faculty_table.column("name", width=115)
        self.Faculty_table.column("email", width=115)
        self.Faculty_table.column("gender", width=115)
        self.Faculty_table.column("contact", width=115)
        self.Faculty_table.column("dob",width=115)
        self.Faculty_table.column("doj", width=115)
        self.Faculty_table.column("proofType", width=115)
        self.Faculty_table.column("proofNumber", width=115)
        self.Faculty_table.column("Address", width=115)
        self.Faculty_table.pack(fill=BOTH,expand=1)
        self.Faculty_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    # ================Detail_Frame 2 ======================

        Detail_Frame2 = LabelFrame(Detail_Frame,text="Department Management", font=("times new roman", 15, "bold"), bd=5, relief=RIDGE, bg="white")
        Detail_Frame2.place(x=10, y=370, width=960, height=280)

        combo_search_dept = ttk.Combobox(Detail_Frame2, textvariable=self.search_by, width=15, font=("times new roman", 12),values=("Select Option", "Roll", "Name", "Contact"), state='readonly')
        combo_search_dept.grid(row=0, column=1, padx=10, pady=10)
        combo_search_dept.current(0)

        txt_search_dept = Entry(Detail_Frame2, textvariable=self.search_txt, width=15, font=("times new roman", 15, "bold"),bd=3, relief=GROOVE)
        txt_search_dept.grid(row=0, column=2, pady=10, padx=10, sticky="w")

        searchbtn = Button(Detail_Frame2, text="Search", bg="#96989b", font=("times new roman", 13, "bold"),command=self.search_data).place(x=350, y=10, width=115, height=30)
        showallbtn = Button(Detail_Frame2, text="Show All", bg="#96989b", font=("times new roman", 13, "bold"),command=self.fetch_data).place(x=475, y=10, width=115, height=30)

        lbl_Dept_id = Label(Detail_Frame2, text="Department Id", bg="white", fg="black",font=("times new roman", 15, "bold"))
        lbl_Dept_id.place(x=80, y=65)
        txt_Dept_id = Entry(Detail_Frame2, textvariable=self.department_Id, font=("times new roman", 10, "bold"),bd=2, relief=GROOVE)
        txt_Dept_id.place(x=340, y=65, width=230, height=28)

        lbl_Dept_name = Label(Detail_Frame2, text="Department Name", bg="white", fg="black", font=("times new roman", 15, "bold"))
        lbl_Dept_name.place(x=80,y=105)
        txt_Dept_name = Entry(Detail_Frame2, textvariable=self.department_Name, font=("times new roman", 10, "bold"),bd=2, relief=GROOVE)
        txt_Dept_name.place(x=340,y=105, width=230,height=28)

        btn_Frame2 = Frame(Detail_Frame2, bd=4, relief=RIDGE)
        btn_Frame2.place(x=10, y=180, width=530, height=65)

        Addbtn = Button(btn_Frame2, text="Add", command=self.add_department, font=("times new roman", 14,"bold"), bg="#284b4d",fg="#fdce02").place(x=7, y=6, width=120, height=45)
        updatebtn = Button(btn_Frame2, text="Update", command=self.update_department, font=("times new roman", 14,"bold"),bg="#284b4d", fg="#fdce02").place(x=134, y=6, width=120, height=45)
        deletebtn = Button(btn_Frame2, text="Delete", command=self.delete_department, font=("times new roman", 14,"bold"),bg="#284b4d", fg="#fdce02").place(x=261, y=6, width=120, height=45)
        clearbtn = Button(btn_Frame2, text="Clear", command=self.clear1, font=("times new roman", 14,"bold"), bg="#284b4d",fg="#fdce02").place(x=388, y=6, width=120, height=45)

        # ====================Table Frame 2 =============
        Table_Frame2 = Frame(Detail_Frame2, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame2.place(x=615, y=0, width=320, height=253)

        scroll_x2 = Scrollbar(Table_Frame2, orient=HORIZONTAL)
        scroll_y2 = Scrollbar(Table_Frame2, orient=VERTICAL)
        self.Department_table = ttk.Treeview(Table_Frame2,columns=("dpid","departmentName"),xscrollcommand=scroll_x2.set, yscrollcommand=scroll_y2.set)
        scroll_x2.pack(side=BOTTOM, fill=X)
        scroll_y2.pack(side=RIGHT, fill=Y)
        scroll_x2.config(command=self.Department_table.xview)
        scroll_y2.config(command=self.Department_table.yview)
        self.Department_table.heading("dpid", text="Department Id")
        self.Department_table.heading("departmentName", text="Department Name")

        self.Department_table['show'] = 'headings'
        self.Department_table.column("dpid", width=50)
        self.Department_table.column("departmentName", width=70)

        self.Department_table.pack(fill=BOTH, expand=1)
        self.Department_table.bind("<ButtonRelease-1>", self.get_cursor1)
        self.fetch_data1()
    #======================================================================================================

    def fetch_dept(self):
        self.dept_list.append("Empty")
        con = sqlite3.connect(database=r"studentmanagement.db")
        cur = con.cursor()
        try:
            cur.execute("Select departmentName from department")
            dep = cur.fetchall()

            if len(dep) > 0:
                del self.dept_list[:]
                self.dept_list.append("Select")
                for i in dep:
                    self.dept_list.append(i[0])
        except EXCEPTION as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)

    def add_faculty(self):
        if self.employee_id_var.get()=="" or self.fac_name_var=="":
            messagebox.showerror("Error","All fields are required!!!")
        else:
            con=sqlite3.connect(database=r'studentmanagement.db')
            cur=con.cursor()
            try:
                if self.employee_id_var.get()=="":
                    messagebox.showerror("error","Employee Id must be required",parent=self.root)
                else:
                    cur.execute("Select * from faculty where empid=?",(self.employee_id_var.get(),))
                    row=cur.fetchone()
                    if row!=None:
                        messagebox.showerror("Error","this roll number already assigned,try different",parent=self.root)
                    else:
                        cur.execute("INSERT into faculty(department,empid,name,email,gender,contact,dob,doj,proofType,proofNumber,Address) values(?,?,?,?,?,?,?,?,?,?,?)",(
                            self.department_var.get(),
                            self.employee_id_var.get(),
                            self.fac_name_var.get(),
                            self.fac_email_var.get(),
                            self.fac_gender_var.get(),
                            self.fac_contact_var.get(),
                            self.fac_dob_var.get(),
                            self.fac_doj_var.get(),
                            self.ptype.get(),
                            self.pnumber.get(),
                            self.txt_Address.get('1.0',END),
                        ))
                        con.commit()
                        messagebox.showinfo("success","faculty added successfully",parent=self.root)

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to:{str(ex)}",parent=self.root)
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            #messagebox.showinfo("Success","Record has been inserted")

    def add_department(self):
        if self.department_Name.get()=="" or self.department_Id.get()=="":
            messagebox.showerror("Error","All fields are required!!!")
        else:
            con = sqlite3.connect(database=r'studentmanagement.db')
            cur = con.cursor()
            try:
                if self.department_Id.get() == "":
                    messagebox.showerror("error", "Department Id must be required", parent=self.root)
                else:
                    cur.execute("Select * from department where dpid=?", (self.department_Id.get(),))
                    row = cur.fetchone()
                    if row != None:
                        messagebox.showerror("Error", "this department id already assigned,try different",parent=self.root)
                    else:
                        cur.execute("INSERT into department(dpid,departmentName) values(?,?)",
                            (
                                self.department_Id.get(),
                                self.department_Name.get(),
                            ))
                        con.commit()
                        messagebox.showinfo("success", "department added successfully", parent=self.root)

            except Exception as ex:
                messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)
            con.commit()
            self.fetch_data1()
            self.clear1()
            con.close()

    def fetch_data(self):
        con=sqlite3.connect(database=r'studentmanagement.db')
        cur=con.cursor()
        cur.execute("select * from faculty");
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Faculty_table.delete(*self.Faculty_table.get_children())
            for row in rows:
                self.Faculty_table.insert('',END,values=row)
                con.close()

    def fetch_data1(self):
        con=sqlite3.connect(database=r'studentmanagement.db')
        cur=con.cursor()
        cur.execute("select * from department");
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Department_table.delete(*self.Department_table.get_children())
            for row in rows:
                self.Department_table.insert('',END,values=row)
                con.close()

    def clear(self):
        self.department_var.set("")
        self.employee_id_var.set("")
        self.fac_name_var.set("")
        self.fac_email_var.set("")
        self.fac_gender_var.set("")
        self.fac_contact_var.set("")
        self.fac_dob_var.set("")
        self.fac_doj_var.set("")
        self.ptype.set("")
        self.pnumber.set("")
        self.txt_Address.delete("1.0",END)

    def clear1(self):
        self.department_Id.set("")
        self.department_Name.set("")

    def get_cursor(self,ev):
        curosor_row=self.Faculty_table.focus()
        content=self.Faculty_table.item(curosor_row)

        row=content['values']
        self.department_var.set(row[0])
        self.employee_id_var.set(row[1])
        self.fac_name_var.set(row[2])
        self.fac_email_var.set(row[3])
        self.fac_gender_var.set(row[4])
        self.fac_contact_var.set(row[5])
        self.fac_dob_var.set(row[6])
        self.fac_doj_var.set(row[7])
        self.ptype.set(row[8])
        self.pnumber.set(row[9])
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,row[6])

    def get_cursor1(self,ev):
        curosor_row=self.Department_table.focus()
        content=self.Department_table.item(curosor_row)

        row=content['values']
        self.department_Id.set(row[0])
        self.department_Name.set(row[1])


    def update_data(self):
        con = sqlite3.connect(database=r'studentmanagement.db')
        cur = con.cursor()
        try:
            if self.employee_id_var.get() == "":
                messagebox.showerror("error", "Employee Id must be required", parent=self.root)
            else:
                cur.execute("Select * from faculty where empid=?", (self.employee_id_var.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Employee Id", parent=self.root)
                else:
                    cur.execute("UPDATE faculty set department=?,name=?,email=?,gender=?,contact=?,dob=?,doj=?,proofType=?,proofNumber=?,Address=? where empid=? ",(
                        self.department_var.get(),
                        self.fac_name_var.get(),
                        self.fac_email_var.get(),
                        self.fac_gender_var.get(),
                        self.fac_contact_var.get(),
                        self.fac_dob_var.get(),
                        self.fac_doj_var.get(),
                        self.ptype.get(),
                        self.pnumber.get(),
                        self.txt_Address.get('1.0', END),
                        self.employee_id_var.get()))

                    con.commit()
                    messagebox.showinfo("success", "faculty update successfully", parent=self.root)
                    self.fetch_data()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)
            con.commit()

    def update_department(self):
        con = sqlite3.connect(database=r'studentmanagement.db')
        cur = con.cursor()
        try:
            if self.department_Id.get() == "":
                messagebox.showerror("error", "Department Id must be required", parent=self.root)
            else:
                cur.execute("Select * from department where dpid=?", (self.department_Id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Employee Id", parent=self.root)
                else:
                    cur.execute("UPDATE department set departmentName=? where dpid=? ",(
                        self.department_Name.get(),
                        self.department_Id.get()))
                    con.commit()
                    messagebox.showinfo("success", "department update successfully", parent=self.root)
                    self.fetch_data1()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.root)
            con.commit()


    def delete_data(self):
        con = sqlite3.connect(database=r"studentmanagement.db")
        cur = con.cursor()
        try:
            if self.employee_id_var.get() == "":
                messagebox.showerror("Error", "Select/Enter employee id from the list", parent=self.root)
            else:
                cur.execute("Select * from faculty where empid=?", (self.employee_id_var.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Employee Id", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do yoy want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from faculty where empid=?", (self.employee_id_var.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Employee Deleted Successfully", parent=self.root)
                        self.clear()
        except EXCEPTION as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)
        con.close()
        self.fetch_data()

    def delete_department(self):
        con = sqlite3.connect(database=r"studentmanagement.db")
        cur = con.cursor()
        try:
            if self.department_Id.get() == "":
                messagebox.showerror("Error", "Select/Enter department id from the list", parent=self.root)
            else:
                cur.execute("Select * from department where dpid=?", (self.department_Id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Department Id", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do yoy want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from department where dpid=?", (self.department_Id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Department Deleted Successfully", parent=self.root)
                        self.clear()
        except EXCEPTION as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)
        con.close()
        self.fetch_data1()


    def search_data(self):
        # con = sqlite3.connect(database=r'student.db')
        # cur = con.cursor()
        # cur.execute("select * from student where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        # rows = cur.fetchall()
        # if len(rows) != 0:
        #     self.Student_table.delete(*self.Student_table.get_children())
        #     for row in rows:
        #         self.Student_table.insert('', END, values=row)
        #         con.close()
        pass



if __name__=="__main__":
    root = Tk()
    ob = Faculty(root)
    root.mainloop()

