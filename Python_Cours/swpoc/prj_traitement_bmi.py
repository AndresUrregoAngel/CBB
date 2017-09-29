from swpoc.prj_bmi import Bmi

#calcul BMI-IMC avec validation de saisie de taille

def saisie_valeur(message):
    valeur = float(input(message))
    return valeur

# afficher imc
def afficher_valeur(imc):
    print("Votre imc est:{0:5.2f}".format (imc))

#afficher la classification
def afficher_classification(imc):
    if imc< 18.5:
        print("Classification:,",Bmi.CLASSIFICATION[0])
        print("Risque:",Bmi.RISQUE[0])
    elif imc <24.9:
        print("Classification:,",Bmi.CLASSIFICATION[1])
        print("Risque:",Bmi.RISQUE[1])
    elif imc<29.9:
        print("Classification:,",Bmi.CLASSIFICATION[2])
        print("Risque:",Bmi.RISQUE[2])
    elif imc<34.9:
        print("Classification:,",Bmi.CLASSIFICATION[3])
        print("Risque:",Bmi.RISQUE[3])
    elif imc<39.9:
        print("Classification:,",Bmi.CLASSIFICATION[4])
        print("Risque:",Bmi.RISQUE[4])
    else:
        print("Classification:,",Bmi.CLASSIFICATION[5])
        print("Risque:",Bmi.RISQUE[5])


def calcul_imc(personne):
    #calcul avec validation
    imc = personne.poids / (personne.taille * personne.taille)
    return imc


def main(poids,taille, nom="snp", age=25):
       #cr�er objet
    pers= Bmi(nom,age,poids,taille)
    #calcul imc et affichage
    imc = calcul_imc(pers)
    return imc
    #afficher_valeur(imc)
    #afficher classification
    #afficher_classification(imc)
    #print Bmi
    #print(pers)

