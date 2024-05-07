import tkinter
from changement_frame import change_frame
import outils1


def changement_menu(maitre):
    change_frame(maitre, outils1.outils1(maitre) )

def choix_des_outils(maitre):
    frame = tkinter.Frame(maitre)
    outils1 = tkinter.Button(frame, text="Dimensionnement d'une résistance dans un montage éà LED", command=lambda : changement_menu(frame))
    outils2 = tkinter.Button(frame, text= "Dimmensionnement de Charge/décharge d'un condensateur")
    outils3 = tkinter.Button(frame, text= "Résistances en série à partir d'une valeur donnée")

    outils1.grid()
    outils2.grid()
    outils3.grid()
    return frame