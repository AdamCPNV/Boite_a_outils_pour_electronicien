def trouver_plus_proche(nombre, liste):
    plus_proche = liste[0]
    difference_min = abs(nombre - plus_proche)
    
    for num in liste:
        difference = abs(nombre - num)
        if difference < difference_min:
            plus_proche = num
            difference_min = difference
    
    return plus_proche

liste_nombres = [1, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]
nombre_donne = float(input("Entrez un nombre : "))

plus_proche = trouver_plus_proche(nombre_donne, liste_nombres)
print("Le nombre le plus proche de", nombre_donne, "est", plus_proche)
