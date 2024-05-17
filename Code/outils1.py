"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.2
Date : 13.05.2024
"""
import tkinter
import loi_ohm
from changement_frame import change_frame
import interface_choix_produit

#Recupere les valeurs insérer par l'utilisateur et affiche les résultat

def recuprer_champs(entrer_tension_alimentation, entrer_courent_max, entrer_tension_seuil_led, text_resistance, text_courrant_avec_resistance, text_puissance_dissiper):
    tension_alimentation = float(entrer_tension_alimentation.get())
    courrant_max = float(entrer_courent_max.get())
    tension_seuil_led = float(entrer_tension_seuil_led.get())
    text_resistance.config(text= "Valeur de la résistance a installé :" + str(loi_ohm.resistance_inserer(tension_alimentation,tension_seuil_led,courrant_max)[0]))
    text_courrant_avec_resistance.config(text= "Courant avec la résistance :" + str(loi_ohm.resistance_inserer(tension_alimentation,tension_seuil_led,courrant_max)[1]))
    text_puissance_dissiper.config(text= "Puissance disspé :" + str(loi_ohm.resistance_inserer(tension_alimentation,tension_seuil_led,courrant_max)[2]))

# affiche l'interface graphique
def outils1(maitre):
    frame = tkinter.Frame(maitre)

    frame.rowconfigure(0,weight=5)

    text_tension_alimentation = tkinter.Label(frame, text = "Veuilliez entrez la tension d'allimentaion : ")
    entrer_tension_alimentation = tkinter.Entry(frame)
    text_courent_max = tkinter.Label(frame, text= "Veuillez entrer le courant maximum :")
    entrer_courent_max = tkinter.Entry(frame)
    text_tension_seuil_led = tkinter.Label(frame, text= "Veuillez entrer la tension de seuil de la LED :")
    entrer_tension_seuil_led = tkinter.Entry(frame)
    text_resistance = tkinter.Label(frame, text= "Valeur de la résistance a installé :")
    text_courrant_avec_resistance = tkinter.Label(frame, text= "Courant avec la résistance: ")
    text_puissance_dissiper = tkinter.Label(frame, text="Puissance disspé :")

    bouton_calculer = tkinter.Button(frame,text="Calculer", command = lambda :(recuprer_champs(
        entrer_tension_alimentation,
        entrer_courent_max, 
        entrer_tension_seuil_led,text_resistance,
        text_courrant_avec_resistance, 
        text_puissance_dissiper)))
    
    bouton_recherche = tkinter.Button(frame, text="Recherche produit", command= lambda :(change_frame(maitre, interface_choix_produit.affichage_produit(maitre,1, 1.1, 1.2))))

    text_tension_alimentation.grid(row=0,column=0, sticky="n")
    entrer_tension_alimentation.grid(row=0, column=1, sticky="n")

    text_courent_max.grid(row=1,column=0, sticky="n")
    entrer_courent_max.grid(row=1, column=1, sticky="n")

    text_tension_seuil_led.grid(row=2,column=0, sticky="n")
    entrer_tension_seuil_led.grid(row = 2, column = 1, sticky="n")

    bouton_calculer.grid(row=4, column=2, padx= 10)

    text_resistance.grid(row=5,column=0, sticky="n")

    text_courrant_avec_resistance.grid(row=6,column=0, sticky="n")

    text_puissance_dissiper.grid(row = 7, column= 0, sticky= "n")

    bouton_recherche.grid(row=8, column=1, sticky="n")

    return frame