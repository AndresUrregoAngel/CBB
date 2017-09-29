class Bmi:
    #liste de classification
    CLASSIFICATION = ["Poids insuffisant","Poids normal","Excès de poids","Obésité, classe I","Obésité, classe II","Obésité, classe III"]
    RISQUE=["Accru","Moindre","Accru","Élevé","Très élevé","Extrêmement élevé"]

    def __init__(self, nom, age, poids, taille):
        self.nom = nom
        self.age = age
        self.poids = poids
        self.taille = taille

    def __str__(self):
        return "nom: {0:<10} et age:{1:2d}".format(self.nom ,self.age)