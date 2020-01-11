from tkinter import *
from tkinter import ttk
class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        title = Label (self.root,text = "Student Management System",bd = 10,relief = GROOVE,font = ("times new roman",40,"bold"),bg = "yellow",fg = "red")
        title.pack(side=TOP,fill=X)
        manage_Frame=Frame (self.root,bd=4,relief=RIDGE,bg="crimson")
        manage_Frame.place(x=20,y=100,width=450,height=560)
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=100,width=800,height=560)
        m_title= Label(manage_Frame,text="Manage Student",bg="crimson",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20,padx=30)
        lbl_roll=Label(manage_Frame,text="RollNo.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        txt_Roll = Entry(manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")  

        

        lbl_name=Label(manage_Frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        txt_Name = Entry(manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_email=Label(manage_Frame,text="Email",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        txt_Email = Entry(manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10,padx=20,sticky="w")


        

        lbl_contact=Label(manage_Frame,text="Contact",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        txt_Contact = Entry(manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_address=Label(manage_Frame,text="Address",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_address.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        txt_Address = Entry(manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Address.grid(row=6,column=1,pady=10,padx=20,sticky="w")
        
        btn_Frame = Frame(manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=15,y=500,width=420)
        Addbtn = Button(btn_Frame,text="Add",width=10).grid(row=0,column=0,padx=10,pady=10)
        Updatebtn = Button(btn_Frame,text="Update",width=10).grid(row=0,column=1,padx=10,pady=10)
        Deletebtn = Button(btn_Frame,text="Delete",width=10).grid(row=0,column=2,padx=10,pady=10)
        
        Clearbtn = Button(btn_Frame,text="Clear",width=10).grid(row=0,column=3,padx=10,pady=10)
        #detail frame...
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")             
        Detail_Frame.place(x=500,y=100,width=800,height=580)


        lbl_search = Label(Detail_Frame,text= "Search By",bg="crimson",fg="white",font =("times new roman",20,"bold"))
        lbl_search.grid(row=0,column =0,pady=10,padx=10,sticky="w")

        combo_search = ttk.Combobox(Detail_Frame,width=10,font=("times new roman",13,"bold"),state ='read only')
        combo_search['value']=("Roll","Name","contact")
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        txt_search = Entry(Detail_Frame,font =("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,padx=20,pady=10,sticky="w")
        searchbtn=Button(Detail_Frame,text="Search",width=10).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="Show All",width=10,pady=5).grid(row=0,column=4,padx=10,pady=20)

        #---student table---

        
        table_frame = Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        table_frame.place(x=10,y=70,width=760,height=500)
        scroll_x=Scrollbar(table_frame,orient= HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
        student_table =ttk.Treeview(table_frame,columns=("roll","name","email","contact","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=student_table.xview)
        scroll_y.config(command=student_table.yview)

        






root = Tk()       
ob = Student(root)
root.mainloop()