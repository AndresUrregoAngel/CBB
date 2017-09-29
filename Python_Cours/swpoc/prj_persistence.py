import csv
#sauvegarde dans un fichier csv
def enregistrer_bmi(nom_fichier, personne):
    file = open(nom_fichier,"a")
    writer = csv.writer(file,quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow( (personne.nom, personne.age, personne.poids,personne.taille) )
    file.close()