
class indicator ():
    def __init__(self,name, description, price, priceChange,priceChangePercent, priceCurrency, exchangeTimezone,url,quoteTime):
        self.name = name
        self.description = description
        self.price = price
        self.priceChange = priceChange
        self.priceChangePercent = priceChangePercent
        self.priceCurrency = priceCurrency
        self.exchangeTimezone = exchangeTimezone
        self.url = url
        self.quoteTime = quoteTime


    def feed_dataset(self):


        attrs = vars(self)
        line = ( ','.join(v for v in attrs.values()))
        with open("dataset.csv","a+") as f:
            f.write(str(line)+"\n")

            f.close()


def define_metadata ():

    try:
        objecti = indicator('','','','','','','','','')
        fields = [f for f in objecti.__dict__.keys()]

    except Exception as error:
        print("The reader has gotten an error: {}".format(error))

    finally:
        return fields