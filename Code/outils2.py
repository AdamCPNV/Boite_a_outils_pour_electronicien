import tkinter
import trouve_produit_inserer


def recuperer_champs( entrer_temps_charge_condensateur,  entrer_capaciter, taille_reistance, temps_charge_reel_reistance, taille_condensateur):
    temps_charge_condensateur = float(entrer_temps_charge_condensateur.get())
    capaciter = float(entrer_capaciter.get())
    resltat_reistance = trouve_produit_inserer.resistance_inserer(temps_charge_condensateur, capaciter)
    taille_reistance.config(text = " Si vous cherchez une reistance elle sera de : " + str(resltat_reistance[0]))
    resltat_condensateur = trouve_produit_inserer.condensateur_inserer(temps_charge_condensateur,capaciter)
    taille_condensateur.config(text = " Si vous chercher un condensateur il sera de : " + str(resltat_condensateur[0]))
    temps_charge_reel_reistance.config(text = " le temps de charge réel sera de  : " + str(resltat_reistance[1]) + " ou si vous utiliser un condo sera de : " + str(resltat_condensateur[1]))

    print(resltat_reistance)

#true pour les reistance false pour les condensateur
def choix_mode(text_capaciter, mode):
    if mode:
        text_capaciter.config(text="Entrez la capacité du condensateur : ")
        
    else:
        text_capaciter.config(text="Entrez la taille de la resistance  : ")

def outils2(maitre):

    frame = tkinter.Frame(maitre)
    bouton_resistance = tkinter.Button(frame, text="Résistance", command=lambda:choix_mode(text_capaciter, True))
    bouton_condensateur = tkinter.Button(frame, text="condensateur", command = lambda:choix_mode(text_capaciter, False))

    text_temps_charge_condensateur = tkinter.Label(frame, text="Entrez le temps de charge du condensateur : ")
    entrer_temps_charge_condensateur = tkinter.Entry(frame)

    text_capaciter = tkinter.Label(frame, text="Entrez la capacité du condensateur : ")
    entrer_capaciter = tkinter.Entry(frame)

    bouton_calculer = tkinter.Button(frame, text="Calculer", command = lambda :(recuperer_champs(
        entrer_temps_charge_condensateur,
        entrer_capaciter,
        text_taille_resitance,
        text_temps_charge_reel,
        text_taille_condensateur
        )))


    text_taille_resitance = tkinter.Label(frame, text="")
    text_taille_condensateur = tkinter.Label(frame, text="")
    text_temps_charge_reel = tkinter.Label(frame, text="")

    bouton_resistance.grid(row = 0, column  = 0)
    bouton_condensateur.grid(row = 0, column = 1)

    text_temps_charge_condensateur.grid(row = 1, column = 0)
    entrer_temps_charge_condensateur.grid(row = 1, column = 1)

    text_capaciter.grid(row = 2, column = 0)
    entrer_capaciter.grid(row = 2, column = 1)

    bouton_calculer.grid(row = 3, column = 0)

    text_taille_resitance.grid(row=4, column= 0)
    text_temps_charge_reel.grid(row= 5, column= 0)
    text_taille_condensateur.grid(row=6, column= 0)

    return frame