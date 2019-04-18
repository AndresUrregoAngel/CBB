from bs4 import BeautifulSoup
import md_cadindicator as currency
import requests



def reading_from_web():


    try:
        r  = requests.get("https://www.marketwatch.com/investing/currency/usdcad")
        data = r.text
        soup = BeautifulSoup(data , "html.parser")

        metatags = currency.define_metadata()
        record = dict( (tag.attrs['name'], tag.attrs['content'] )for tag in soup.find_all('meta', attrs={"name" : metatags}) )


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
        print("the new read has been added to the file")





if __name__ == "__main__":


    record = reading_from_web()
    feed_dataset(record)