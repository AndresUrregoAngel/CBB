# _*_ coding:utf-8 _*_
import pymysql.cursors

conn = pymysql.connect(host='localhost',
                       user='root',
                       passwd='',
                       db='northwindmysql',
                       cursorclass = pymysql.cursors.DictCursor)

curseur = conn.cursor()
commande = "SELECT customerID,companyName FROM customers"
curseur.execute(commande)

resultat = curseur.fetchall()
for ligne in resultat:
    print("id:{},company:{}".format(ligne['customerID'],ligne['companyName']))


conn.close()

