#_*_ coding:UTF-8 _*_
import sqlite3
import MySQLdb


class ExceptionsDB (Exception):
    def __init__(self,message):
        self.message = message

    def __str__(self):
        return "the command can't be executed due:{}".format(self.message)


db = sqlite3.connect("poc.dbf")
cursor = db.cursor()

n = input("provide the id employee required")

#commdcreate = "create table students (id int, name varhcar(20))"
#commdinsert = "insert into students values (1,'andrw')"
commdread = ('select * from students where id=%s' % (n))

#cursor.execute(commdcreate)
#cursor.execute(commdinsert)
#db.commit()




try:
    cursor.execute(commdread)
    result = cursor.fetchall()
    for line in result:
        print("the id is:{}, and the student name is:{}".format(line[0],line[1]))
        #print(line[0])
        if (line[0]!=2):
            raise ExceptionsDB("the id it's not the expected value")

except ExceptionsDB as v:
        print(v)
except Exception as v:
        print(v)


finally:
    if db != None:
        db.close()







