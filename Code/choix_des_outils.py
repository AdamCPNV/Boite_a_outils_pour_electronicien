import tkinter

fenetre = tkinter.Tk()
fenetre.geometry("900x900")


text_tension_alimentation = tkinter.Label(fenetre, text = "Veuilliez entrez la tension d'allimentaion : ")
entrer_tension_alimentation = tkinter.Entry(fenetre)

text_courent_max = tkinter.Label(fenetre, text= "Veuillez entrer le courant maximum :")
entrer_courent_max = tkinter.Entry(fenetre)

text_tension_seuil_led = tkinter.Label(fenetre, text= "Veuillez entrer la tension de seuil de la LED :")
entrer_tension_seuil_led = tkinter.Entry(fenetre)

text_resistance = tkinter.Label(fenetre, text= "Valeur de la résistance a installé :")

text_courrant_avec_resistance = tkinter.Label(fenetre, text= "Courant avec la résistance: ")

bouton_calculer = tkinter.Button(fenetre,text="Calculer")

bouton_recherche = tkinter.Button(fenetre, text="Recherche produit")


text_tension_alimentation.grid(row=0,column=0, sticky="n")
entrer_tension_alimentation.grid(row=0, column=1, sticky="n")

text_courent_max.grid(row=1,column=0, sticky="n")
entrer_courent_max.grid(row=1, column=1, sticky="n")

text_tension_seuil_led.grid(row=2,column=0, sticky="n")
entrer_tension_seuil_led.grid(row = 2, column = 1, sticky="n")

bouton_calculer.grid(row=4, column=2, sticky="n")

text_resistance.grid(row=5,column=0, sticky="n")

text_courrant_avec_resistance.grid(row=6,column=0, sticky="n")

bouton_recherche.grid(row=7, column=2, sticky="n")

fenetre.mainloop()