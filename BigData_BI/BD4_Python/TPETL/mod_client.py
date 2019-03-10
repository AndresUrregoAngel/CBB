# _*_ coding:utf-8 _*_

class client:
##Define client object
    def __init__(self,id , first_name,last_name,email,gender,city,source):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.city = city
        self.source = source


    def __str__(self):
        print('{},{},{},{},{},{},{}'.format(int(self.id),str(self.first_name),str(self.last_name),
                                          str(self.email),str(self.gender),str(self.city),str(self.source)))

def definegender(x):
##Garantee and standard the same sex nomenclature for whole sources
    if x is None:
        x = 'unknown'
        return x
    elif (x =='Male') or (x=='Female'):
        return {
         'Male':'M',
         'Female': 'F'
        }.get(x)
    else:
        return x

def definecity(x):
    #Method to validate and garantee the city in each source
    #return x if x is not None else 'city_unknown'
    if x is None or (x =='') or (x==' '):
        x = 'city_unknown'
        return x
    else:
        return x


