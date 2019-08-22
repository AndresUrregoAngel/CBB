from builder.builder_ml import builder
import pandas as pd 
import numpy as np





def createvectorizer():
    
    zipfile = "bbcsport-fulltext.zip"
    modelbuilder = builder(zipfile)

    df = modelbuilder.loadfilecategories()
    modelbuilder.buildvectorizer(df)


# modelbuilder.transformvector()