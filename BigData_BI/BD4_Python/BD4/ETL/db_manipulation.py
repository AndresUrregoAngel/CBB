import pymysql.cursors

def insertinfo(info = list()):
    ###########
    #Connect and prepare host table
    ###########
    conn = pymysql.connect(host='localhost',
                       user='root',
                       passwd='',
                       db='northwindmysql',
                       cursorclass = pymysql.cursors.DictCursor)
    cursor_exe = conn.cursor()
    createtable = "CREATE TABLE IF NOT EXISTS POC_Items " \
             "( name varchar(10) NULL, qty int NULL, price float NULL)"

    cursor_exe.execute(createtable)
    cursor_exe.execute("delete from POC_Items")

    #######################
    ### Insert data
    ######################
    inserttable = """INSERT INTO POC_Items VALUES (%s , %s, %s)"""

    for temp in info:
         cursor_exe.execute(inserttable, (temp.nom, temp.qty, temp.prix))
         conn.commit()


    selectcommand = "select name,qty,price from poc_items"
    cursor_exe.execute(selectcommand)
    result = cursor_exe.fetchall()


    for ligne in result:
       print("name:{},qty:{},price:{}".format(ligne['name'],ligne['qty'],ligne['price']))

    conn.close()


