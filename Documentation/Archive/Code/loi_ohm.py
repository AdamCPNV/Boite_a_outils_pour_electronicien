"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.5
Date : 30.05.2024
"""
import trouve_resistance_E12


PUISSANCE_DISIPER = [250,500,1000,2000,5000,10000]

def perte(perte):
    """calcule la puissance dissipée 

    Args:
        perte (int,float):

    Returns:
        nombre: (int)
    """
    perte = perte * 1000
    if perte > PUISSANCE_DISIPER[5]:
        return "Trop grand"
    for nombre in PUISSANCE_DISIPER:
        if nombre >= perte:
            return nombre

def resistance_inserer(tension_alimentation, tension_seul_led, courant_max):
    """calcule la resistance a inserer, le courant réel

    Args:
        tension_alimentation (int, float)
        tension_seul_led (int, float)
        courant_max (int, float)

    Returns:
        resistance (int, float)
        courant_reel (int, float)
        puissance_dissiper (int)
    """
    tension_reel = tension_alimentation - tension_seul_led
    resistance = tension_reel / courant_max

    if resistance > 10000000:
        return False

    resistance = trouve_resistance_E12.supperieur_proche_E12(resistance)
    courant_reel = tension_reel / resistance
    puissance_dissiper = (tension_alimentation - tension_seul_led) **2/resistance
    puissance_dissiper = perte(puissance_dissiper)
    return resistance ,courant_reel, puissance_dissiper
