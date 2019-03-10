# _*_ coding:utf-8 _*_
from ETL.Items import article
from ETL.operations import convert,reduction
import pymysql.cursors

conn = pymysql.connect(host='localhost',
                       user='root',
                       passwd='',
                       db='northwindmysql',
                       cursorclass = pymysql.cursors.DictCursor)
cursor_exe = conn.cursor()
createtable = "CREATE TABLE IF NOT EXISTS POC_Items " \
             "( name varchar(10) NULL, qty int NULL, price float NULL)"


cursor_exe.execute(createtable)

#####
#EXTRACT AND TRANSFORMATION
####

itemslist = list()
files = open("C:/Users/axu30/PycharmProjects/BD4/files/data.txt")
for temp in files:
    res=temp.split()
    descrip = convert(res[0])
    newp = reduction(int(res[1]),float(res[2]))
    ObjI = article (nom = descrip,qty=int(res[1]),prix =newp)
    itemslist.append(ObjI)





cursor_exe.execute("delete from POC_Items")
inserttable = """INSERT INTO POC_Items VALUES (%s , %s, %s)"""

########
##LOAD IN RDBSM MYSQL
####
for temp in itemslist:
     cursor_exe.execute(inserttable, (temp.nom, temp.qty, temp.prix))
     conn.commit()
     #print(temp.nom)



selectcommand = "select name,qty,price from poc_items"
cursor_exe.execute(selectcommand)
result = cursor_exe.fetchall()

for ligne in result:
    print("name:{},qty:{},price:{}".format(ligne['name'],ligne['qty'],ligne['price']))

conn.close()




