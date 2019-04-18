



class indicator ():
    def __init__(self,name, description, price, priceChange,priceChangePercen, priceCurrency, exchangeTimezone,url,quoteTime):
        self.name = name
        self.description = description
        self.price = price
        self.priceChange = priceChange
        self.priceChangePercen = priceChangePercen
        self.priceCurrency = priceCurrency
        self.exchangeTimezone = exchangeTimezone
        self.url = url
        self.quoteTime = quoteTime



def define_metadata ():

    try:

        objecti = indicator('','','','','','','','','')
        fields = [f for f in objecti.__dict__.keys()]

    except Exception as error:
        print("The reader has gotten an error: {}".format(error))

    finally:
        return fields