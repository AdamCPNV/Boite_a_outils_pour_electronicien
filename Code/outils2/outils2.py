import tkinter



def outils2(maitre):

    frame = tkinter.Frame(maitre)
    bouton_resistance = tkinter.Button(frame, text="Résistance")
    bouton_condensateur = tkinter.Button(frame, text="condensateur")

    text_temps_charge_condensateur = tkinter.Label(frame, text="Entrez le temps de charge du condensateur : ")
    entrer_temps_charge_condensateur = tkinter.Entry(frame)

    text_capaciter_condensateur = tkinter.Label(frame, text="Entrez la capacité du condensateur : ")
    entrer_capaciter_condensateur = tkinter.Entry(frame)

    bouton_calculer = tkinter.Button(frame, text="Calculer")

    bouton_resistance.grid(row = 0, column  = 0)
    bouton_condensateur.grid(row = 0, column = 1)

    text_temps_charge_condensateur.grid(row = 1, column = 0)
    entrer_temps_charge_condensateur.grid(row = 1, column = 1)

    text_capaciter_condensateur.grid(row = 2, column = 0)
    entrer_capaciter_condensateur.grid(row = 2, column = 1)

    bouton_calculer.grid(row = 3, column = 0)
    
    return frame