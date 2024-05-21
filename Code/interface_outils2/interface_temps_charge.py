"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.1
Date : 21.05.2024
"""

import tkinter
import trouve_produit_inserer
from changement_frame import change_frame
import interface_choix_produit

# récupere les donnée entrer est affiche le résultat
def recuperer_champs( temps_charge_condensateur,  capaciter, taille_reistance, temps_charge_reel_reistance, taille_condensateur, bouton_rechercher,maitre):
    resltat_reistance = trouve_produit_inserer.resistance_inserer(float(temps_charge_condensateur), float(capaciter))
    taille_reistance.config(text = " Si vous cherchez une reistance elle sera de : " + str(resltat_reistance[0]))
    temps_charge_reel_reistance.config(text = " le temps de charge réel sera de  : " + str(resltat_reistance[1]))
    bouton_rechercher.config(command= lambda :(change_frame(maitre, interface_choix_produit.affichage_produit(maitre,1,resltat_reistance[0]))))


def interface_tao_outils2(maitre):

    frame = tkinter.Frame(maitre)

    text_resistance = tkinter.Label(frame, text="Entrez la taile de la résistance : ")
    entrer_resistance = tkinter.Entry(frame)

    text_resistance.grid(column= 0, row=0)
    entrer_resistance.grid(column= 1, row= 0)
    return frame