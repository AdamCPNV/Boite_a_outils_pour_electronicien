"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.5
Date : 30.05.2024
"""

import tkinter
from changement_frame import change_frame
import interface_choix_produit
import trouve_produit_inserer
import choix_outils

def retour(maitre):
    """Retourne au menu précédent

    Args:
        maitre (widget):
    """
    
    change_frame(maitre, choix_outils.choix_des_outils(maitre))

def recuperer_champs(reistance, tao, bouton_rechercher,maitre, text_taille_condensateur):
    """recuperer les champs et affiche le resultat

    Args:
        reistance (int, float)
        tao (int, flaot)
        bouton_rechercher (widget)
        maitre (widget)
        text_taille_condensateur (widget)
    """    """"""
    try:
        tao = float(tao)
        text_taille_condensateur = float(text_taille_condensateur)
    except:
        bouton_rechercher.config(command = "")
        text_taille_condensateur.config(text = """Veuillez entrez: \n 
                             Un nombre composer uniquement de chiffre allant de 0 à 9 \n 
                             Content  si néssaisaire 1 seul point par nombre décimale(pas de virgule) \n Pas de lettre""")
    condensateur = trouve_produit_inserer.condensateur_inserer(float(tao), float(reistance))
    text_taille_condensateur.config(text = "Votre condensateur sera de :" + str(condensateur[0]) + "et sont tao en seconde est de : " + str(condensateur[1]))
    bouton_rechercher.config(command= lambda :(change_frame(maitre, interface_choix_produit.affichage_produit(maitre,2,condensateur[0], taille= condensateur[1]))))


def interface_condensateur_outils2(maitre):
    """Affiche l'interface de calcule du condensateur

    Args:
        maitre (widget)

    Returns:
        frame (widget)
    """

    frame = tkinter.Frame(maitre)

    text_temps_charge_condensateur = tkinter.Label(frame, text="Entrez le Tao (en seonde) du condensateur : ")
    entrer_temps_charge_condensateur = tkinter.Entry(frame)

    text_resistance = tkinter.Label(frame, text="Entrer la taille de la résistance(en Ohm) : ")
    entrer_capaciter = tkinter.Entry(frame)
    bouton_rechercher = tkinter.Button(frame, text="Recherche produit")

    bouton_calculer = tkinter.Button(frame, text="Calculer", command = lambda :(recuperer_champs(
        entrer_capaciter.get(),
        entrer_temps_charge_condensateur.get(),
        bouton_rechercher,
        frame,
        text_taille_condensateur
        )))

    text_taille_condensateur = tkinter.Label(frame, text="")
    text_temps_charge_reel = tkinter.Label(frame, text="")

    bouton_retour = tkinter.Button(frame, text= "Retour", command= lambda:(retour(maitre)))

    text_temps_charge_condensateur.grid(row = 1, column = 0)
    entrer_temps_charge_condensateur.grid(row = 1, column = 1)

    text_resistance.grid(row = 2, column = 0)
    entrer_capaciter.grid(row = 2, column = 1)

    bouton_calculer.grid(row = 3, column = 0)
    text_temps_charge_reel.grid(row= 5, column= 0)
    text_taille_condensateur.grid(row=6, column= 0)

    bouton_rechercher.grid(row=7, column= 0)
    bouton_retour.grid(row=8, column=0)

    return frame