"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.2
Date : 30.05.2024
"""
import tkinter
from integration import IntergationDB
from changement_frame import change_frame
import choix_outils

def retour(maitre):
    """Retourne au menu précédent

    Args:
        maitre (widget):
    """
    change_frame(maitre, choix_outils.choix_des_outils(maitre))

def modification_composant(type, valeur, taille, prix, numero_article, nouveaux_numero_article, numero_telephone, text_validation):
    """modifie dans la BD un composant

    Args:
        type (int)
        valeur (int, float)
        taille (int, float)
        prix (int, float)
        numero_article (string)
        nouveaux_numero_article (string)
        numero_telephone (int)
        text_validation (widget)
    """
    bdd = IntergationDB()

    if type == "":
        type = "type"
    else:
        type = "'" + type + "'"

    if valeur == "":
        valeur = "value"
    else:
        valeur = "'" + valeur + "'"
    
    if taille == "":
        taille = "Size"
    else:
        taille = "'" + taille + "'"

    if prix == "":
        prix = "price"
    else:
        prix = "'" + prix + "'"   

    if numero_article == "":
        numero_article = "manufacturer-reference"
    else:
        numero_article = "'" + numero_article + "'"   

    if nouveaux_numero_article == "":
        nouveaux_numero_article = numero_article
    else:
        nouveaux_numero_article = "'" + nouveaux_numero_article + "'"  

    try:
        bdd.modification_produit(type, valeur, taille, prix, numero_article, nouveaux_numero_article)
        text_validation.config(text = "Les modifications ont été effectuer correctementn")
    except:
        text_validation.config(text = "Entrez un numero de téléphone uniquement composer de chiffre sans espace")
 
def modifier_materiel(maitre):
    """affiche l'interface pour modifier un composant

    Args:
        maitre (widget)

    Returns:
        frame (widget)
    """
    frame = tkinter.Frame(maitre)

    text_type = tkinter.Label(frame, text="Entrez le type")
    entrer_type = tkinter.Entry(frame)

    text_valeur = tkinter.Label(frame, text = "Entrer la nouvelle valeur(Ohm, Farad) du composant")
    entrer_valeur = tkinter.Entry(frame)

    text_taille = tkinter.Label(frame, text = "Entrez la nouvelle taille(puissance max dissipée ou tension max) du composant :")
    entrer_taille = tkinter.Entry(frame)

    text_prix = tkinter.Label(frame, text = "Entrer le nouveaux prix :")
    entrer_prix = tkinter.Entry(frame)

    text_num_article = tkinter.Label(frame, text= "Entrez le  numero de article")
    entrer_num_article = tkinter.Entry(frame)

    text_entrer_nouveaux_num_article = tkinter.Label(frame, text="Entrer le nouveaux numero de article")
    entrer_nouveaux_num_article = tkinter.Entry(frame)

    text_numero_fournisseur = tkinter.Label(frame, text="Entrer le numero de télàphone du fournisseur :")
    entrer_num_telphone = tkinter.Entry(frame)

    bouton_ajoute = tkinter.Button(frame,text= "Modifier", command=lambda:(modification_composant(
        entrer_type.get(),
        entrer_valeur.get(),
        entrer_taille.get(),
        entrer_prix.get(),
        entrer_num_article.get(),
        entrer_nouveaux_num_article.get(),
        entrer_num_telphone.get(),
        message_info
    )))
    bouton_retour = tkinter.Button(frame, text="Retour", command= lambda:(retour(frame)))



    message_info = tkinter.Label(frame, text = "")

    text_type.grid(row=0, column=0)
    entrer_type.grid(row=0, column=1)

    text_entrer_nouveaux_num_article.grid(row=1, column =0)
    entrer_nouveaux_num_article.grid(row=1, column=1)

    text_valeur.grid(row=2, column=0)
    entrer_valeur.grid(row=2, column= 1)

    text_taille.grid(row=3, column=0)
    entrer_taille.grid(row=3, column=1)

    text_prix.grid(row=4, column=0)
    entrer_prix.grid(row=4,column= 1)


    text_num_article.grid(row=5, column= 0)
    entrer_num_article.grid(row=5, column= 1)
    
    bouton_ajoute.grid(row=6, column=0)

    message_info.grid(row=7, column= 0)

    text_numero_fournisseur.grid(row=8, column=0)
    entrer_num_telphone.grid(row=8, column=1)

    bouton_retour.grid(row = 9, column=0)
    return frame