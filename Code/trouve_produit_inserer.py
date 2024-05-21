"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.3
Date : 21.05.2024
"""

import trouve_resistance_E12

#calcule le temps de recharge réel du condensateur en fonction de la résistance choisi
def resistance_inserer(temps_recharge, capcaciter_condensateur):
    resistance = temps_recharge / capcaciter_condensateur
    resistance = trouve_resistance_E12.valeur_proche(resistance,trouve_resistance_E12.inferieur_proche_E12(resistance), trouve_resistance_E12.supperieur_proche_E12(resistance))
    temps_recharge_reel = resistance * capcaciter_condensateur
    return resistance, temps_recharge_reel

#calcule le temps de recharge réel du condensateur en fonction de condensateur choisi
def condensateur_inserer(temps_recharge, resistance):
    capcaciter_condensateur =  temps_recharge/resistance
    condensateur = trouve_resistance_E12.valeur_proche(capcaciter_condensateur,trouve_resistance_E12.inferieur_proche_E12(capcaciter_condensateur, True), trouve_resistance_E12.supperieur_proche_E12(capcaciter_condensateur, True))
    temps_recharge_reel = resistance * condensateur
    return condensateur, temps_recharge_reel


print(condensateur_inserer(0.0005,0.00000033)[0])