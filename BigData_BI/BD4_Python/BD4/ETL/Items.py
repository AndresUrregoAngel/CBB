# _*_ coding:utf-8 _*_

class article:
    def __init__(self, nom: object, qty: object, prix: object) -> object:

        self.nom = nom
        self.qty = qty
        self.prix =prix



    def __str__(self):
        return "{},{},{}".format(self.nom,self.qty, self.prix)

