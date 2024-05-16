"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.1
Date : 14.05.2024
"""
import tkinter
from integration import IntergationDB

def ajout_fournisseur(nom_fournisseur, addresse_fournisseur, numero_telephone, text_validation):
    bdd = IntergationDB()
    bdd.insertion(nom_fournisseur, addresse_fournisseur, numero_telephone)
    text_validation.config(text = "Le fournisseur {} à bien été ajouter".format(nom_fournisseur))
    



#affiche l'interface graphique
def ajouter_fournisseur(maitre):
    frame = tkinter.Frame(maitre)

    text_nom_fournisseur = tkinter.Label(frame, text = "Entrez le nom du nouveaux fournisseur :")
    entrer_nom_fournisseur = tkinter.Entry(frame)

    text_addresse_fournisseur = tkinter.Label(frame, text= "Entrez l'addresse du nouveaux fournisseur :")
    entrer_addresse_fournisseur = tkinter.Entry(frame)

    text_numero_telephone = tkinter.Label(frame, text= "Entrez le numéro de téléphone du nouveaux fournisseur :")
    entrer_numero_telephone = tkinter.Entry(frame)

    bouton_ajouter = tkinter.Button(frame, text= "Ajouté", command= lambda :(ajout_fournisseur(entrer_nom_fournisseur.get(), entrer_addresse_fournisseur.get(), entrer_numero_telephone.get(), text_validation)))

    text_validation = tkinter.Label(frame, text= "")

    text_nom_fournisseur.grid(row= 0, column= 0)
    entrer_nom_fournisseur.grid(row= 0, column= 1)

    text_addresse_fournisseur.grid(row= 1, column= 0)
    entrer_addresse_fournisseur.grid(row=1, column=1)

    text_numero_telephone.grid(row=2, column= 0)
    entrer_numero_telephone.grid(row=2, column= 1)

    bouton_ajouter.grid(row=3, column= 1)

    text_validation.grid(row=4, column=1)

    return frame