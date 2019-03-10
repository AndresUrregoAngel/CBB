import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=INF-LAP-187;DATABASE=poc;UID=sqoop;PWD=1234')
cursor = conn.cursor()

commande = "SELECT Name_user,Amount FROM poc"

cursor.execute(commande)
result = cursor.fetchall()

for temp in result:
    print("name:{},amount:{}".format(temp[0],temp[1]))
