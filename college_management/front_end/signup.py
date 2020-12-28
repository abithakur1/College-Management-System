from tkinter import *
from tkinter import messagebox

from back_end.connection import dbconnection
from front_end import login, employee, student
from model.model import user


class Mainpage:
    def __init__(self,root):
        self.wn=root
        self.wn.title('HOSPITAL MANAGEMENT SYSTEM')
        self.wn.geometry('1350x700+0+0')

#=======================================================connection======================================================
        self.dbconnect = dbconnection()

#==========================================all variable====================================================
        self.uname = StringVar()
        self.pas = StringVar()

#========================================================frmae==========================================================
        frame1 = Frame(self.wn, bd=4, relief=RIDGE, bg='light blue')
        frame1.place(x=20, y=40, width=550, height=590)

        m_title = Label(frame1, text='Select Any One', font=('arial', 20, 'bold', 'underline'), bg='light blue')
        m_title.place(x=170,y=40)

        btn_frame = Frame(frame1, relief=RIDGE, bg='light blue')
        btn_frame.place(x=10, y=450, width=520,height=80)

        frame2 = Frame(self.wn, bd=4, relief=RIDGE, bg='light blue')
        frame2.place(x=620, y=40, width=620, height=590)

        m_title = Label(frame2, text='Sign Up For New User', font=('arial', 20, 'bold', 'underline'), bg='light blue')
        m_title.place(x=170, y=40)

#===================================================frame1 button=======================================================
        btn_st = Button(frame1, text='STUDENT', font=('arial', 12, 'bold'), width=16, height=2, bd=4, bg= 'cyan',
                        command=self.stu)
        btn_st.place(x=185,y=120)

        btn_emp = Button(frame1, text='EMPLOYEE', font=('arial', 12, 'bold'), width=16, height=2, bd=4, bg='cyan',
                         command=self.employee)
        btn_emp.place(x=185, y=220)

        btn_exit = Button(btn_frame, text='EXIT', font=('arial', 10, 'bold'), width=10, height=2, bd=4, bg='crimson',
                          command=self.exit_btn)
        btn_exit.place(x=50, y=10)

        btn_out = Button(btn_frame, text='LOG OUT', font=('arial', 10, 'bold'), width=10, height=2, bd=4, bg='crimson',
                         command=self.logout)
        btn_out.place(x=350, y=10)

#==================================================frame2 widgets=======================================================

        lbl_uname = Label(frame2, text='USER NAME', font=('arial', 20, 'bold'), bg='light blue')
        lbl_uname.place(x=240, y=125)

        self.ent_uname = Entry(frame2,textvariable=self.uname, bd=3)
        self.ent_uname.place(x=245, y=170, width=160, height=30)

        lbl_pass = Label(frame2, text='PASSWORD', font=('arial', 20, 'bold'), bg='light blue')
        lbl_pass.place(x=240, y=235)

        self.ent_pas = Entry(frame2,textvariable=self.pas, bd=3)
        self.ent_pas.place(x=245, y=275, width=160, height=30)

# ==================================================frame2 button=======================================================
        btn_add = Button(frame2, text='SIGN UP', font=('arial', 12, 'bold'), width=8, height=2, bd=5, bg='cyan',
                         command=self.add)
        btn_add.place(x=100, y=400)

        btn_clear = Button(frame2, text='CLEAR', font=('arial', 12, 'bold'), width=8, height=2, bd=5, bg='cyan',
                           command=self.clear_btn)
        btn_clear.place(x=400, y=400)


    def stu(self):
        study_window = Tk()
        student.Std(study_window)
        self.wn.destroy()

    def employee(self):
        about_window=Tk()
        employee.Staff(about_window)
        self.wn.destroy()

    def exit_btn(self):
        self.wn.destroy()

    def logout(self):
        log_window=Tk()
        login.log_in(log_window)
        self.wn.destroy()

    def add(self):
        if self.ent_uname.get() == '' or self.ent_pas.get() == '':
            messagebox.showerror("Error", "User_Name and Password must be needed")
        else:
            obj = user(self.ent_uname.get(), self.ent_pas.get())
            query = 'insert into login values (%s,%s);'
            values = (obj.get_uname(), obj.get_pas())
            self.dbconnect.insert(query, values)
            messagebox.showinfo("success", "new user are added successfully")

    def clear_btn(self):
        if self.ent_uname.get() == '' and self.ent_pas.get() == '':
            messagebox.showerror("Error", "Nothing to clear here")
        else:
            self.uname.set("")
            self.pas.set("")

# root=Tk()
# Mainpage(root)
# root.mainloop()