import tkinter
import integration


def rechercher_produit(type, valeur, taille, info_produit):
    bdd = integration.IntergationDB()
    resultat = bdd.rechercher_produit(type, valeur, taille)
    return resultat

# affiche l'interface graphique
def affichage_produit(maitre, type, valeur, taille):
    frame = tkinter.Frame(maitre)
    info_produit = tkinter.Label(frame)
    info_produit.grid()
    yo = rechercher_produit(type,valeur,taille, info_produit)

    tableaux = ["prix", "Numero fabriquant", "Type", "Valeur", "Taille", "Nom"]

    for categorie in range (len(tableaux)):
        entete = tkinter.Label(frame, text= tableaux[categorie])
        entete.grid(row = 0, column=categorie)

    for i in range(len(yo)):
        for j in range(len(tableaux)):
            #e = tkinter.Label(frame, text = tableaux[j])
            f = tkinter.Label(frame, text= yo[i][j])
            f.grid(row=i + 1, column=j)

    return frame