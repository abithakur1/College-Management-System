import mysql.connector


class dbconnection:
    def __init__(self):
        self.con = mysql.connector.connect(host="localhost", user="root", password="20002511",
                                           database="college_management")
        self.cursor = self.con.cursor()

    def insert(self, query, values):
        self.cursor.execute(query, values)
        self.con.commit()

    def update(self, query, values):
        self.cursor.execute(query, values)
        self.con.commit()

    def delete(self, query, values):
        self.cursor.execute(query, values)
        self.con.commit()

    def select(self, query):
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        self.con.commit()
        return records

    def select1(self, query, values):
        self.cursor.execute(query, values)
        records = self.cursor.fetchall()
        self.con.commit()
        return records
