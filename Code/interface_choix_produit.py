"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.3
Date : 24.05.2024
"""

import tkinter
import integration
from changement_frame import change_frame
import choix_outils

def retour(maitre):
    change_frame(maitre, choix_outils.choix_des_outils(maitre))

def rechercher_produit(type, valeur, taille):
    bdd = integration.IntergationDB()
    if taille != 0:
        resultat = bdd.rechercher_produit(type, valeur, taille)
    else :
        resultat = bdd.rechercher_resistance(valeur)
    return resultat

# affiche l'interface graphique
def affichage_produit(maitre, type, valeur, taille = 0):
    frame = tkinter.Frame(maitre)
    info_produit = tkinter.Label(frame)
    info_produit.grid()
    resultat = rechercher_produit(type,valeur,taille)

    if resultat == []:
        message_erreur = tkinter.Label(frame, text= "Produit pas présent dans la base de donnée")
        message_erreur.grid()
        return frame

    tableaux = ["prix", "Numero fabriquant", "Type", "Valeur", "Taille", "Nom"]

    for categorie in range (len(tableaux)):
        entete = tkinter.Label(frame, text= tableaux[categorie])
        entete.grid(row = 0, column=categorie)

    for i in range(len(resultat)):
        for j in range(len(tableaux)):
            f = tkinter.Label(frame, text= resultat[i][j])
            f.grid(row=i + 1, column=j)

    bouton_retour = tkinter.Button(frame, text= "Retour", command=lambda:(retour(maitre)))
    bouton_retour.grid()

    return frame

