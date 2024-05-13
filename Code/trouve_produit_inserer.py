import trouve_resistance_E12

def resistance_inserer(temps_recharge, capcaciter_condensateur):
    resistance = temps_recharge / capcaciter_condensateur
    resistance = trouve_resistance_E12.valeur_proche(trouve_resistance_E12.inferieur_proche_E12(resistance), trouve_resistance_E12.supperieur_proche_E12(resistance))
    temps_recharge_reel = resistance * capcaciter_condensateur
    return resistance, temps_recharge_reel

def condensateur_inserer(temps_recharge, resistance):
    capcaciter_condensateur = resistance/ temps_recharge
    #ajouter serie E6
    temps_recharge_reel = resistance * capcaciter_condensateur
    return capcaciter_condensateur, temps_recharge_reel