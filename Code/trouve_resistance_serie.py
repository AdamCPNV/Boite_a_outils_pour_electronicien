"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.4
Date : 27.05.2024
"""
SERIE = [1, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]

# retourne la paire de résistance la plus proche
def trouve_paire_reistance(cible):

    if cible > 10000000:
        return False
    
    if cible <= 1:
        return 1, 0, 1,round((1 - cible) /cible,3)
        
    somme_proche = None
    marge_erreur_proche = None
    liste_multiplicateur = []
    multiplicateur = 0.1
    while multiplicateur < cible / 10:
        multiplicateur = multiplicateur * 10
        liste_multiplicateur.append(multiplicateur * 10)

        
    for resistance_E12 in SERIE:
        resistance =round(resistance_E12 * multiplicateur,1)
        if resistance == cible:
            return resistance, 0, resistance, 0 
        
    resistance = SERIE[0] * multiplicateur *10
    if resistance == cible:
        return resistance, 0, resistance, 0 

    for i in range(len(SERIE)):
        for j in range(i, len(SERIE)):
            for m1 in liste_multiplicateur:
                for m2 in liste_multiplicateur:
                    num1= SERIE[i] * m1
                    num2 = SERIE[j] * m2
                    somme_actuelle = round(num1) + round(num2)
                    if somme_proche is None or abs((somme_actuelle - cible) / cible) < marge_erreur_proche:
                        somme_proche = somme_actuelle
                        resistance1 = round(num1, 1)
                        resistance2 = round(num2, 1)
                        marge_erreur_proche = abs(somme_proche - cible) / cible
    return resistance1, resistance2, somme_proche, marge_erreur_proche