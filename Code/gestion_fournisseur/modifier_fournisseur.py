"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.2
Date : 23.05.2024
"""
import tkinter
import integration

def modification_fournisseur(numero_telephone, nom_fournisseur, nouvelle_addresse, nouveaux_numero_telephone, text_info):
    bdd = integration.IntergationDB()

    # mise en forme des données 
    if nom_fournisseur == "":
        nom_fournisseur = "Name"
    else:
        nom_fournisseur = "'" + nom_fournisseur + "'"

    if nouvelle_addresse == "":
        nouvelle_addresse = "Address"
    else:
        nouvelle_addresse = "'" + nouvelle_addresse + "'"

    if nouveaux_numero_telephone == "":
        nouveaux_numero_telephone = "PhoneNumber"
        
    try:
        bdd.modification(numero_telephone, nom_fournisseur, nouvelle_addresse, nouveaux_numero_telephone)
        text_info.config(text = "Information modifier")
    except:
        text_info.config(text = "Remplisser les champs numero de téléphone avec uniquement des chiffres et sans espace")


#affiche l'interface graphique
def modifier_fournisseur(maitre):
    frame = tkinter.Frame(maitre)
    text_info = tkinter.Label(frame, text= "Entrez le numero de téléphone actuelle puis entrez les information que vous voulez modifier \n Pour validé les modifcation appuier sur le bouton modifier")
    text_numero_telephone_fournisseur = tkinter.Label(frame, text= "Entret le numero_telephone du fournisseur a modifier : ")
    entrer_numero_telephone_fournisseur = tkinter.Entry(frame)

    bouton_rechercher = tkinter.Button(frame, text= "Modifier", command= lambda :modification_fournisseur(entrer_numero_telephone_fournisseur.get(), 
                                                                                                          entrer_nom_fournisseur.get(), 
                                                                                                          entrer_nouvelle_addresse.get(), 
                                                                                                          entrer_nouveaux_numero_telephone.get(), 
                                                                                                          text_info))

    text_nom_fournisseur = tkinter.Label(frame, text= "Entrer le nouveaux nom du fournisseur : ")
    entrer_nom_fournisseur = tkinter.Entry(frame)

    text_nouvelle_addresse = tkinter.Label(frame, text="Entret la nouvelle addresse du fournisseur : ")
    entrer_nouvelle_addresse = tkinter.Entry(frame)

    text_nouveaux_numero_telephone = tkinter.Label(frame, text="Enrez le nouveaux numero de téléphone : ")
    entrer_nouveaux_numero_telephone = tkinter.Entry(frame)

    text_info.grid(row=0, column=0)

    text_numero_telephone_fournisseur.grid(row=1, column=0)
    entrer_numero_telephone_fournisseur.grid(row=1, column=1)

    text_nom_fournisseur.grid(row=3, column= 0)
    entrer_nom_fournisseur.grid(row=3, column=1)

    text_nouvelle_addresse.grid(row=4, column=0)
    entrer_nouvelle_addresse.grid(row = 4, column = 1)

    text_nouveaux_numero_telephone.grid(row= 5, column=0)
    entrer_nouveaux_numero_telephone.grid(row=5, column= 1)

    bouton_rechercher.grid(row= 6, column= 1)


    return frame