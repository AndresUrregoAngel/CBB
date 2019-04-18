from bs4 import BeautifulSoup
import md_cadindicator as currency
import requests
import boto3


def reading_from_web():
    try:
        r  = requests.get("https://www.marketwatch.com/investing/currency/usdcad")
        data = r.text
        soup = BeautifulSoup(data , "html.parser")

        metatags = currency.define_metadata()
        record = dict( (tag.attrs['name'], tag.attrs['content'] )for tag in soup.find_all('meta', attrs={"name" : metatags}) )

        print("The data has been for renewal has been downloaded succesfully")

    except Exception as error:
        print("There was an error reading the data from the website: {}".
              format(error))

    finally:
        return record




def feed_dataset(record):
    try:

        newline = currency.indicator(record["name"],record["description"],record["price"],record["priceChange"],
                                     record["priceChangePercent"],record["priceCurrency"],record["exchangeTimezone"]
                                     ,record["url"],record["quoteTime"])

        newline.feed_dataset()

    except Exception as error:
        print("The flow has stopped due to an error: {}"
              .format(error))

    finally:
        print("The new read has been added to the file")



def get_current_dataset():
    try:
        client = boto3.resource('s3')

        bucket='poc-developers'
        key='dataset.csv'

        client.Object(bucket,key).download_file(key)
        print("The current dataset has moved to a local level")

    except Exception as error:

        print("The flow has stopped due to an error: {}"
              .format(error))



def update_dataset():
    try:
        client = boto3.resource('s3')

        bucket='poc-developers'
        key='dataset.csv'

        client.Object(bucket,key).upload_file(key)

        print("The dataset has been updated into the S3 area")

    except Exception as error:

        print("The flow has stopped due to an error: {}"
              .format(error))



if __name__ == "__main__":

    #Pipeline
    print("*"*10+"Read data from website"+"*"*10)
    record = reading_from_web()
    print("*"*10+"Bring the current dataset status"+"*"*10)
    get_current_dataset()
    print("*"*10+"Append a new record within the dataset"+"*"*10)
    feed_dataset(record)
    print("*"*10+"Move the new dataset to the storage area S3"+"*"*10)
    update_dataset()