from tkinter import *
from tkinter import ttk
from back_end.connection import *
from tkinter import messagebox
from front_end import signup
from model.model import employee


class Staff:
    def __init__(self, root):
        self.wn = root
        self.wn.title("COLLEGE MANAGEMENT SYSTEM")
        self.wn.geometry('1350x700+0+0')

        # ==============================================model objet=======================================
        self.dbconnect = dbconnection()

        # ==========================================all variable====================================================
        self.emp_id = StringVar()
        self.name = StringVar()
        self.faculty = StringVar()
        self.qualification = StringVar()
        self.contact = StringVar()
        self.email = StringVar()
        self.address = StringVar()
        self.search_by = StringVar()
        self.search_text = StringVar()

# ===================================================heading============================================================
        heading = Label(self.wn, text=' EMPLOYEE  DETAILS', bg='light blue', fg="black", font=('arial', 20, 'bold'))
        heading.pack(side=TOP, fill=X)

# ===============================================frame in window========================================================
        frame1 = Frame(self.wn, bd=4, relief=RIDGE, bg='light blue')
        frame1.place(x=20, y=70, width=420, height=590)

        btn_frame = Frame(frame1, bd=4, relief=RIDGE, bg='light blue')
        btn_frame.place(x=10, y=480, width=400)

        frame2 = Frame(self.wn, bd=4, relief=RIDGE, bg='light blue')
        frame2.place(x=450, y=70, width=815, height=590)

        table_frame = Frame(frame2, bd=4, relief=RIDGE, bg='light blue')
        table_frame.place(x=15, y=70, width=790, height=490)

        m_title = Label(frame1, text='Employee Details', font=('arial', 20, 'bold', 'underline'), bg='light blue')
        m_title.grid(row=0, columnspan=2, pady=20)

# ==================================================widgets in frame1 ==================================================
        lbl_id = Label(frame1, text=' EMP_ID: ', font=('arial', 15, 'bold'), bg='light blue')
        lbl_id.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.ent_id = Entry(frame1, font=('arial', 14, 'bold'), textvariable=self.emp_id, bd=3)
        self.ent_id.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        lbl_name = Label(frame1, text=' NAME: ', font=('arial', 15, 'bold'), bg='light blue')
        lbl_name.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.ent_name = Entry(frame1, font=('arial', 14, 'bold'), textvariable=self.name, bd=3)
        self.ent_name.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        lbl_faculty = Label(frame1, text=' FACULTY:', font=('arial', 15, 'bold'), bg='light blue')
        lbl_faculty.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.combo_faculty = ttk.Combobox(frame1, font=('arial', 13, 'bold'), textvariable=self.faculty,
                                          state='readonly')
        self.combo_faculty['values'] = ("Teacher", "management", "others")
        self.combo_faculty.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        lbl_quali = Label(frame1, text=' QUALI: ', font=('arial', 15, 'bold'), bg='light blue')
        lbl_quali.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        self.ent_quali = Entry(frame1, font=('arial', 14, 'bold'), textvariable=self.qualification, bd=3)
        self.ent_quali.grid(row=4, column=1, padx=10, pady=10, sticky='w')

        lbl_contact = Label(frame1, text=' CONT_NO:', font=('arial', 15, 'bold'), bg='light blue')
        lbl_contact.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        self.ent_contact = Entry(frame1, font=('arial', 14, 'bold'), textvariable=self.contact, bd=3)
        self.ent_contact.grid(row=5, column=1, padx=10, pady=10, sticky='w')

        lbl_email = Label(frame1, text=' EMAIL:', font=('arial', 15, 'bold'), bg='light blue')
        lbl_email.grid(row=6, column=0, padx=10, pady=10, sticky='w')
        self.ent_email = Entry(frame1, font=('arial', 14, 'bold'), textvariable=self.email, bd=3)
        self.ent_email.grid(row=6, column=1, padx=10, pady=10, sticky='w')

        lbl_address = Label(frame1, text=' ADDRESS: ', font=('arial', 15, 'bold'), bg='light blue')
        lbl_address.grid(row=7, column=0, padx=10, pady=10, sticky='w')
        self.ent_address = Entry(frame1, font=('arial', 14, 'bold'), textvariable=self.address, bd=3)
        self.ent_address.grid(row=7, column=1, padx=10, pady=10, sticky='w')

# ==================================================button in button frame==============================================
        btn_add = Button(btn_frame, text='ADD', font=('arial', 10, 'bold'), height=2, width=9, bd=2, bg='cyan',
                         fg='black', command=self.add)
        btn_add.grid(row=0, column=0, padx=8, pady=5)

        btn_update = Button(btn_frame, text='UPDATE', font=('arial', 10, 'bold'), height=2, width=9, bd=2, bg='cyan',
                            fg='black', command=self.update)
        btn_update.grid(row=0, column=1, padx=8, pady=5)

        btn_reset = Button(btn_frame, text='RESET', font=('arial', 10, 'bold'), height=2, width=9, bd=2, bg='cyan',
                           fg='black', command=self.reset)
        btn_reset.grid(row=0, column=2, padx=8, pady=5)

        btn_del = Button(btn_frame, text='DELETE', font=('arial', 10, 'bold'), height=2, width=9, bd=2, bg='cyan',
                         fg='black', command=self.delete)
        btn_del.grid(row=0, column=3, padx=8, pady=5)

        btn_back = Button(self.wn, text=' BACK', font=('arial', 10, 'bold'), height=1, width=9, bd=2, bg='cyan',
                          fg="black",command=self.btn_back)
        btn_back.place(x=20, y=40)

# ==================================================widgets in frame2===================================================
        lbl_search = Label(frame2, text="Search By", font=('arial', 14, 'bold'), bg='light blue')
        lbl_search.grid(row=0, column=0, padx=10, pady=10)
        self.combo_search = ttk.Combobox(frame2, font=('arial', 11, 'bold'), width=11, state='readonly')
        self.combo_search['values'] = ("EMP_ID")
        self.combo_search.grid(row=0, column=1, padx=10, pady=10)

        self.ent_search = Entry(frame2, font=('arial', 12, 'bold'), bd=3)
        self.ent_search.grid(row=0, column=2, padx=10, pady=10)
        btn_search = Button(frame2, text='SEARCH', font=('arial', 11, 'bold'), width=9, bd=2, bg='cyan', fg='black'
                            , command=self.searching)
        btn_search.grid(row=0, column=3, padx=10, pady=10)

        btn_show_all = Button(frame2, text='SHOW ALL', font=('arial', 11, 'bold'), width=9, bd=2, bg='cyan', fg='black'
                              , command=self.fetch_data)
        btn_show_all.grid(row=0, column=4, padx=10, pady=10)

# =========================================table in table_frame=========================================================
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.employee_table = ttk.Treeview(table_frame, columns=(
            "emp_id", "name", "faculty", "quali", "contact", "email", "address"), xscrollcommand=scroll_x.set,
                                           yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)
        self.employee_table.heading("emp_id", text="EMP_ID")
        self.employee_table.heading("name", text="NAME")
        self.employee_table.heading("faculty", text="FACULTY")
        self.employee_table.heading("quali", text="QUALIFICATION")
        self.employee_table.heading("contact", text="CONTACT")
        self.employee_table.heading("email", text="EMAIL")
        self.employee_table.heading("address", text="ADDRESS")
        self.employee_table['show'] = 'headings'
        self.employee_table.pack()
        self.employee_table.column("emp_id", width=50)
        self.employee_table.column("name", width=150)
        self.employee_table.column("faculty", width=100)
        self.employee_table.column("quali", width=125)
        self.employee_table.column("contact", width=110)
        self.employee_table.column("email", width=150)
        self.employee_table.column("address", width=150)
        self.employee_table.pack(fill=BOTH, expand=1)
        self.employee_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add(self):
        if self.ent_id.get() == '' or self.ent_name.get() == '' or self.combo_faculty.get() == '' \
                or self.ent_quali.get() == '' or self.ent_contact.get() == '' or self.ent_email.get() == '' \
                or self.ent_address.get() == '':
            messagebox.showerror("Error", "every entry must be filed")
        else:
            obj = employee(self.ent_id.get(), self.ent_name.get(), self.combo_faculty.get(), self.ent_quali.get(),
                           self.ent_contact.get(), self.ent_email.get(), self.ent_address.get())
            query = 'insert into employee values (%s,%s,%s,%s,%s,%s,%s)'
            values = (obj.get_emp_id(), obj.get_name(), obj.get_faculty(), obj.get_qualification(), obj.get_contact(),
                      obj.get_email(), obj.get_address())
            self.dbconnect.insert(query,values)
            self.fetch_data()
            self.reset()
            messagebox.showinfo("success", "data inserted successfully")

    def update(self):
        if self.ent_id.get() == '':
            messagebox.showerror("Error","Invalid id for update here")
        else:
            obj = employee(self.ent_id.get(), self.ent_name.get(), self.combo_faculty.get(), self.ent_quali.get(),
                           self.ent_contact.get(), self.ent_email.get(), self.ent_address.get())
            query = 'update employee set name=%s, faculty=%s, quali=%s, contact=%s,email=%s address=%s where emp_id=%s;'
            values = (obj.get_emp_id(), obj.get_name(), obj.get_faculty(), obj.get_qualification(), obj.get_contact(),
                      obj.get_email(), obj.get_address())
            self.dbconnect.insert(query, values)
            if obj==values:
                print ('a')
            else:
                self.fetch_data()
                self.reset()
                messagebox.showinfo("success", "data updated successfully")

    def reset(self):
        if self.ent_id.get() == '' and self.ent_name.get() == '' and self.combo_faculty.get() == '' \
                and self.ent_quali.get() == '' and self.ent_contact.get() == '' and self.ent_email.get() == '' \
                and self.ent_address.get() == '':
            messagebox.showerror("Error", "Nothing to reset here")
        else:
            self.emp_id.set("")
            self.name.set("")
            self.faculty.set("")
            self.qualification.set("")
            self.contact.set("")
            self.email.set("")
            self.address.set("")

    def delete(self):
        if self.emp_id.get() == '':
            messagebox.showerror("Error","Nothing to delete here")
        else:
            obj = employee(self.ent_id.get(), self.ent_name.get(), self.combo_faculty.get(), self.ent_quali.get(),
                           self.ent_contact.get(), self.ent_email.get(), self.ent_address.get())
            query = 'delete from employee where emp_id=%s;'
            values = (obj.get_emp_id(),)
            self.dbconnect.delete(query, values)
            self.fetch_data()
            self.reset()
            messagebox.showinfo("success", "data deleted successfully")

    def searching(self):
        ent = self.ent_search.get() and self.combo_search.get()
        if ent != "":
            try:
                self.lis = []
                for i in self.employee_table.get_children():
                    a = self.employee_table.item(i)['values'][0]
                    self.lis.append(a)
                search = self.linearsearch(self.lis, self.ent_search.get())
                if search:
                    query = "select * from employee where emp_id = %s"
                    values = (search,)
                    a = self.dbconnect.select1(query,values)
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in a:
                        self.employee_table.insert('', END, values=i)
                    messagebox.showinfo("Success", "Found")

                else:
                    messagebox.showerror("failed", "Error, Not found")

            except BaseException as m:
                print(m)
                messagebox.showerror("Not Found", "Error, Not found")
        else:
            messagebox.showerror("Failed","'Search' and 'search by:' must by filled")

    def linearsearch(self, lis, x):
        for i in range(len(lis)):
            if int(lis[i]) == int(x):
                return lis[i]
        return False

    def fetch_data(self):
        query='select * from employee;'
        rows= self.dbconnect.select(query)
        self.search_text.set("")
        if rows!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert('', END, values=row)

    def get_cursor(self, eve):
        cursor_row = self.employee_table.focus()
        contents = self.employee_table.item(cursor_row)
        row = contents['values']
        self.emp_id.set(row[0])
        self.name.set(row[1])
        self.faculty.set(row[2])
        self.qualification.set(row[3])
        self.contact.set(row[4])
        self.email.set(row[5])
        self.address.set(row[6])

    def btn_back(self):
        ab_window = Tk()
        signup.Mainpage(ab_window)
        self.wn.destroy()


# root = Tk()
# Staff(root)
# root.mainloop()
