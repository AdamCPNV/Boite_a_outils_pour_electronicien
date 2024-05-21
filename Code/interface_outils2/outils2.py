"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.3
Date : 21.05.2024
"""

import tkinter
from changement_frame import change_frame
import interface_outils2.interface_reistance as resistance
import interface_outils2.interface_condensateur as condensateur
import interface_outils2.interface_temps_charge as tao


#true pour les reistance false pour les condensateur
def choix_mode(mode, frame):
    if mode == 1:
        change_frame(frame, resistance.interface_resistance_outils2(frame))
        
    elif mode == 2:
        change_frame(frame, condensateur.interface_condensateur_outils2(frame))

    elif mode == 3:
        change_frame(frame, tao.interface_tao_outils2(frame))

def outils2(maitre):

    frame = tkinter.Frame(maitre)
    bouton_resistance = tkinter.Button (frame, text="Résistance", command=lambda:choix_mode(1, frame))
    bouton_condensateur = tkinter.Button(frame, text="condensateur", command = lambda:choix_mode(2, frame))
    bouton_tao = tkinter.Button(frame, text= "tao", command= lambda:choix_mode(3, frame))

    bouton_resistance.grid()
    bouton_condensateur.grid()
    bouton_tao.grid()


    return frame