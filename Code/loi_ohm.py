import trouve_resistance_E12

def resistance_inserer(tension_alimentation, tension_seul_led, courant_max):
    tension_reel = tension_alimentation - tension_seul_led
    resistance = tension_reel / courant_max

    resistance = trouve_resistance_E12.supperieur_proche_E12(resistance)[1]
    courant_reel = tension_reel / resistance
    puissance_dissiper = tension_alimentation **2 /resistance
    return resistance ,courant_reel, puissance_dissiper

test = resistance_inserer(10, 2, 0.025)
print("resistance = " + str(test[0]) + " courranr réel = " + str(test[1]) + " perte = " + str(test[2]))