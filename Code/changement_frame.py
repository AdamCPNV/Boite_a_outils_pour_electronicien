"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.2
Date : 30.05.2024
"""
def change_frame(fenetre, nouvelle_frame):
    """change de frame

    Args:
        fenetre (widget)
        nouvelle_frame (widget)
    """
    for frame in fenetre.winfo_children():
        frame.grid_forget()
    nouvelle_frame.grid()