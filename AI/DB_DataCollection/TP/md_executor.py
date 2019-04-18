from bs4 import BeautifulSoup
import md_cadindicator as currency
import requests



def reading_from_web():

    r  = requests.get("https://www.marketwatch.com/investing/currency/usdcad")

    data = r.text
    soup = BeautifulSoup(data , "html.parser")

    metatags = currency.define_metadata()

    record = dict( (tag.attrs['name'], tag.attrs['content'] )for tag in soup.find_all('meta', attrs={"name" : metatags}) )


    print(record)





if __name__ == "__main__":


    reading_from_web()