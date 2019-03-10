
from ETL.file_manipulation import transformation
from ETL.db_manipulation import insertinfo

#################
######  Trigger Main
#################

file = open("C:/Users/axu30/PycharmProjects/BD4/files/data.txt")
#print(file)

#result = list()
result = transformation(file)

insertinfo(result)




