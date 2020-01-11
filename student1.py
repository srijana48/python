from tkinter import *
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
root = Tk()       
ob = Student(root)
root.mainloop()