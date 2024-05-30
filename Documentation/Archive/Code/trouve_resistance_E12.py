"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.6
Date : 30.05.2024
"""

#SERIE_E12
SERIE_E12 = [1, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]
SERIE_E6 = [1, 1.5, 2.2, 3.3, 4.7, 6.8]

def supperieur_proche_E12(resistance, serie_E6 = False):
     """Permet de trouvé la résistance maximal à utiliser pour etre le plus proche de la cible


     Args:
         resistance (int, float)
         serie_E6 (bool, optionelle)

     Returns:
         resistance_E12 * i (int, float)
     """
     
     if serie_E6:
         serie = SERIE_E6
         i = 0.00000001
     else:
         serie = SERIE_E12
         i = 0.1
     while True :
        i *= 10
        for resistance_E12 in serie:
            resulta = resistance / (resistance_E12 * i)
            print(str(resistance) + " diviser par " + str(resistance_E12 * i ) + " = " + str(resulta))
            if resulta <= 1:
                    return resistance_E12 * i
            

def inferieur_proche_E12(resistance, serie_E6 = False):
     """Permet de trouvé la résistance minimal à utiliser pour etre le plus proche de la cible


     Args:
         resistance (int, float)
         serie_E6 (bool, opttionnelle):

     Returns:
         (resistance_E12 * i) /10000000 (int, float)
         ancien_resistance_E12) /10000000 (int, float)
     """

     resistance = resistance * 10000000
     if serie_E6:
         serie = SERIE_E6
     else:
         serie = SERIE_E12
     i = 1
     while True :
        i *= 10
        ancienne_difference = 1
        for resistance_E12 in serie:
            resulta = resistance / (resistance_E12 * i)
            print(str(resistance) + " diviser par " + str(resistance_E12 * i ) + " = " + str(resulta))
            # tanps que le resistance_E12 est compris entre 1 et 2 on le divise par plus grand
            #Ne fonctionne pas si la resitance est inferieur a 1 
            if resulta >= 1 and resulta <= 2:
                    difference = resulta - 1
                    if ancienne_difference > difference:
                         ancienne_difference = difference
                         ancien_resistance_E12 = resistance_E12 * i
                    else:
                        return (resistance_E12 * i) /10000000
            elif resulta < 1: 
                 return (ancien_resistance_E12) /10000000

def valeur_proche(cible,min,max):
     """Deduit quelle est la valeur la plus proche de la cible


     Args:
         cible (int, float)
         min (int, float)
         max (int, float)

     Returns:
         max (int, float)
         min (int, float)
     """
     difference_minimal = cible - min
     difference_maximal = cible - max

     if abs(difference_maximal) < abs(difference_minimal):
          print("Valeur max :" + str(difference_maximal))
          print("La résistance la plus proche est de : " + str(max))
          return max
     else:
          print("Valeur min :" + str(difference_minimal))
          print("La résistance la plus proche est de : " + str(min))
          return min



