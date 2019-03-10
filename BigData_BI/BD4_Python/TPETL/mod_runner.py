from mod_reader import jsonreader,csvreader,mysqlreader
from mod_db import insertdata,stagingvalidation,stagingtable


try:
    ##Create and cleanse for staging table
    stagingtable()
    print("=" * 70)
    print("Cleanse in staging table completed")
    print("=" * 70)
    ## Insert Json
    result = jsonreader()
    insertdata(result)
    print("=" * 70)
    print("The JSON file has been loaded successfully")
    print("=" * 70)
    ## Insert CSV
    resultcsv = csvreader()
    insertdata(resultcsv)
    print("=" * 70)
    print("The CSV file has been loaded successfully")
    print("=" * 70)
    ## Insert MySQL
    resultmysql = mysqlreader()
    insertdata(resultmysql)
    print("=" * 70)
    print("The MySQL table has been loaded successfully")
    print("=" * 70)
    print("Staging Validation Result")
    print("=" * 70)
    validation = stagingvalidation()
    for query in validation:
        print('Source type:{}, Qty rows:{}'.format(query["source"],query["count"]))
except:
    print("The data pipeline ETL has failed please contact to the administrator")