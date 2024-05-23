"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.5
Date : 23.05.2024
"""
import tkinter
import loi_ohm
from changement_frame import change_frame
import interface_choix_produit

#Recupere les valeurs insérer par l'utilisateur et affiche les résultat

def recuprer_champs(tension_alimentation, courrant_max, tension_seuil_led, text_resistance, text_courrant_avec_resistance, text_puissance_dissiper, bouton_rechercher, maitre):
    try:
        tension_alimentation = float(tension_alimentation)
        courrant_max = float(courrant_max)
        tension_seuil_led = float(tension_seuil_led)
    except:
        bouton_rechercher.config(command = "")
        text_resistance.config(text = """Veuillez entrez: \n 
                             Un nombre composer uniquement de chiffre allant de 0 à 9 \n 
                             Content  si néssaisaire 1 seul point par nombre décimale(pas de virgule) \n Pas de lettre""")
        text_courrant_avec_resistance.config(text = "")
        text_puissance_dissiper.config(text = "")       
    resultat = loi_ohm.resistance_inserer(tension_alimentation,tension_seuil_led,courrant_max)
    if resultat == False:
        text_resistance.config(text= "La valeur de la résistance a installer est trop grande (dépasse les 10 mega ohm)")
        return None

    resistance_a_installer =resultat[0]
    courrant_avec_resistance = resultat[1]
    puissance_dissiper = resultat[2]
    text_resistance.config(text= "Valeur de la résistance a installé :" + str(resistance_a_installer))
    text_courrant_avec_resistance.config(text= "Courant avec la résistance :" + str(courrant_avec_resistance))
    text_puissance_dissiper.config(text= "Puissance disspé :" + str(puissance_dissiper))
    bouton_rechercher.config(command= lambda :(change_frame(maitre, interface_choix_produit.affichage_produit(maitre,1,resistance_a_installer, puissance_dissiper))))

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
    bouton_recherche = tkinter.Button(frame, text="Recherche produit")

    bouton_calculer = tkinter.Button(frame,text="Calculer", command = lambda :(recuprer_champs(
        entrer_tension_alimentation.get(),
        entrer_courent_max.get(), 
        entrer_tension_seuil_led.get(),
        text_resistance,
        text_courrant_avec_resistance, 
        text_puissance_dissiper,
        bouton_recherche,
        maitre)))
    
    bouton_recherche = tkinter.Button(frame, text="Recherche produit")
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