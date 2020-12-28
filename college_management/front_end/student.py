from tkinter import *
from tkinter import ttk
from back_end.connection import dbconnection
from tkinter import messagebox
from front_end import signup
from model.model import students

class Std:
    def __init__(self, root):
        self.wn = root
        self.wn.title("COLLEGE MANAGEMENT SYSTEM")
        self.wn.geometry('1350x700+0+0')
#===================================================connection object===================================================
        self.dbconnect = dbconnection()

# ==================================================all variables=======================================================
        self.st_id = StringVar()
        self.name = StringVar()
        self.batch = StringVar()
        self.sec = StringVar()
        self.contact = StringVar()
        self.email = StringVar()
        self.address = StringVar()
        self.search_text = StringVar()


# ====================================================heading===========================================================
        heading = Label(self.wn, text=' STUDENT  DETAILS', bg='light blue', fg="black", font=('arial', 20, 'bold'))
        heading.pack(side=TOP, fill=X)

# =================================================frame in window======================================================
        frame1 = Frame(self.wn, bd=4, relief=RIDGE, bg='light blue')
        frame1.place(x=20, y=70, width=420, height=590)

        btn_frame = Frame(frame1, bd=4, relief=RIDGE, bg='light blue')
        btn_frame.place(x=10, y=480, width=400)

        frame2 = Frame(self.wn, bd=4, relief=RIDGE, bg='light blue')
        frame2.place(x=450, y=70, width=815, height=590)

        table_frame = Frame(frame2, bd=4, relief=RIDGE, bg='light blue')
        table_frame.place(x=15, y=70, width=790, height=490)

        m_title = Label(frame1, text='Student Details', font=('arial', 20, 'bold', 'underline'), bg='light blue')
        m_title.grid(row=0, columnspan=2, pady=20)

# ================================================widgets in frame1 ====================================================
        lbl_id = Label(frame1, text=' ST_ID: ', font=('arial', 15, 'bold'),bg= 'light blue')
        lbl_id.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.ent_id = Entry(frame1, textvariable=self.st_id, font=('arial', 14, 'bold'), bd=3)
        self.ent_id.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        lbl_name = Label(frame1, text=' NAME: ', font=('arial', 15, 'bold'), bg='light blue')
        lbl_name.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.ent_name = Entry(frame1, textvariable=self.name, font=('arial', 14, 'bold'), bd=3)
        self.ent_name.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        lbl_batch = Label(frame1, text=' BATCH:', font=('arial', 15, 'bold'), bg='light blue')
        lbl_batch.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.combo_batch= ttk.Combobox(frame1, textvariable=self.batch, font=('arial', 13, 'bold'), state='readonly')
        self.combo_batch['values'] = ("2019", "2020", "2021")
        self.combo_batch.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        lbl_sec = Label(frame1, text=' SECTION: ', font=('arial', 15, 'bold'), bg='light blue')
        lbl_sec.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        self.combo_sec = ttk.Combobox(frame1, textvariable=self.sec, font=('arial', 13, 'bold'), state='readonly')
        self.combo_sec['values'] = ("A", "B", "C")
        self.combo_sec.grid(row=4, column=1, padx=10, pady=10, sticky='w')

        lbl_contact = Label(frame1, text=' CONT_NO:', font=('arial', 15, 'bold'), bg='light blue')
        lbl_contact.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        self.ent_contact = Entry(frame1, textvariable=self.contact, font=('arial', 14, 'bold'), bd=3)
        self.ent_contact.grid(row=5, column=1, padx=10, pady=10, sticky='w')

        lbl_email = Label(frame1, text=' EMAIL:', font=('arial', 15, 'bold'), bg='light blue')
        lbl_email.grid(row=6, column=0, padx=10, pady=10, sticky='w')
        self.ent_email = Entry(frame1, textvariable=self.email, font=('arial', 14, 'bold'), bd=3)
        self.ent_email.grid(row=6, column=1, padx=10, pady=10, sticky='w')

        lbl_address = Label(frame1, text=' ADDRESS: ', font=('arial', 15, 'bold'), bg='light blue')
        lbl_address.grid(row=7, column=0, padx=10, pady=10, sticky='w')
        self.ent_address = Entry(frame1, textvariable=self.address, font=('arial', 14, 'bold'), bd=3)
        self.ent_address.grid(row=7, column=1, padx=10, pady=10, sticky='w')

# =============================================button in button frame===================================================
        btn_add = Button(btn_frame, text='ADD', font=('arial', 10, 'bold'), height=2, width=9, bd=2, bg='cyan',
                         fg='black',command=self.add)
        btn_add.grid(row=0, column=0, padx=8, pady=5)

        btn_update = Button(btn_frame, text='UPDATE', font=('arial', 10, 'bold'), height=2, width=9, bd=2, bg='cyan',
                            fg='black',command=self.update)
        btn_update.grid(row=0, column=1, padx=8, pady=5)

        btn_reset = Button(btn_frame, text='RESET', font=('arial', 10, 'bold'), height=2, width=9, bd=2, bg='cyan',
                           fg='black',command=self.reset)
        btn_reset.grid(row=0, column=2, padx=8, pady=5)

        btn_del = Button(btn_frame, text='DELETE', font=('arial', 10, 'bold'), height=2, width=9, bd=2, bg='cyan',
                         fg='black',command=self.delete)
        btn_del.grid(row=0, column=3, padx=8, pady=5)

        btn_back = Button(self.wn, text=' BACK', font=('arial', 10, 'bold'), height=1, width=9, bd=2, bg='cyan',
                          fg="black", command=self.btn_back)
        btn_back.place(x=20, y=40)

# =================================================widgets in frame2====================================================
        lbl_search = Label(frame2, text="Search By", font=('arial', 14, 'bold'), bg='light blue')
        lbl_search.grid(row=0, column=0, padx=10, pady=10)
        self.combo_search = ttk.Combobox(frame2, font=('arial', 11, 'bold'), width=11,state='readonly')
        self.combo_search['values'] = ("st_id")
        self.combo_search.grid(row=0, column=1, padx=10, pady=10)

        self.ent_search = Entry(frame2, font=('arial', 12, 'bold'), bd=3)
        self.ent_search.grid(row=0, column=2, padx=10, pady=10)
        btn_search = Button(frame2, text='SEARCH', font=('arial', 11, 'bold'), width=9, bd=2, bg='cyan', fg='black',
                            command=self.searching)
        btn_search.grid(row=0, column=3, padx=10, pady=10)

        btn_show_all = Button(frame2, text='SHOW ALL', font=('arial', 11, 'bold'), width=9, bd=2, bg='cyan', fg='black'
                              ,command=self.fetch_data)
        btn_show_all.grid(row=0, column=4, padx=10, pady=10)

# =========================================table in table_frame=========================================================
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, columns=(
        "st_id", "name", "batch", "sec", "contact", "email", "address"), xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("st_id", text="ST_ID")
        self.student_table.heading("name", text="NAME")
        self.student_table.heading("batch", text="BATCH")
        self.student_table.heading("sec", text="SECTION")
        self.student_table.heading("contact", text="CONTACT")
        self.student_table.heading("email", text="EMAIL")
        self.student_table.heading("address", text="ADDRESS")
        self.student_table['show'] = 'headings'
        self.student_table.pack()
        self.student_table.column("st_id", width=50)
        self.student_table.column("name", width=150)
        self.student_table.column("batch", width=60)
        self.student_table.column("sec", width=75)
        self.student_table.column("contact", width=110)
        self.student_table.column("email", width=150)
        self.student_table.column("address", width=150)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()
    def add(self):
        if self.ent_id.get() == '' or self.ent_name.get() == '' or self.combo_batch.get() == '' \
                or self.combo_sec.get() == '' or self.ent_contact.get() == '' or self.ent_email.get() == '' \
                or self.ent_address.get() == '':
            messagebox.showerror("Error", "every entry must be filed")
        else:
            obj = students(self.ent_id.get(), self.ent_name.get(), self.combo_batch.get(), self.combo_sec.get(),
                           self.ent_contact.get(), self.ent_email.get(), self.ent_address.get())
            query = 'insert into student values (%s,%s,%s,%s,%s,%s,%s)'
            values = (obj.get_st_id(), obj.get_name(), obj.get_batch(), obj.get_section(), obj.get_contact(),
                      obj.get_email(), obj.get_address())
            self.dbconnect.insert(query,values)
            self.fetch_data()
            self.reset()
            messagebox.showinfo("success", "data inserted successfully")

    def update(self):
        if self.ent_id.get() == '':
            messagebox.showerror("Error","Invalid id for update here")
        else:
            obj = students(self.ent_id.get(), self.ent_name.get(), self.combo_batch.get(), self.combo_sec.get(),
                           self.ent_contact.get(), self.ent_email.get(), self.ent_address.get())
            query = 'update student set name=%s, batch=%s, sec=%s, contact=%s,email=%s address=%s where st_id=%s;'
            values = (obj.get_st_id(), obj.get_name(), obj.get_batch(), obj.get_section(), obj.get_contact(),
                      obj.get_email(), obj.get_address())
            self.dbconnect.insert(query, values)

            self.fetch_data()
            self.reset()
            messagebox.showinfo("success", "data updated successfully")

    def reset(self):
        if self.ent_id.get() == '' and self.ent_name.get() == '' and self.combo_batch.get() == '' \
                and self.combo_sec.get() == '' and self.ent_contact.get() == '' and self.ent_email.get() == '' \
                and self.ent_address.get() == '':
            messagebox.showerror("Error", "Nothing to reset here")
        else:
            self.st_id.set("")
            self.name.set("")
            self.batch.set("")
            self.sec.set("")
            self.contact.set("")
            self.email.set("")
            self.address.set("")

    def delete(self):
        if self.st_id.get() == '':
            messagebox.showerror("Error","Nothing to delete here")
        else:
            obj = students(self.ent_id.get(), self.ent_name.get(), self.combo_batch.get(), self.combo_sec.get(),
                           self.ent_contact.get(), self.ent_email.get(), self.ent_address.get())
            query = 'delete from student where st_id=%s;'
            values = (obj.get_st_id(),)
            self.dbconnect.delete(query, values)
            self.fetch_data()
            self.reset()
            messagebox.showinfo("success", "data deleted successfully")

    def searching(self):
        ent = self.ent_search.get() and self.combo_search.get()
        if ent != "":
            try:
                self.lis = []
                for i in self.student_table.get_children():
                    a = self.student_table.item(i)['values'][0]
                    self.lis.append(a)
                search = self.linearsearch(self.lis, self.ent_search.get())
                if search:
                    query = "select * from student where st_id = %s"
                    values = (search,)
                    a = self.dbconnect.select1(query,values)
                    self.student_table.delete(*self.student_table.get_children())
                    for i in a:
                        self.student_table.insert('', END, values=i)
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
        query = 'select * from student;'
        rows = self.dbconnect.select(query)
        self.search_text.set("")
        if rows != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)

    def get_cursor(self, eve):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        self.st_id.set(row[0])
        self.name.set(row[1])
        self.batch.set(row[2])
        self.sec.set(row[3])
        self.contact.set(row[4])
        self.email.set(row[5])
        self.address.set(row[6])

    def btn_back(self):
        ab_window = Tk()
        signup.Mainpage(ab_window)
        self.wn.destroy()



# root = Tk()
# Std(root)
# root.mainloop()
