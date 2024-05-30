"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.4
Date : 30.05.2024
"""

import tkinter
import trouve_produit_inserer
from changement_frame import change_frame
import interface_choix_produit
import choix_outils

def retour(maitre):
    """Retourne au menu précédent

    Args:
        maitre (widget):
    """
    change_frame(maitre, choix_outils.choix_des_outils(maitre))

def recuperer_champs( temps_charge_condensateur,  capaciter, taille_reistance, temps_charge_reel_reistance, bouton_rechercher,maitre):
    """ récupere les donnée entrer est affiche le résultat


    Args:
        temps_charge_condensateur (int, float)
        capaciter (int, flaot)
        taille_reistance (int, flaot)
        temps_charge_reel_reistance (int, float)
        bouton_rechercher (widget)
        maitre (widget)
    """    """"""
    try:
        temps_charge_condensateur = float(temps_charge_condensateur)
        capaciter = float(capaciter)
    except:
        bouton_rechercher.config(command = "")
        taille_reistance.config(text = """Veuillez entrez: \n 
                             Un nombre composer uniquement de chiffre allant de 0 à 9 \n 
                             Content  si néssaisaire 1 seul point par nombre décimale(pas de virgule) \n Pas de lettre""")
        temps_charge_condensateur.config(text = "")
    resltat_reistance = trouve_produit_inserer.resistance_inserer(float(temps_charge_condensateur), float(capaciter))
    taille_reistance.config(text = " La resistence en Ohm sera de : " + str(resltat_reistance[0]))
    temps_charge_reel_reistance.config(text = " le temps de charge réel sera de  : " + str(resltat_reistance[1]))
    bouton_rechercher.config(command= lambda :(change_frame(maitre, interface_choix_produit.affichage_produit(maitre,1,resltat_reistance[0]))))

def interface_resistance_outils2(maitre):
    """Affiche l'interface de calcule de resistance de l'outils 2

    Args:
        maitre (widget)

    Returns:
        frame (widget)
    """

    frame = tkinter.Frame(maitre)

    text_temps_charge_condensateur = tkinter.Label(frame, text="Entrez le TAO : ")
    entrer_temps_charge_condensateur = tkinter.Entry(frame)

    text_capaciter = tkinter.Label(frame, text="Entrez la capacité du condensateur en farad : ")
    entrer_capaciter = tkinter.Entry(frame)
    bouton_rechercher = tkinter.Button(frame, text="Recherche produit")
    text_taille_resitance = tkinter.Label(frame, text="")
    text_taille_condensateur = tkinter.Label(frame, text="")
    text_temps_charge_reel = tkinter.Label(frame, text="")

    bouton_calculer = tkinter.Button(frame, text="Calculer", command = lambda :(recuperer_champs(
        entrer_temps_charge_condensateur.get(),
        entrer_capaciter.get(),
        text_taille_resitance,
        text_temps_charge_reel,
        bouton_rechercher,
        maitre
        )))

    bouton_retour = tkinter.Button(frame, text="Retour", command= lambda:(retour(maitre)))


    text_temps_charge_condensateur.grid(row = 1, column = 0)
    entrer_temps_charge_condensateur.grid(row = 1, column = 1)

    text_capaciter.grid(row = 2, column = 0)
    entrer_capaciter.grid(row = 2, column = 1)

    bouton_calculer.grid(row = 3, column = 0)

    text_taille_resitance.grid(row=4, column= 0)
    text_temps_charge_reel.grid(row= 5, column= 0)
    text_taille_condensateur.grid(row=6, column= 0)

    bouton_rechercher.grid(row=7, column= 0)

    bouton_retour.grid(row=8, column=0)

    return frame