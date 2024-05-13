"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.1
Date : 13.05.2024
"""
SERIE = [1, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]

# retourne la paire de résistance la plus proche
def trouve_paire_resistance(cible):

    multiplicateur = 1

    while multiplicateur < cible / 10:
        multiplicateur = multiplicateur * 10
    liste_resultat = []

    cible = cible / multiplicateur


    for resistance_E12 in SERIE:
        for resistance_E12_2 in SERIE:
            # classe dans l'ordre croissant la liste de toute les soustraction effectuer
            liste_resultat.append((abs(cible - (resistance_E12 + resistance_E12_2)), (resistance_E12, resistance_E12_2)))

    liste_resultat = sorted(liste_resultat)

    return liste_resultat[0][1]

print(trouve_paire_resistance(756))