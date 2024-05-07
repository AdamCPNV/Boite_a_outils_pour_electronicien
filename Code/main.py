import tkinter
from choix_outils import choix_des_outils
 
fenetre = tkinter.Tk()
fenetre.geometry("900x900")
frame = choix_des_outils(fenetre)
frame.grid()
fenetre.mainloop()