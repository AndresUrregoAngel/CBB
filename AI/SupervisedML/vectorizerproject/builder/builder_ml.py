from services.services_ml import services 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import zipfile as zf
import pandas as pd
import numpy as np
import pickle
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

class builder(object):
    
    
    def __init__(self,zipfile):
        self.zipfile = zipfile
        
    
    def loadfilecategories(self):
        
        cleanlist = ['bbcsport/', 'bbcsport/athletics/','bbcsport/cricket/','bbcsport/football/','bbcsport/rugby/','bbcsport/tennis/','bbcsport/README.TXT']
        fathletics = []
        fcricket = []
        ffootball = []
        frugby = []
        ftennis = []  
  
        print(dir_path)
        
        zipfile = dir_path+"/"+self.zipfile
        
        with zf.ZipFile(zipfile) as zipcontent:
            objectslist = zipcontent.namelist()
    
            #Clean the paths I dont need from the root folder
            for element in cleanlist:
              objectslist.remove(element)
            
            # Create a list of files for each category 
            for files in objectslist:
              if "athletics" in files:
                fathletics.append(files)
              elif "cricket" in files:
                fcricket.append(files)
              elif "football" in files:
                ffootball.append(files)
              elif "tennis" in files:
                ftennis.append(files)
              elif "rugby" in files:
                frugby.append(files)
                      
                
            # Insert the file content on the topic list 
            lathletics = []
            for file in fathletics:
              with zipcontent.open(file) as rawdata:
                lathletics.append(rawdata.read())
        
            lcricket = []
            for file in fcricket:
              with zipcontent.open(file) as rawdata:
                lcricket.append(rawdata.read())
        
            lfootball = []
            for file in ffootball:
              with zipcontent.open(file) as rawdata:
                lfootball.append(rawdata.read())    
        
            lrugby = []
            for file in frugby:
              with zipcontent.open(file) as rawdata:
                lrugby.append(rawdata.read())    
        
            ltennis = []
            for file in ftennis:
              with zipcontent.open(file) as rawdata:
                ltennis.append(rawdata.read())
              
              
        # Targets ar deffined as the list      
        target = 1 
        contentlist = [lathletics,lcricket,lfootball,lrugby,ltennis]
        contentdf = []
        for content in contentlist:
            data = {"words":content,"target":target}
            df = pd.DataFrame.from_dict(data)
            contentdf.append(df)
            target += 1
            
        contentfull = pd.concat(contentdf)
          
        return contentfull
        
        
    def buildvectorizer(self,df):
        
        
        vectorizerfile = "vectorizer.pk"
        vectorizerpath = dir_path+"/"+vectorizerfile
        
        
        vectorizer = TfidfVectorizer(stop_words="english",encoding="latin-1",decode_error='strictic',
                               lowercase=True)
                               
                               
        vectorizer.fit(df['words'])
        
        with open(vectorizerpath,"wb") as vfile:
            pickle.dump(vectorizer,vfile)
        
        servicesml = services()
        servicesml.storeons3(vectorizerpath)
        
    
    def transformvector(self,dfull):
        
        vectorizerfile = "vectorizer.pk"
        vectorizerpath = dir_path+"/"+vectorizerfile
        
        servicesml = services()
        servicesml.getfroms3(dir_path)
        
        with open(vectorizerpath,"rb") as vfile:
          vectorizer = pickle.load(vfile)
        
          
        X = vectorizer.transform(dfull['words'])  
        
        columns = ["var{}".format(i) for i in range(X.toarray().shape[1])]
        df = pd.DataFrame(X.toarray(),columns=columns)
        
        #Prepare the target
        nptarget = np.array(dfull['target'])
        print(nptarget.shape)
        df['target'] = nptarget
        
        return df
        
        
        