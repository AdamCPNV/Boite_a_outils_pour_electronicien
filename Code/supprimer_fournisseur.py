"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.1
Date : 14.05.2024
"""
import tkinter

#affiche l'interface graphique
def supprimer_fournisseur(maitre):
    frame = tkinter.Frame(maitre)

    text_nom_fournisseur = tkinter.Label(frame, text = "Entrez le nom du fournisseur a supprimer :")
    entrer_nom_fournisseur = tkinter.Entry(frame)


    bouton_supprimer = tkinter.Button(frame, text= "Supprimer")


    text_nom_fournisseur.grid(row= 0, column= 0)
    entrer_nom_fournisseur.grid(row= 0, column= 1)


    bouton_supprimer.grid(row=2, column= 1)

    return frame