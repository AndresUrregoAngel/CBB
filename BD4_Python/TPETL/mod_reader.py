import json
import csv
from mod_db import getmysqlconnection,getmysqlcursor
from mod_client import client,definegender,definecity

def mysqlreader():
##Reading a mysql source to collect data
    ##Scripts Library
    cmdreadtable = "SELECT id,first_name,last_name,email,gender,ville FROM client_data"
    ##Declarate a cursor
    currconn = getmysqlconnection()
    currcurs = getmysqlcursor(currconn)
        ##Create client objects and store them in a list
    resultsql = list()
    currcurs.execute(cmdreadtable)
    source = currcurs.fetchall()
    ##Create objects and store them in a list
    for line in source:
        gender_n= definegender(line["gender"])
        city_n = definecity(line["ville"])
        ObjClient = client(id=line["id"],first_name = line["first_name"],
                       last_name=line["last_name"],email=line["email"],
                       gender=gender_n,city=city_n,source='RDB')
        resultsql.append(ObjClient)

    ##Close cursor connection
    currcurs.close()
    currconn.close()
    return resultsql

def csvreader():
##Reader for csv files
    ##Declare List to store client objects
    ## and open the files
    resultcsv = list()
    with open('week_cust.csv','r') as file:
        next(file)
        reader = csv.reader(file)
    ## Loop to get whole source lines as objects in a list
        for line in reader:
            gender_n=definegender(line[4])
            city_n = definecity(line[5])
            ObjClient = client(id=line[0],first_name = line[1],
                              last_name=line[2],email=line[3],
                              gender=gender_n,city=city_n,source='CSV')
            resultcsv.append(ObjClient)

    return resultcsv

def jsonreader():
##Reader for json files
    ##Open files using json library
    with open('cust_data.json') as file:
        data = json.load(file)
    resultlist = list()
    ## Loop to get whole source lines as objects in a list
    for line in data:
        try:
            gender_n = definegender(line["gender"])
        except KeyError:
            gender_n = 'unknown'
        city_n = definecity(line["ville"])
        ObjClient = client(id=line["id"], first_name=line["first_name"],
                           last_name=line["last_name"], email=line["email"],
                           gender=gender_n, city=city_n,source='JSON')
        resultlist.append(ObjClient)
    return resultlist

