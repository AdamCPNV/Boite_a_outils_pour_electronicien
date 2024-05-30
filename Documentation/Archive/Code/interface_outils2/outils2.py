"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.4
Date : 30.05.2024
"""

import tkinter
from changement_frame import change_frame
import interface_outils2.interface_reistance as resistance
import interface_outils2.interface_condensateur as condensateur
import interface_outils2.interface_temps_charge as tao
import choix_outils

def retour(maitre):
    """Retourne au menu précédent

    Args:
        maitre (widget):
    """
    change_frame(maitre, choix_outils.choix_des_outils(maitre))

def choix_mode(mode, frame):
    """peremt de choisir ce que l'on veux calculer

    Args:
        mode (int)
        frame (widget)
    """
    if mode == 1:
        change_frame(frame, resistance.interface_resistance_outils2(frame))
        
    elif mode == 2:
        change_frame(frame, condensateur.interface_condensateur_outils2(frame))

    elif mode == 3:
        change_frame(frame, tao.interface_tao_outils2(frame))

def outils2(maitre):
    """permet de choisir le type de valeur que l'on souaite calculer

    Args:
        maitre (widget)

    Returns:
        frame (widget)
    """
    frame = tkinter.Frame(maitre)
    bouton_resistance = tkinter.Button (frame, text="Résistance", command=lambda:choix_mode(1, frame))
    bouton_condensateur = tkinter.Button(frame, text="condensateur", command = lambda:choix_mode(2, frame))
    bouton_tao = tkinter.Button(frame, text= "tao", command= lambda:choix_mode(3, frame))
    bouton_retour = tkinter.Button(frame, text="Retour", command= lambda:(retour(maitre)))

    bouton_resistance.grid(row = 0, column=0)
    bouton_condensateur.grid(row=0, column=1)
    bouton_tao.grid(row=1, column=0)
    bouton_retour.grid(row=1, column=1)

    return frame