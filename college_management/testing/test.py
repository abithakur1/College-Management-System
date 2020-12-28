import unittest
from back_end.connection import *
class test_student(unittest.TestCase):
    def setUp(self):
        self.dbconnect=dbconnection()
    def test_insert(self):
        query = 'insert into student values(%s,%s,%s,%s,%s,%s,%s);'
        values= (3,'Rahul','2019','c','9819882545','rahul@gmail.com','kathmandu')
        self.dbconnect.insert(query,values)
        expect=[(3,'Rahul','2019','c','9819882545','rahul@gmail.com','kathmandu')]
        actual=self.dbconnect.select('select * from student where st_id=3')
        self.assertEqual(expect,actual)
    def test_delete(self):
        query='delete from student where st_id=%s;'
        values=(3,)
        self.dbconnect.delete(query,values)
        expect = []
        actual = self.dbconnect.select('select * from student where st_id=3')
        self.assertEqual(expect, actual)
if __name__=="__main__":
    unittest.main()