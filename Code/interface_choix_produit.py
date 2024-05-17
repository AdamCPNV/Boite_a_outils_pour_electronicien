import tkinter
import integration


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

    tableaux = ["prix", "Numero fabriquant", "Type", "Valeur", "Taille", "Nom"]

    for categorie in range (len(tableaux)):
        entete = tkinter.Label(frame, text= tableaux[categorie])
        entete.grid(row = 0, column=categorie)

    for i in range(len(resultat)):
        for j in range(len(tableaux)):
            f = tkinter.Label(frame, text= resultat[i][j])
            f.grid(row=i + 1, column=j)

    return frame