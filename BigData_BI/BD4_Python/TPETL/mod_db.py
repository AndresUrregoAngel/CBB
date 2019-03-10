# _*_ coding:utf-8 _*_
import pyodbc
import pymysql.cursors

def getmysqlconnection():
    ##Define a new cursor for Mysql on DB northwindmysql
    conn = pymysql.connect(host='localhost',
                           user='root',
                           passwd='',
                           db='northwindmysql',
                           cursorclass=pymysql.cursors.DictCursor)
    conn.autocommit = True
    newconenction = conn
    return newconenction

def getmysqlcursor(mysqlconnection):
## Using a connection create the cursor
    cursormysql = mysqlconnection.cursor()
    return cursormysql

def stagingtable():
    ##Call cursor method to open a new connection
    currconn = getmysqlconnection()
    currcurs = getmysqlcursor(currconn)
    ##Create the staging BI table
    cmdcreatetable = "CREATE TABLE IF NOT EXISTS client_all ( " \
                 "internal_id INT NOT NULL  PRIMARY KEY  AUTO_INCREMENT," \
                 "source_id INT NULL, first_name nvarchar(50) NULL,last_name nvarchar(50) NULL,"\
                 "email nvarchar(50) NULL, gender nvarchar(50) NULL,city nvarchar(100) NULL , source nvarchar(20) NULL)"
    cmdcleanse = '''DELETE FROM client_all'''
    ##Execute the creation action
    currcurs.execute(cmdcreatetable)
    currcurs.execute(cmdcleanse)
    currconn.commit()
    ##Close the current connection after complete last statement
    currcurs.close()
    currconn.close()

def insertdata(resultlist):
##Store new data in staging BI table
    ## Open a cursor connection
    currconn = getmysqlconnection()
    currcurs = getmysqlcursor(currconn)
    ##Scripts library
    cmdinsert ='''INSERT INTO client_all (source_id,first_name,last_name,email,gender,city,source)
    VALUES (%s,%s,%s,%s,%s,%s,%s)'''
    ##Perform the insert
    for line in resultlist:
        currcurs.execute(cmdinsert,(line.id,line.first_name,line.last_name,
                                    line.email,line.gender,line.city,line.source))
        currconn.commit()

    ##close the DB connection
    currcurs.close()
    currconn.close()

def stagingvalidation():
##Methode to validate if the staging table is populated
    ## Open a cursor connection
    currconn = getmysqlconnection()
    currcurs = getmysqlcursor(currconn)
    ##Scripts library
    cmdquery = "SELECT source,count(*) as count FROM client_all GROUP BY source"
    currcurs.execute(cmdquery)
    result = currcurs.fetchall()
    ##Return the resultset in a list
    resultset = list()
    for line in result:
        resultset.append(line)
    ##Close DB connection
    currcurs.close()
    currconn.close()

    return resultset

