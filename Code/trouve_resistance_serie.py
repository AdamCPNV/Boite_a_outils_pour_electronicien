"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.2
Date : 24.05.2024
"""
SERIE = [1, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]

# retourne la paire de résistance la plus proche
def trouve_paire_rEistance(cible):

    if cible > 10000000:
        return False
        
    somme_proche = None
    proche = None
    liste_multiplicateur = []
    multiplicateur = 0.1
    while multiplicateur < cible / 10:
        multiplicateur = multiplicateur * 10
        liste_multiplicateur.append(multiplicateur * 10)

        
    for resistance_E12 in SERIE:
        if resistance_E12 * multiplicateur == cible:
            return resistance_E12 * multiplicateur


    for i in range(len(SERIE)):
        for j in range(i, len(SERIE)):
            for m1 in liste_multiplicateur:
                for m2 in liste_multiplicateur:
                    num1= SERIE[i] * m1
                    num2 = SERIE[j] * m2
                    somme_actuelle = round(num1) + round(num2)
                    if somme_proche is None or abs((somme_actuelle - cible) / cible) < abs((somme_proche - cible) / cible):
                        somme_proche = somme_actuelle 
                        print("paire utiliser : " + str(num1), str(num2)) 
    return somme_proche

print(trouve_paire_rEistance(83))