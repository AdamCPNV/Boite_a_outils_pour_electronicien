def change_frame(fenetre, nouvelle_frame):
    for frame in fenetre.winfo_children():
        frame.grid_forget()
    nouvelle_frame.grid()