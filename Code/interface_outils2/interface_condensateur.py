"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.1
Date : 21.05.2024
"""

import tkinter
from changement_frame import change_frame
import interface_choix_produit
import trouve_resistance_E12
import trouve_produit_inserer

# récupere les donnée entrer est affiche le résultat
def recuperer_champs(reistance, tao, bouton_rechercher,maitre, text_taille_condensateur):
    condensateur = trouve_produit_inserer.condensateur_inserer(tao, reistance)
    condensateur_reel = 
    text_taille_condensateur.config(text "Votre condensateur sera de :" + condensateur_reel + "et mettra ")
    taille_reistance.config(text = " Si vous cherchez une reistance elle sera de : " + str(resltat_reistance[0]))
    temps_charge_reel_reistance.config(text = " le temps de charge réel sera de  : " + str(resltat_reistance[1]))
    bouton_rechercher.config(command= lambda :(change_frame(maitre, interface_choix_produit.affichage_produit(maitre,1,resltat_reistance[0]))))


def interface_condensateur_outils2(maitre):

    frame = tkinter.Frame(maitre)

    text_temps_charge_condensateur = tkinter.Label(frame, text="Entrez le temps de charge du condensateur : ")
    entrer_temps_charge_condensateur = tkinter.Entry(frame)

    text_resistance = tkinter.Label(frame, text="Entrer la taille de la résistance : ")
    entrer_capaciter = tkinter.Entry(frame)
    bouton_rechercher = tkinter.Button(frame, text="Recherche produit")

    bouton_calculer = tkinter.Button(frame, text="Calculer", command = lambda :(recuperer_champs(
        entrer_temps_charge_condensateur.get(),
        entrer_capaciter.get(),
        text_temps_charge_reel,
        text_taille_condensateur,
        bouton_rechercher,
        maitre
        )))


    text_taille_condensateur = tkinter.Label(frame, text="")
    text_temps_charge_reel = tkinter.Label(frame, text="")

    text_temps_charge_condensateur.grid(row = 1, column = 0)
    entrer_temps_charge_condensateur.grid(row = 1, column = 1)

    text_resistance.grid(row = 2, column = 0)
    entrer_capaciter.grid(row = 2, column = 1)

    bouton_calculer.grid(row = 3, column = 0)
    text_temps_charge_reel.grid(row= 5, column= 0)
    text_taille_condensateur.grid(row=6, column= 0)

    bouton_rechercher.grid(row=7, column= 0)

    return frame