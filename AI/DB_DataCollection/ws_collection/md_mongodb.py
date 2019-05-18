from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests
from datetime import datetime as dt
import pprint as p
import datetime



def validate_content(url):
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data , "html.parser")
    content = soup.get_text
    payload = str(content).lower().split()

    counter = 0

    for word in payload:
        if 'intelligence' in word:
            counter += 1

    return  counter


def insert_mongo(client,qtyword,url):

    if qtyword > 1:

        document = {
            "url" : url,
            "word_repetions" : qtyword,
            "timestamp" : dt.now()
        }

        db = client.db.final_exam

        post_id = db.insert_one(document).inserted_id
        print("The element has been stored {}".format(post_id))

    else:
        print("The number of repetitions for the word is not greater than 1")
        # print(client.list_database_names())



def db_scan_document(client):

    db = client.db.final_exam
    for document in db.find():
        print(document['timestamp'])


def db_scan_document_timestamp(client,date_param):

    db = client.db.final_exam
    for document in db.find({'timestamp': date_param}):
        print( document)


if __name__ == '__main__':

    client = MongoClient()

    urls = ['https://www.popsci.com/technology','https://www.science-et-vie.com/cerveau-et-intelligence','https://www.zdnet.com/']

    # for url in urls:
    #
    #     #Execute web scrapping
    #     qtyword = validate_content(url)
    #
    #     #Validate the insert of findings
    #     insert_mongo(client,qtyword,url)

    # db_scan_document(client)

    #Get a list of documents based on a timestamp
    date_param = dt.now()- datetime.timedelta(minutes=15)
    db_scan_document_timestamp(client,date_param)

