def est_adresse_ip_valide(ip):
    """
    Vérifie si une adresse IP est valide.
    Une adresse IP est composée de 4 nombres séparés par des points.
    Chaque nombre doit être compris entre 0 et 255.
    """
    # Séparer l'adresse IP en parties à l'aide du point comme séparateur
    parties = ip.split('.')

    # Une adresse IP valide doit avoir exactement 4 parties
    if len(parties) != 4:
        return False

    for partie in parties:
        # Vérifier que chaque partie est un nombre entier
        if not partie.isdigit():
            return False

        # Convertir la partie en entier
        nombre = int(partie)

        # Vérifier que le nombre est dans l'intervalle valide
        if nombre < 0 or nombre > 255:
            return False

    # Si toutes les vérifications sont passées, l'adresse est valide
    return True

# Exemples de test
print(est_adresse_ip_valide("192.168.1.1"))     # Doit afficher True
print(est_adresse_ip_valide("256.300.1.1"))     # Doit afficher False
print(est_adresse_ip_valide("192.168.1"))       # Doit afficher False
print(est_adresse_ip_valide("abc.def.ghi.jkl")) # Doit afficher False
