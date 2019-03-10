# just a test

nom = "toto"
prenom="momo"
age =0
while age <= 0:
    age = int(input("SVP tapez votre age:"))

#test
if age > 10 :
    # age=25
    age = age + 10
else:
    age = age + 5

print("hello1 :{2:12s},hello:{0:20s},age:{1:3d}".format(nom,age,prenom))

