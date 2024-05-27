"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.1
Date : 23.05.2024
"""
import tkinter
from integration import IntergationDB

from changement_frame import change_frame
import choix_outils

def retour(maitre):
    change_frame(maitre, choix_outils.choix_des_outils(maitre))

def ajout_fournisseur(nom_fournisseur, addresse_fournisseur, numero_telephone, text_validation):
    bdd = IntergationDB()
    try:
        bdd.insertion(nom_fournisseur, addresse_fournisseur, numero_telephone)
        text_validation.config(text = "Le fournisseur {} à bien été supprimer".format(nom_fournisseur))
    except:
        text_validation.config(text = "Entrez un numero de téléphone uniquement composer de chiffre sans espace")

#affiche l'interface graphique
def supprimer_materiel(maitre):
    frame = tkinter.Frame(maitre)

    numero_materielle = tkinter.Label(frame, text="Entrer le numero de materielle")
    enter_numero_materielle = tkinter.Entry(frame)

    bouton_supprimer = tkinter.Button(frame, text="supprimer")

    bouton_retour = tkinter.Button(frame, text="retour",command=lambda:retour(frame))

    numero_materielle.grid()
    enter_numero_materielle.grid()
    bouton_supprimer.grid()
    bouton_retour.grid()

    return frame