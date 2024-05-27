"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.1
Date : 23.05.2024
"""
import tkinter
from integration import IntergationDB

def ajout_fournisseur(nom_fournisseur, addresse_fournisseur, numero_telephone, text_validation):
    bdd = IntergationDB()
    try:
        bdd.insertion(nom_fournisseur, addresse_fournisseur, numero_telephone)
        text_validation.config(text = "Le fournisseur {} à bien été ajouter".format(nom_fournisseur))
    except:
        text_validation.config(text = "Entrez un numero de téléphone uniquement composer de chiffre sans espace")

    



#affiche l'interface graphique
def modifier_materiel(maitre):
    frame = tkinter.Frame(maitre)

    text_valeur = tkinter.Label(frame, text = "Entrer la valeur(Ohm, Farad) du composant")
    entrer_valeur = tkinter.Entry(frame)

    text_taille = tkinter.Label(frame, text = "Entrez la taille(puissance max dissipée ou tension max) du composant :")
    entrer_taille = tkinter.Entry(frame)

    text_prix = tkinter.Label(frame, text = "Entrer le prix :")
    entrer_prix = tkinter.Entry(frame)

    text_num_fabrican = tkinter.Label(frame, text = "Entre")
    entrer_num_fabrican = tkinter.Entry(frame)

    text_num_article = tkinter.Label(frame, text= "Entrez le numero de article")
    entrer_num_article = tkinter.Entry(frame)

    bouton_ajoute = tkinter.Button(text= "Ajouté")

    message_info = tkinter.Label(frame, text = "")

    text_valeur.grid(row=0, column=0)
    entrer_valeur.grid(row=0, column= 1)

    text_taille.grid(row=1, column=0)
    entrer_taille.grid(row=1, column=1)

    text_prix.grid(row=2, column=0)
    entrer_prix.grid(row=2,column= 1)

    text_num_fabrican.grid(row=3, column=0)
    entrer_num_fabrican.grid(row=3, column=1)

    text_num_article.grid(row=4, column= 0)
    entrer_num_article.grid(row=4, column= 1)
    
    bouton_ajoute.grid(row=2, column=0)

    message_info.grid(row=3, column= 0)
    return frame