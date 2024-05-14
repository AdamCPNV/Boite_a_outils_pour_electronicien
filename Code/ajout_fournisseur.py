import tkinter

def outils1(maitre):
    frame = tkinter.Frame(maitre)

    text_nom_fournisseur = tkinter.Label(frame, text = "Entrez le nom du nouveaux fournisseur :")
    entrer_nom_fournisseur = tkinter.Entry(frame)

    text_addresse_fournisseur = tkinter.Label(frame, text= "Entrez l'addresse du nouveaux fournisseur :")
    entrer_addresse_fournisseur = tkinter.Entry(frame)

    text_numero_telephone = tkinter.Label(frame, text= "Entrez le numéro de téléphone du nouveaux fournisseur :")
    entrer_numero_telephone = tkinter.Entry(frame)

    bouton_ajouter = tkinter.Button(frame, text= "Ajouté")


    text_nom_fournisseur.grid(row= 0, column= 0)
    entrer_nom_fournisseur.grid(row= 0, column= 1)

    text_addresse_fournisseur.grid(row= 1, column= 0)
    entrer_addresse_fournisseur.grid(row=1, column=1)

    text_numero_telephone.grid(row=2, column= 0)
    entrer_numero_telephone.grid(row=2, column= 1)

    bouton_ajouter.grid(row=3, column= 1)

    return frame