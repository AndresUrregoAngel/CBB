import json

class auto:
    def __init__(self,door,transmition,brand,model,color,accessories = {}):
        self.door = door
        self.transmition = transmition
        self.brand = brand
        self.model = model
        self.color = color
        self.accessories = accessories

    def __str__(self):
        return "{},{},{},{},{},{}".format(self.door,self.transmition,self.brand,self.model,self.color,self.accessories)


newobject = auto(door=4,transmition="manual",brand='mazda',model='4x4',color='red',
                 accessories={ "mode_croisiere": False, "toit_ouvrant": True,
                               "option_turbo_chargeurs": 4 })


print(newobject)

newfile = open('autoobject.json','w')
json.dump(vars(newobject),newfile, indent=3 )
newfile.close()