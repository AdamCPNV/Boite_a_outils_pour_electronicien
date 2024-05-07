import tkinter
from changement_frame import change_frame
import outils1


def changement_menu(maitre, outils):

    match outils:
        case 1:
            change_frame(maitre, outils1.outils1(maitre))
        case 2:
            print("A implementer")
        case 3:
            print("A implementer")
        case 4:
            print("A implementer")
        case 5:
            print("A implementer")
        case 6:
            print("A implementer")

def choix_des_outils(maitre):
    frame = tkinter.Frame(maitre)
    titre = tkinter.Label(frame, text= "Veuilliez choisire ce que vous voulez faire")
    outils1 = tkinter.Button(frame, text="Dimensionnement d'une résistance dans un montage éà LED", command=lambda : changement_menu(frame, 1))
    outils2 = tkinter.Button(frame, text= "Dimmensionnement de Charge/décharge d'un condensateur", command=lambda : changement_menu(frame, 2))
    outils3 = tkinter.Button(frame, text= "Résistances en série à partir d'une valeur donnée", command=lambda : changement_menu(frame, 3))
    ajouter_fournisseur = tkinter.Button(frame, text="Ajouté un fournisseur", command=lambda : changement_menu(frame, 4))
    modifier_fournisseur = tkinter.Button(frame, text="Modifier les coordonné de un fournisseur", command=lambda : changement_menu(frame, 5))
    supprimer_fournisseur = tkinter.Button(frame, text="Supprimer un fournisseur", command=lambda : changement_menu(frame, 6))

    titre.grid(row = 0, column = 0)
    outils1.grid(row = 1,column = 0)
    outils2.grid(row = 2, column = 0)
    outils3.grid(row = 3, column = 0)
    ajouter_fournisseur.grid(row = 4, column = 0)
    modifier_fournisseur.grid(row = 4, column = 0)
    supprimer_fournisseur.grid(row = 5, column= 0)
    return frame