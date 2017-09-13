#import J29_Class as college
from Jun29.J29_Class import  Teacher,Student
'''import Jun29 as fct

#from Jun29 import suma_test

k=int(input("type"))
v=int(input("type"))

print("result:",suma_test(k,v))

#fct.main()
print(fct.calcul_puissa(x=2))
print(fct.calcul_puissa(x=3,y=3))'''

'''
def afficher_donnes (**dicto):
    for k,v in dicto.items():
        print(k,v)

afficher_donnes(nom='angel',prenom='andres',age=30)


print(afficher_donnes())'''


objT = Teacher (nom="angel",prenom="andres",salaire=20000)
objS = Student (nom="angel",prenom="jose",note_finale=4)
#print(type(objT))
#print(objT,objS)

registre = list()
registre.append(objT)
registre.append(objS)
for temp in registre:
    print(temp)
    #objS.venir_college()
    #objT.venir_college()

objS.venir_college()
objT.venir_college()