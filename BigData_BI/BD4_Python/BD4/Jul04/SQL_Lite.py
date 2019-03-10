import sqlite3
# _*_ coding:utf-8 _*_

connection = sqlite3.connect("poc.dbf")
cursor = connection.cursor()

cursor.execute(
    """ CREATE TABLE IF NOT EXISTS user_poc (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT,
        age INTERGER
        )
    """
    )
connection.commit()


#cursor.execute("""
#INSERT INTO user_poc(name, age) VALUES(?, ?)""", ("olivier", 30))
#connection.commit()


commande = "SELECT id,name,age FROM user_poc"
cursor.execute(commande)
connection.commit()

user1 = cursor.fetchall()
lecture = cursor.fetchone()

for ligne in user1:
     print("nom:{},age:{}".format(ligne[1],ligne[2]))
 #   for column in ligne:
  #      print(column[0])

