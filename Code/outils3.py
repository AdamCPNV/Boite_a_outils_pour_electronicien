"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.2
Date : 21.05.2024
"""

import tkinter
import trouve_resistance_serie
from changement_frame import change_frame
import interface_choix_produit

def recupere_champs(entrer_total_resistance_serie, text_resultat, bouton_rechercher, maitre):
    valeur_rechercher = float(entrer_total_resistance_serie.get())
    resultat = trouve_resistance_serie.trouve_paire_resistance(valeur_rechercher)
    text_resultat.config(text = " Les résistances trouvé sont " + str(resultat[0]) + " et " + str(resultat[1]))
    bouton_rechercher.config(command= lambda :(change_frame(maitre, interface_choix_produit.affichage_produit(maitre,1,resultat[0], resultat[1]))))

# affiche l'interface graphique
def outils3(maitre):

    frame = tkinter.Frame(maitre)
    
    text_total_resitance_serie = tkinter.Label(frame, text = "Quelle valeur de résistance en serie voulez vous optenir :")
    entrer_total_resistance_serie = tkinter.Entry(frame)
    bouton_rechercher = tkinter.Button(frame, text= "Rechercher produit")
    bouton_calculer = tkinter.Button(frame, text = "calculer", command= lambda : recupere_champs(entrer_total_resistance_serie,text_resultat, bouton_rechercher, frame))

    text_resultat = tkinter.Label(frame, text = "")




    text_total_resitance_serie.grid(row = 0, column = 0)
    entrer_total_resistance_serie.grid(row = 0, column = 1)
    bouton_calculer.grid(row = 1, column = 2)
    text_resultat.grid(row  = 2, column = 0)
    bouton_rechercher.grid(row = 3, column = 0)
    

    return frame