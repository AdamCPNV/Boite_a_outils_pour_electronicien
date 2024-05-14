"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.2
Date : 13.05.2024
"""
import tkinter
from changement_frame import change_frame
import outils1
import outils2
import outils3
import ajout_fournisseur
import modifier_fournisseur
import supprimer_fournisseur



# permet de differencier quelle outils à été choisi
def changement_menu(maitre, outils):

    match outils:
        case 1:
            change_frame(maitre, outils1.outils1(maitre))
        case 2:
            change_frame(maitre, outils2.outils2(maitre))
        case 3:
            change_frame(maitre, outils3.outils3(maitre))
        case 4:
            change_frame(maitre, ajout_fournisseur.ajouter_fournisseur(maitre))
        case 5:
            change_frame(maitre, modifier_fournisseur.modifier_fournisseur(maitre))
        case 6:
            change_frame(maitre, supprimer_fournisseur.supprimer_fournisseur(maitre))

# affiche l'interface graphique
def choix_des_outils(maitre):
    frame = tkinter.Frame(maitre)
    titre = tkinter.Label(frame, text= "Veuilliez choisire ce que vous voulez faire")
    outils1 = tkinter.Button(frame, text="Dimensionnement d'une résistance dans un montage éà LED", command=lambda : changement_menu(frame, 1))
    outils2 = tkinter.Button(frame, text= "Dimmensionnement de Charge/décharge d'un condensateur", command=lambda : changement_menu(frame, 2))
    outils3 = tkinter.Button(frame, text= "Résistances en série à partir d'une valeur donnée", command=lambda : changement_menu(frame, 3))
    ajouter_fournisseur = tkinter.Button(frame, text="Ajouté un fournisseur", command=lambda : changement_menu(frame, 4))
    modifier_fournisseur = tkinter.Button(frame, text="Modifier les coordonné de un fournisseur", command=lambda : changement_menu(frame, 5))
    supprimer_fournisseur = tkinter.Button(frame, text="Supprimer un fournisseur", command=lambda : changement_menu(frame, 6))

    titre.grid(row = 0, column = 0, columnspan= 2, padx= 5, pady= 5)
    outils1.grid(row = 1,column = 0, columnspan= 2, padx= 5, pady= 5)
    outils2.grid(row = 2, column = 0, columnspan= 2, padx= 5, pady= 5)
    outils3.grid(row = 3, column = 0, columnspan= 2, padx= 5, pady= 5)
    ajouter_fournisseur.grid(row = 4, column = 0, padx= 5, pady= 5)
    modifier_fournisseur.grid(row = 4, column = 1, padx= 5, pady= 5)
    supprimer_fournisseur.grid(row = 5, column= 0, columnspan= 2, padx= 5, pady= 5)
    return frame