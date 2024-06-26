"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.3
Date : 30.05.2024
"""
import tkinter
from changement_frame import change_frame
import outils1
import interface_outils2.outils2 as outils2
import outils3
import gestion_fournisseur.ajout_fournisseur as ajout_fournisseur
import gestion_fournisseur.modifier_fournisseur as modifier_fournisseur
import gestion_fournisseur.supprimer_fournisseur as supprimer_fournisseur
import gestion_materielle.ajout_materielle as ajout_materielle
import gestion_materielle.modification_materielle as modification_materielle
import gestion_materielle.suppression_materielle as suppression_materielle



def changement_menu(maitre, outils):
    """Appelle la nouvelle interface graphique en fonction du produit charger

    Args:
        maitre (widget)
        outils (int)
    """

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
        case 7: 
            change_frame(maitre, ajout_materielle.ajouter_materiel(maitre))
        case 8 :
            change_frame(maitre, modification_materielle.modifier_materiel(maitre))
        case 9 :
            change_frame(maitre, suppression_materielle.supprimer_materiel(maitre))

def choix_des_outils(maitre):
    """affiche l'interface graphique de choix de outils

    Args:
        maitre (widget)

    Returns:
        frame (widget)
    """
    frame = tkinter.Frame(maitre)
    titre = tkinter.Label(frame, text= "Veuilliez choisire ce que vous voulez faire")
    outils1 = tkinter.Button(frame, text="Dimensionnement d'une résistance dans un montage éà LED", command=lambda : changement_menu(frame, 1))
    outils2 = tkinter.Button(frame, text= "Dimmensionnement de Charge/décharge d'un condensateur", command=lambda : changement_menu(frame, 2))
    outils3 = tkinter.Button(frame, text= "Résistances en série à partir d'une valeur donnée", command=lambda : changement_menu(frame, 3))
    ajouter_fournisseur = tkinter.Button(frame, text="Ajouté un fournisseur", command=lambda : changement_menu(frame, 4))
    modifier_fournisseur = tkinter.Button(frame, text="Modifier les coordonné de un fournisseur", command=lambda : changement_menu(frame, 5))
    supprimer_fournisseur = tkinter.Button(frame, text="Supprimer un fournisseur", command=lambda : changement_menu(frame, 6))

    ajout_materielle = tkinter.Button(frame, text="Ajouter materielle", command=lambda : changement_menu(frame, 7))
    modifier_materielle = tkinter.Button(frame, text="Modification materielle", command=lambda : changement_menu(frame, 8))
    suppresion_materielle= tkinter.Button(frame, text="Suprression materielle", command=lambda : changement_menu(frame, 9))

    titre.grid(row = 0, column = 0, columnspan= 2, padx= 5, pady= 5)
    outils1.grid(row = 1,column = 0, columnspan= 2, padx= 5, pady= 5)
    outils2.grid(row = 2, column = 0, columnspan= 2, padx= 5, pady= 5)
    outils3.grid(row = 3, column = 0, columnspan= 2, padx= 5, pady= 5)
    ajouter_fournisseur.grid(row = 4, column = 0, padx= 5, pady= 5)
    modifier_fournisseur.grid(row = 4, column = 1, padx= 5, pady= 5)
    supprimer_fournisseur.grid(row = 5, column= 0, columnspan= 2, padx= 5, pady= 5)
    ajout_materielle.grid(row=6, column= 0, padx= 5, pady= 5)
    modifier_materielle.grid(row=6, column=1, padx= 5, pady= 5)
    suppresion_materielle.grid(row=7, column=0, columnspan= 2, padx= 5, pady= 5)

    return frame