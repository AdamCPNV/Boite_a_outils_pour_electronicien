import tkinter
import trouve_produit_inserer


def recuperer_champs( entrer_temps_charge_condensateur,  entrer_capaciter_condensateur, taille_reistance, temps_charge_reel_reistance):
    temps_charge_condensateur = float(entrer_temps_charge_condensateur.get())
    capaciter_condensateur = float(entrer_capaciter_condensateur.get())
    resltat = trouve_produit_inserer.resistance_inserer(temps_charge_condensateur, capaciter_condensateur)
    taille_reistance.config(text = " la résitance sera de : " + str(resltat[0]))
    temps_charge_reel_reistance.config(text = " le temps de charge réel sera de  : " + str(resltat[1]))
    print(resltat)

def outils2(maitre):

    frame = tkinter.Frame(maitre)
    bouton_resistance = tkinter.Button(frame, text="Résistance")
    bouton_condensateur = tkinter.Button(frame, text="condensateur")

    text_temps_charge_condensateur = tkinter.Label(frame, text="Entrez le temps de charge du condensateur : ")
    entrer_temps_charge_condensateur = tkinter.Entry(frame)

    text_capaciter_condensateur = tkinter.Label(frame, text="Entrez la capacité du condensateur : ")
    entrer_capaciter_condensateur = tkinter.Entry(frame)

    bouton_calculer = tkinter.Button(frame, text="Calculer", command = lambda :(recuperer_champs(
        entrer_temps_charge_condensateur,
        entrer_capaciter_condensateur,
        text_taille_resitance,
        text_temps_charge_reel
        )))

    text_taille_resitance = tkinter.Label(frame, text="")
    text_temps_charge_reel = tkinter.Label(frame, text="")

    bouton_resistance.grid(row = 0, column  = 0)
    bouton_condensateur.grid(row = 0, column = 1)

    text_temps_charge_condensateur.grid(row = 1, column = 0)
    entrer_temps_charge_condensateur.grid(row = 1, column = 1)

    text_capaciter_condensateur.grid(row = 2, column = 0)
    entrer_capaciter_condensateur.grid(row = 2, column = 1)

    bouton_calculer.grid(row = 3, column = 0)

    text_taille_resitance.grid(row=4, column= 0)
    text_temps_charge_reel.grid(row= 5, column= 0)

    return frame