# _*_ coding:utf-8 _*_
from ETL.Items import article
from ETL.operations import convert,reduction


#############
# Transform and Read File
#############
def transformation(info):
     itemslist = list()
     for temp in info:
        res = temp.split()
        descrip = convert(res[0])
        newp = reduction(int(res[1]), float(res[2]))
        ObjI = article(nom=descrip, qty=int(res[1]), prix=newp)
        itemslist.append(ObjI)
     return itemslist

