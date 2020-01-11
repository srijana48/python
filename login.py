from tkinter import*
from PIL import ImageTk
class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")

        #---ALL IMAGES----

        self.bg_icone=ImageTk.PhotoImage(file="backg.jpg")
        self.user_icon=PhotoImage(file="person.png")
        self.pass_icon=PhotoImage(file="password.png")
        
        title=Label(self.root,text="Login System",font=("times new roman",40,"bold"))
        title.place(x=0,y=0,relwidth=1)



root=Tk()
obj=Login_System(root)
root.mainloop()

        