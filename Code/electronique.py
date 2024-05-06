SERIE = [1, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]

def inferieur_proche_E12(a_trouver):
    i = 1
    while True :
        i *= 10
        for nombre in SERIE:
            resulta = a_trouver / (nombre * i)
            print(str(a_trouver) + " diviser par " + str(nombre * i ) + " = " + str(resulta))
            # inferieur avec serie E 12 le plus proche du nombre entier
            if resulta <= 1:
                    return resulta

print(inferieur_proche_E12(500))

