"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.1
Date : 07.05.2024
"""
import trouve_resistance_E12

#perte en milliwatt
PERTE = [250,500,1000,2000,5000,10000]

#Calcule le taux de perte à appliquer à une résistance
def perte(perte):
    for nombre in PERTE:
        if nombre >= perte:
            return nombre

#Calcule la résistance à insérer ainsi que le courant réel est la puissance dissiper
def resistance_inserer(tension_alimentation, tension_seul_led, courant_max):
    tension_reel = tension_alimentation - tension_seul_led
    resistance = tension_reel / courant_max

    resistance = trouve_resistance_E12.supperieur_proche_E12(resistance)
    courant_reel = tension_reel / resistance
    puissance_dissiper = tension_alimentation **2 /resistance
    puissance_dissiper = perte(puissance_dissiper)
    return resistance ,courant_reel, puissance_dissiper

