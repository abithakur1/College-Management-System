from tkinter import *
from tkinter import messagebox
import back_end.connection
import front_end
from front_end import signup


class log_in:
    def __init__(self, root):
        self.wn = root
        self.wn.title('COLLEGE MANAGEMENT SYSTEM')
        self.wn.geometry('1350x700+0+0')

# =======================================================model object==============================================
        self.dbconnect = back_end.connection.dbconnection()

# ==========================================================heading=====================================================
        heading = Label(self.wn, text=' College Management System', bg='light blue', font=('arial', 20, 'bold'))
        heading.pack(side=TOP, fill=X)

# ==========================================================widgets=====================================================
        lbl_uname = Label(self.wn,text='USER NAME', font=('arial', 20, 'bold'))
        lbl_uname.place(x=550,y=95)

        self.ent_uname = Entry(self.wn,bd=3)
        self.ent_uname.place(x=550,y=145,width=160,height=30)

        lbl_pass = Label(self.wn, text='PASSWORD', font=('arial', 20, 'bold'))
        lbl_pass.place(x=550, y=225)

        self.ent_pass = Entry(self.wn,bd=3,show='*')
        self.ent_pass.place(x=550, y=275, width=160, height=30)

#=======================================================button==========================================================

        btn_login = Button(self.wn, text='LOGIN', font=('arial', 10, 'bold'),width= 12,height =2,bd=3,bg='cyan',
                           command= self.login_click)
        btn_login.place(x=570, y=350)


    def login_click(self):
        if self.ent_uname.get() !='' and self.ent_pass.get()!='':
            query = "select * from login where name = %s"
            val = (self.ent_uname.get(),)
            get = self.dbconnect.select1(query, val)
            value = []
            for i in get[0]:
                value.append(i)

            if value[1] == self.ent_pass.get():
                log_window = Tk()
                front_end.signup.Mainpage(log_window)
                self.wn.destroy()

            else:
                messagebox.showerror("Wrong","Invalid Username or password")

        else:
            messagebox.showerror("Empty","Value can not be empty")


def win():
    root = Tk()
    log_in(root)
    root.mainloop()


if __name__ == '__main__':
  win()