"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.2
Date : 28.05.2024
"""
import tkinter
from integration import IntergationDB

from changement_frame import change_frame
import choix_outils

def retour(maitre):
    change_frame(maitre, choix_outils.choix_des_outils(maitre))

def ajout_composant(type, valeur, taille, prix, numer_article, telephone, reference_fabriquant, text_validation):
    bdd = IntergationDB()
    try:
        bdd.insertion_produit(type, valeur, taille, prix, reference_fabriquant, telephone, numer_article)
        text_validation.config(text = "Le compostant {} à bien été ajouter".format(numer_article))
    except:
        text_validation.config(text = "tout les champs a par le numero de numero de article doive etre composer uniquement de chiffre ")

    



#affiche l'interface graphique
def ajouter_materiel(maitre):
    frame = tkinter.Frame(maitre)

    text_type = tkinter.Label(frame, text="Entrez le type du composant")
    entrer_type = tkinter.Entry(frame)

    text_valeur = tkinter.Label(frame, text = "Entrer la valeur(Ohm, Farad) du composant")
    entrer_valeur = tkinter.Entry(frame)

    text_taille = tkinter.Label(frame, text = "Entrez la taille(puissance max dissipée ou tension max) du composant :")
    entrer_taille = tkinter.Entry(frame)

    text_prix = tkinter.Label(frame, text = "Entrer le prix :")
    entrer_prix = tkinter.Entry(frame)

    text_num_fabrican = tkinter.Label(frame, text = "Entre numero fabriquant")
    entrer_num_fabrican = tkinter.Entry(frame)

    text_num_article = tkinter.Label(frame, text= "Entrez le numero de article")
    entrer_num_article = tkinter.Entry(frame)
    
    text_num_tel = tkinter.Label(frame, text="Entrez le numero de télphone du fournisseur")
    entrer_num_tel = tkinter.Entry(frame)

    text_ref_fabriquant = tkinter.Label(frame, text="Entrer reference fabriquant")
    entrer_ref_fabriquant = tkinter.Entry(frame)

    # ajouter les bouton manquant 
    # tester que sa fonctionne en ajoutant composant fournisseur est en recherchat le produit

    text_validation = tkinter.Label(frame, text="")
    bouton_ajoute = tkinter.Button(frame,text= "Ajouté", command=lambda:(ajout_composant(entrer_type.get,
                                                                                         entrer_taille.get(),
                                                                                         entrer_taille.get(),
                                                                                         entrer_prix.get(),
                                                                                         entrer_num_article.get(),
                                                                                         entrer_num_tel.get(),
                                                                                         entrer_ref_fabriquant.get(),
                                                                                         text_validation)))

    message_info = tkinter.Label(frame, text = "")

    bouton_retour = tkinter.Button(frame,text="Retoure", command=lambda:(retour(frame)))

    text_type.grid(row=0,column=0)
    entrer_type.grid(row=0, column=1)

    text_valeur.grid(row=1, column=0)
    entrer_valeur.grid(row=1, column= 1)

    text_taille.grid(row=2, column=0)
    entrer_taille.grid(row=2, column=1)

    text_prix.grid(row=3, column=0)
    entrer_prix.grid(row=3,column= 1)

    text_num_fabrican.grid(row=4, column=0)
    entrer_num_fabrican.grid(row=4, column=1)

    text_num_article.grid(row=5, column= 0)
    entrer_num_article.grid(row=5, column= 1)

    text_num_tel.grid(row=6, column=0)
    entrer_num_tel.grid(row=6, column=1)

    text_ref_fabriquant.grid(row=7, column=0)
    entrer_ref_fabriquant.grid(row=7, column=1)

    bouton_ajoute.grid(row=8, column=1)

    message_info.grid(row=9, column= 0)

    bouton_retour.grid(row=10, column=0)

    text_validation.grid()
    return frame