import tkinter

def modifier_fournisseur(maitre):
    frame = tkinter.Frame(maitre)

    text_nom_fournisseur_a_modifer = tkinter.Label(frame, text= "Entret le nom du fournisseur a modifier : ")
    entrer_nom_fournisseur_a_modifier = tkinter.Label(frame)

    bouton_rechercher = tkinter.Button(frame)

    text_nom_fournisseur = tkinter.Label(frame, text= "Entrer le nouveaux nom du fournisseur : ")
    entrer_nom_fournisseur = tkinter.Entry(frame)

    text_nouvelle_addresse = tkinter.Label(frame, text="Entret la nouvelle addresse du fournisseur : ")
    entrer_nouvelle_addresse = tkinter.Entry(frame)

    text_nouveaux_numero_telephone = tkinter.Label(frame, text="Enrez le nouveaux numero de téléphone : ")
    entrer_nouveaux_numero_telephone = tkinter.Entry(frame)

    bouton_valider = tkinter.Entry(text = "Validé")

    text_nom_fournisseur_a_modifer.grid(row=0, column=0)
    entrer_nom_fournisseur_a_modifier.grid(row=0, column=1)

    bouton_rechercher.grid(row= 1, column= 1)

    text_nom_fournisseur.grid(row=2, column= 0)
    entrer_nom_fournisseur.grid(row=2, column=1)

    text_nouvelle_addresse.grid(row=3, column=0)
    entrer_nouvelle_addresse(row = 3, column = 1)

    text_nouveaux_numero_telephone.grid(row= 4, column=0)
    entrer_nouveaux_numero_telephone.grid(row=4, column= 1)

    bouton_valider.grid(row=5, column= 1)
    return frame