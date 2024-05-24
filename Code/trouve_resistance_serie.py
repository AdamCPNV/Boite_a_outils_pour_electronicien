"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.2
Date : 24.05.2024
"""
SERIE = [1, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]

# retourne la paire de résistance la plus proche
def trouve_paire_resistance(cible):

    if cible > 10000000:
        return False
    #calcule option 1
    multiplicateur = 1

    while multiplicateur < cible / 10:
        multiplicateur = multiplicateur * 10
    liste_resultat = []

    for resistance_E12 in SERIE:
        if resistance_E12 * multiplicateur == cible:
            return resistance_E12 * multiplicateur

    cible = cible / multiplicateur

    for resistance_E12 in SERIE:
        for resistance_E12_2 in SERIE:
            # classe dans l'ordre croissant la liste de toute les soustraction effectuer
            liste_resultat.append((abs(cible - (resistance_E12 + resistance_E12_2)), (resistance_E12, resistance_E12_2)))

    liste_resultat = sorted(liste_resultat)

    resistance_1 = liste_resultat[0][1][0]
    resistance_2 = liste_resultat[0][1][1]

    resistance_1 = resistance_1 * multiplicateur
    resistance_2 = resistance_2 * multiplicateur

    #caclcule option2 
    # calcule la plus grande résistance a inserer 
    cible = cible * multiplicateur
    ancienne_resistance = SERIE[0] * multiplicateur
    for resistance_E12 in SERIE:
        
        resistance_E12 = resistance_E12 * multiplicateur
        if resistance_E12 >= cible :
            grande_resistance = ancienne_resistance
        ancienne_resistance = resistance_E12

    #si le print réussi la variable existe
    try: 
        print(grande_resistance)
    except:
        grande_resistance = resistance_E12

    #calcule la plus petite resistance a inserer
    for resistance_E12 in SERIE:
        
        resistance_E12 = resistance_E12 * multiplicateur / 10
        if resistance_E12 >= cible - grande_resistance:
            petite_resistance = ancienne_resistance
            exit
        ancienne_resistance = resistance_E12
    
        #si le print réussi la variable existe
    try: 
        print(petite_resistance)
    except:
        petite_resistance = resistance_E12
 
    if (resistance_1 + resistance_2) - cible <= (grande_resistance + petite_resistance) - cible :
        print("option1")
        return  resistance_1, resistance_2
    else :
        print("option2")
        return grande_resistance, petite_resistance

print(trouve_paire_resistance(560000000))