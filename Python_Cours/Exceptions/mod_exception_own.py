class ValeueNotAllowed(Exception):
    def __init__(self,message,val):
        self.message = message
        self.val = val

    def __str__(self):
        return "Stop:{} et valeur: {}".format(self.message,self.val)