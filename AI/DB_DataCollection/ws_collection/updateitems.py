import sqlite3

### Database management
def create_db():
    sqlite3.connect('items')

    query_createtable = "create table items (" \
                        "description string, quantity int, price float" \
                        ")"



def open_cursor():
    return "tempo"

class items():
    def __init__(self,description,quantity,price):
        self.description = description
        self.quantity = quantity
        self.price = price

    def store_objec_table(self,cursor):

        sqlquery = "insert into items (description,quantity,price)" \
                    "values ({},{},{})".format(self.description,self.quantity,self.price)

        cursor.execute(sqlquery)



def discount(qty,price,qtyv):
    """This method valides the qty and
    assign a discount based on the qty"""
    if qty >= qtyv:
        price = price - (price * 20 /100)

    return price


def upper_case(description):

    return description.upper()


def create_file(payload):
    """Method to create a file based on a
    passed payload"""

    f = open('outputfile.csv','w')
    f.writelines(payload)
    f.close()

    print( "Le fichier outputfile.csvv  est cree avec les donnees requis")



