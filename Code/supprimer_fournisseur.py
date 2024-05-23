"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.1
Date : 16.05.2024
"""
import tkinter
from integration import IntergationDB

def suppression_fournisseur(numero_telephone, text_validation):
    bdd = IntergationDB()
    try:
        bdd.suppertion(numero_telephone)
        text_validation.config(text = "Le fournisseur {} à bien été supprimer".format(numero_telephone))
    except:
        text_validation.config(text = "Entrez uniquement un numero de téléphone composer de nombre sans espace")

#affiche l'interface graphique
def supprimer_fournisseur(maitre):
    frame = tkinter.Frame(maitre)

    text_numero_telephone_fournisseur = tkinter.Label(frame, text = "Entrez le numero de téléphone du fournisseur a supprimer :")
    entrer_numero_telephone_fournisseur = tkinter.Entry(frame)


    bouton_supprimer = tkinter.Button(frame, text= "Supprimer", command= lambda :(suppression_fournisseur(entrer_numero_telephone_fournisseur.get(), text_valdiation)))

    text_valdiation = tkinter.Label(frame, text="")


    text_numero_telephone_fournisseur.grid(row= 0, column= 0)
    entrer_numero_telephone_fournisseur.grid(row= 0, column= 1)

    bouton_supprimer.grid(row=2, column= 1)

    text_valdiation.grid(row=3, column= 1)

    return frame