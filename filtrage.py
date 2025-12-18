def est_heureux(nombre):
    """
    Détermine si un nombre est 'heureux'.
    Un nombre est heureux si la somme des carrés de ses chiffres converge vers 1.
    Si on entre dans une boucle infinie sans atteindre 1, le nombre n'est pas heureux.
    """
    deja_vus = set()  # Pour détecter les boucles

    while nombre != 1 and nombre not in deja_vus:
        deja_vus.add(nombre)
        # Calculer la somme des carrés des chiffres
        nombre = sum(int(chiffre)**2 for chiffre in str(nombre))

    return nombre == 1

def filtrer_nombres_heureux(jusqua_n):
    """
    Génère une liste de nombres heureux de 1 jusqu'à n inclus.
    """
    liste_heureux = []
    for i in range(1, jusqua_n + 1):
        if est_heureux(i):
            liste_heureux.append(i)
    return liste_heureux

# Exemple d'utilisation
n = 100
nombres_heureux = filtrer_nombres_heureux(n)
print(f"Nombres heureux jusqu'à {n} :")
print(nombres_heureux)
