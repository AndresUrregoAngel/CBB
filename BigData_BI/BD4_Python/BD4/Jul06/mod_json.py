import json
import requests
# _*_ coding:utf-8 _*_

class phone:
    def __init__(self, mobile, home, office):
        self.mobile = mobile
        self.home = home
        self.office = office





url = "http://www.androidquebec.com/wp-content/uploads/2010/11/contacts.json"
reponse = requests.get(url)
data = reponse.json()
#print(data)
contactlist =data["contacts"]
#print(contactlist)
for temp in contactlist:
    print(temp)
    print("=" * 45)

    for f,v in temp.items():
        print(f,v)



