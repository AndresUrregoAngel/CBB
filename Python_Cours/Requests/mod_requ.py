#_*_ codig:UTF-8 _*_
import requests
import json

'''
#Example reading a json file and edit it before save it

fichier=open('voiture.json')
data = json.load(fichier)

fichier.close()

data['voiturette']['couleur'] = 'Noir'

newfile= open('voiturenew.json','w')
json.dump(data, newfile, indent=3)

newfile.close()
'''

'''
with open ("stations.json") as n:
    data = json.load(n)

for k,v in data.items():
   if k != 'stations':
        print(v)
   else:
       for k,v in data.items():
           print(v.['stations'].id)
'''



file = "http://www.androidquebec.com/wp-content/uploads/2010/11/contacts.json"
data = requests.get(file)
datafinal = data.json()
#print(datafinal)
result = datafinal["contacts"]

for k in result:
    print(k['id'])

