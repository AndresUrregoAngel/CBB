class patient: 

    def __init__(self,highest,weight,name,age):
        self.highest = highest
        self.weight = weight
        self.name = name
        self.age = age

    def __str__ (self):
        return ("le processus de create de patient {} est reussi".
        format(self.name))


    def calculateimc(self):
        imc = int(self.weight)  / pow(float(self.highest),2)       
        
        if imc < 18.5 :
            print("Attention!! {} votre poids il est vriament insuffisant".format(self.name))
        elif imc > 18.5 and imc < 25:
            print("{}, votre poids est normal".format(self.name))
        elif imc > 25 and  imc < 30:
            print("{}, vous avez exces de poids".format(self.name))
        elif imc >30 and imc < 35:
            print("{}, vous est considere comme obese classe I".format(self.name))
        elif imc > 35 and imc < 40 :
            print("{}, vous est considere comme obese classe II".format(self.name))
        elif imc >= 40 : 
            print("{}, vous est considere comme obese classe III".format(self.name))


def request_userinfo():
    highest = input("saisez votre taille (m):")
    weight = input("saisez votre poids (kg):")
    name = input("s'il vous plait saisez aussi votre nom:")
    age= input("finalment saisez votre age:")

    patientinfo = patient(highest,weight,name,age)
    patientinfo.calculateimc()


if __name__ == '__main__':

    request_userinfo()
