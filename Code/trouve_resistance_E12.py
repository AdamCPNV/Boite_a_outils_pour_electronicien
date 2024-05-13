"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.1
Date : 07.05.2024
"""



#Serie E12
SERIE = [1, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]




#permet de trouvé la résistance maximal à utiliser pour etre le plus proche de la cible
def supperieur_proche_E12(resistance):
    i = 1
    while True :
        i *= 10
        for resistance_E12 in SERIE:
            resulta = resistance / (resistance_E12 * i)
            print(str(resistance) + " diviser par " + str(resistance_E12 * i ) + " = " + str(resulta))
            if resulta <= 1:
                    return resistance_E12 * i
            

#permet de trouvé la résistance minimal à utiliser pour etre le plus proche de la cible
def inferieur_proche_E12(resistance):
    i = 1
    while True :
        i *= 10
        ancienne_difference = 1
        for nombre in SERIE:
            resulta = resistance / (nombre * i)
            print(str(resistance) + " diviser par " + str(nombre * i ) + " = " + str(resulta))
            # tanps que le nombre est compris entre 1 et 2 on le divise par plus grand
            if resulta >= 1 and resulta <= 2:
                    difference = resulta - 1
                    if ancienne_difference > difference:
                         ancienne_difference = difference
                         ancien_nombre = nombre * i
                         None
                    else:
                        return resulta, nombre * i
            elif resulta < 1: 
                 return ancienne_difference + 1, ancien_nombre

#Deduit quelle est la valeur la plus proche de la cible
def valeur_proche(min,max):
     difference_minimal = 1 - min[0]
     difference_maximal = max[0] - 1

     if difference_minimal < difference_maximal:
          print("Valeur max :" + str(difference_maximal))
          print("La résistance la plus proche est de : " + str(max[1]))
          return max
     else:
          print("Valeur min :" + str(difference_minimal))
          print("La résistance la plus proche est de : " + str(min[1]))
          return min
