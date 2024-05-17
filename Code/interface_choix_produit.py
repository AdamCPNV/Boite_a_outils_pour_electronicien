import tkinter
import integration


def rechercher_produit(type, valeur, taille, info_produit):
    bdd = integration.IntergationDB()
    resultat = bdd.rechercher_produit(type, valeur, taille)
    info_produit.config(text = resultat)

# affiche l'interface graphique
def affichage_produit(maitre, type, valeur, taille):
    frame = tkinter.Frame(maitre)
    info_produit = tkinter.Label(frame)
    info_produit.grid()
   
    rechercher_produit(type,valeur,taille, info_produit)
    return frame