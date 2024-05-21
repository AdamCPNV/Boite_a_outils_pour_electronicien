"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.1
Date : 21.05.2024
"""
import tkinter
from changement_frame import change_frame
import interface_outils2.outils2 as outils2

def retour(maitre):
    change_frame(maitre, outils2.outils2(maitre))


# récupere les donnée entrer est affiche le résultat
def recuperer_champs(condensateur, resistance, resultat):
    temps_de_charge = condensateur * resistance
    resultat.config(text= "Le temps de charge du condensateur sera de : " + str(temps_de_charge))



def interface_tao_outils2(maitre):

    frame = tkinter.Frame(maitre)

    text_resistance = tkinter.Label(frame, text="Entrez la taile de la résistance : ")
    entrer_resistance = tkinter.Entry(frame)

    text_condensateur = tkinter.Label(frame, text= "Entrez la valeur du condensateur : ")
    entrer_condensateur = tkinter.Entry(frame)

    bouton_calculer = tkinter.Button(frame, text= "Calculer", command= lambda:(recuperer_champs(float(entrer_condensateur.get()), float(entrer_resistance.get()), text_resultat)))

    text_resultat = tkinter.Label(frame, text="")

    bouton_retour = tkinter.Button(frame, text="retour", command= lambda:(retour(frame)))

    text_resistance.grid(column= 0, row=0)
    entrer_resistance.grid(column= 1, row= 0)

    text_condensateur.grid(column=0, row=1)
    entrer_condensateur.grid(column=1, row=1)

    bouton_calculer.grid(column=1, row=2)

    text_resultat.grid(column=0, row=3)

    bouton_retour.grid(column=0, row=4)
    return frame