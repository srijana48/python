from tkinter import *
#from tkinter import ttk
import pymysql
class Student:
    db_name='database.db'
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        title = Label (self.root,text = "Student Management System",bd = 10,relief = GROOVE,font = ("times new roman",40,"bold"),bg = "yellow",fg = "red")
        title.pack(side=TOP,fill=X)

        #----allvariables------

        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.contact_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()
        
        #----manage frame----
        manage_Frame=Frame (self.root,bd=4,relief=RIDGE,bg="crimson")
        manage_Frame.place(x=20,y=100,width=450,height=580)
        
        m_title= Label(manage_Frame,text="Manage Student",bg="crimson",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20,padx=30)
        lbl_roll=Label(manage_Frame,text="RollNo.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        txt_Roll = Entry(manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(manage_Frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        txt_Name = Entry(manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_email=Label(manage_Frame,text="Email",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        txt_Email = Entry(manage_Frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10,padx=20,sticky="w")


        

        lbl_contact=Label(manage_Frame,text="Contact",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        txt_Contact = Entry(manage_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_Address=Label(manage_Frame,text="Address",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Address.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        self.txt_Address = Text(manage_Frame,width=30,height=4,font=("",10))
        self.txt_Address.grid(row=6,column=1,pady=10,padx=20,sticky="w")
        
        btn_Frame = Frame(manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=15,y=500,width=420)
        Addbtn = Button(btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        Updatebtn = Button(btn_Frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        Deletebtn = Button(btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        
        Clearbtn = Button(btn_Frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)
        #detail frame...
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")             
        Detail_Frame.place(x=500,y=100,width=800,height=580)

        lbl_search = Label(Detail_Frame,text= "Search By",bg="crimson",fg="white",font =("times new roman",20,"bold"))
        lbl_search.grid(row=0,column =0,pady=10,padx=10,sticky="w")

        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state ='read only')
        combo_search['value']=("Roll_no","Name","contact")
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        txt_Search = Entry(Detail_Frame,textvariable=self.search_txt,width=10,font =("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_Search.grid(row=0,column=2,padx=20,pady=10,sticky="w")
        searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=20)
        showallbtn=Button(Detail_Frame,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=20)
        #---TableFrame-----
        table_frame = Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        table_frame.place(x=10,y=70,width=760,height=500)
        scroll_x=Scrollbar(table_frame,orient= HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame,columns=("roll","name","email","contact","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("roll",text="RollNo")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("contact",text="Contact")
        self.student_table.heading("Address",text="Address")
        self.student_table['show']='headings'
        self.student_table.column("roll",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("contact",width=100)
        self.student_table.column("Address",width=150)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def add_students(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                 self.name_var.get(), 
                                                                 self.email_var.get(),
                                                                 self.contact_var.get(),
                                                                 self.txt_Address.get('1.0',END)
                                                                 ))
                      
        con.commit()   
        self.fetch_data()
        self.clear()           
        con.close()

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()      
        cur.execute("select * from students")        
        rows=cur.fetchall()                               
        if len(rows)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                        self.student_table.insert('',END,values=row)
                con.commit()
        con.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.contact_var.set("")
        self.txt_Address.delete("1.0",END)

    def get_cursor(self,ev):   
        curosor_row=self.student_table.focus()
        content=self.student_table.item(curosor_row)
        row=content['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.contact_var.set(row[3])
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,row[4])

    def update_data(self):    
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,contact=%s,address=%s where roll_no=%s",(
                                                                 self.name_var.get(), 
                                                                 self.email_var.get(),
                                                                 self.contact_var.get(),
                                                                 self.txt_Address.get('1.0',END),
                                                                 self.Roll_No_var.get()
                                                                 ))


                      
        con.commit()   
        self.fetch_data()
        self.clear()           
        con.close()
    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()      
        cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())        
        con.commit()     
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()      
        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")     
        rows=cur.fetchall()                               
        if len(rows)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                        self.student_table.insert('',END,values=row)
                con.commit()
        con.close()

root = Tk()
ob = Student(root)
root.mainloop()