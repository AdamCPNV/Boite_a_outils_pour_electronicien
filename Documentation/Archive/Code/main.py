"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.2
Date : 13.05.2024
"""

import tkinter
from choix_outils import choix_des_outils
fenetre = tkinter.Tk()
fenetre.title("Boîte à outils pour électronicien")
frame = choix_des_outils(fenetre)
frame.grid()
fenetre.mainloop()