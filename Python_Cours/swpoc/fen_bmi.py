from tkinter import *
from  swpoc.prj_traitement_bmi import *
from swpoc.prj_persistence import *
import time
import threading as th



def quit():
    root.destroy()

def load():
    time.sleep(50)

def tload():
    t1 = th.Thread(name='t1',target=load)
    t1.start()
    #t1.join()

def main_calcul():
    # values for poids et taille
    txt_poids = float(poids.get())
    txt_taille = float(taille.get())
    txt_imc=main(txt_poids,txt_taille,"",25)
    imc.config(text="{0:5.2f}".format(txt_imc))

def enregistrer():
    personne=Bmi(nom.get(),int(age.get()),float(poids.get()),float(taille.get()))
    enregistrer_bmi("bmi_annuel.csv", personne)






root=Tk()
root.title("Calcul de l'indice de masse corporelle")
root.geometry("580x350")


mainFrame=Frame(root)

#titre écran
rootfont=('arial', 20, 'bold')
label = Label(mainFrame, text='Saisie des données Patient', font=rootfont)
label.config(height=2, width=40)
label.grid(row=1, column=1)

#section de saisie
bodyFrame=Frame(mainFrame)
Label(bodyFrame, text='Nom').grid(row=1, column=1, sticky=W)
Label(bodyFrame, text='Age').grid(row=2, column=1, sticky=W)
Label(bodyFrame, text='Poids' ).grid(row=3, column=1, sticky=W)
Label(bodyFrame, text='Taille' ).grid(row=4, column=1, sticky=W)
Label(bodyFrame, text='Indice de masse corporelle' ).grid(row=5, column=1, sticky=W)
Label(bodyFrame, text='Risque de santé' ).grid(row=6, column=1, sticky=W)

nom   =Entry(bodyFrame, width=60 )
nom.grid(row=1, column=2, columnspan=4, sticky=W)
age   =Entry(bodyFrame, width=20 )
age.grid(row=2, column=2, columnspan=4, sticky=W)
poids=Entry(bodyFrame, width=20 )
poids.grid(row=3, column=2, columnspan=4, sticky=W)
taille=Entry(bodyFrame, width=20 )
taille.grid(row=4, column=2, columnspan=4, sticky=W)
imc=Label(bodyFrame, width=40 )
imc.grid(row=5, column=2)
risque=Label(bodyFrame, width=50 ).grid(row=6, column=2, columnspan=4, sticky=W)

#boutons
bodyFrame.grid(row=2, column=1, sticky=W)

buttonFrame=Frame(mainFrame, padx=5, pady=5)
ok= Button(buttonFrame, text='Calculer',  command=main_calcul).grid(row=1, column=1,pady=5, padx=5,ipady=5, ipadx=15 )
enregistrer= Button(buttonFrame, text='Enregistrer',  command=enregistrer).grid(row=1, column=2,pady=5, padx=5,ipady=5, ipadx=15)
cancel= Button(buttonFrame, text='Quitter',     command=quit).grid(row=1, column=3,pady=5, padx=5,ipady=5, ipadx=15)
load = Button(buttonFrame, text='Load',    command= tload).grid(row=1, column=4,pady=5, padx=5,ipady=5, ipadx=15)
buttonFrame.grid(row=3, column=1)


mainFrame.grid(row=1, column=1 )
root.mainloop()