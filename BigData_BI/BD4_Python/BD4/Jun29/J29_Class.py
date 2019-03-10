class personne:
    def __init__(self,nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def venir_college(self):
        print("personne vient à pied")

    def __str__(self):
        return "{},{}".format(self.nom,self.prenom)


class Teacher(personne):
    def __init__(self, nom,prenom,salaire):
        #self.nom = nom
        #self.prenom = prenom
        personne.__init__(self,nom,prenom)
        self.salaire = salaire

    def venir_college(self):
      print("teacher vient en ferrari")

    def donner_devoir(self):
        print("teacher donne devoir")

    def __str__(self):
        return personne.__str__(self)+"{}".format(self.salaire)

#create a teacher

#objT = teacher (nom="angel",prenom="andres",salaire=20000)

#print(type(objT))
#print(objT)

class Student(personne):

    def __init__(self, nom,prenom,note_finale):
        #self.nom = nom
        #self.prenom = prenom
        personne.__init__(self, nom, prenom)
        self.note_finale = note_finale

    #def venir_college(self):
     #   print("student vient en ferrari")

    def faire_devoir(self):
        print("student fait devoir")

    def __str__(self):
        return personne.__str__(self)+" "+"{}".format(self.note_finale)


