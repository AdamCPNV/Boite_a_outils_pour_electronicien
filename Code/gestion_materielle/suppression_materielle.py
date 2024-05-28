"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.2
Date : 28.05.2024
"""
import tkinter
from integration import IntergationDB

from changement_frame import change_frame
import choix_outils

def retour(maitre):
    change_frame(maitre, choix_outils.choix_des_outils(maitre))

def supprimer_fournisseur(numer_article, text_validation):
    bdd = IntergationDB()
    try:
        bdd.supprimer_produit(numer_article)
        text_validation.config(text = "Le composant {} à bien été supprimer".format(numer_article))
    except:
        text_validation.config(text = "Une erreur c'est produit veuiller reseayer")

#affiche l'interface graphique
def supprimer_materiel(maitre):
    frame = tkinter.Frame(maitre)

    numero_materielle = tkinter.Label(frame, text="Entrer le numero de materielle")
    enter_numero_materielle = tkinter.Entry(frame)
    text_validation = tkinter.Label(frame, text="")

    bouton_supprimer = tkinter.Button(frame, text="supprimer",command=lambda:supprimer_fournisseur(enter_numero_materielle.get(),text_validation))

    bouton_retour = tkinter.Button(frame, text="retour",command=lambda:retour(frame))

    numero_materielle.grid()
    enter_numero_materielle.grid()
    bouton_supprimer.grid()
    bouton_retour.grid()
    text_validation.grid()

    return frame