class user:
    def __init__(self,uname,pas):
        self.uname=uname
        self.pas=pas

    def set_uname(self,uname):
        self.uname=uname
    def get_uname(self):
        return self.uname

    def set_pas(self,pas):
        self.pas=pas
    def get_pas(self):
        return self.pas

class students:
    def __init__(self, st_id, name, batch, section, contact, email, address):
        self.st_id = st_id
        self.name = name
        self.batch = batch
        self.section = section
        self.contact = contact
        self.email = email
        self.address = address

    def set_st_id(self, st_id):
        self.st_id = st_id

    def get_st_id(self):
        return self.st_id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_batch(self, batch):
        self.batch = batch

    def get_batch(self):
        return self.batch

    def set_section(self, section):
        self.section = section

    def get_section(self):
        return self.section

    def set_contact(self, contact):
        self.contact = contact

    def get_contact(self):
        return self.contact

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address


class employee:
    def __init__(self, emp_id, name, faculty, qualification, contact, email, address):
        self.emp_id = emp_id
        self.name = name
        self.faculty = faculty
        self.qualification = qualification
        self.contact = contact
        self.email = email
        self.address = address

    def set_emp_id(self, emp_id):
        self.emp_id = emp_id

    def get_emp_id(self):
        return self.emp_id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_faculty(self, faculty):
        self.faculty = faculty

    def get_faculty(self):
        return self.faculty

    def set_qualification(self, qualification):
        self.qualification = qualification

    def get_qualification(self):
        return self.qualification

    def set_contact(self, contact):
        self.contact = contact

    def get_contact(self):
        return self.contact

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address
