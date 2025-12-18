def compresser_texte(texte):
    """
    Fonction qui compresse un texte en remplaçant les lettres répétées
    par la lettre suivie du nombre de répétitions consécutives.
    Exemple : 'aaabbcccc' devient 'a3b2c4'
    """
    if not texte:
        return ""  # Cas où le texte est vide

    resultat = ""         # Chaîne compressée à construire
    lettre_courante = texte[0]  # Première lettre à analyser
    compteur = 1          # Compteur de répétitions

    # Parcours du texte à partir du deuxième caractère
    for caractere in texte[1:]:
        if caractere == lettre_courante:
            compteur += 1  # Incrémenter si la lettre se répète
        else:
            # Ajouter la lettre et son compteur au résultat
            resultat += lettre_courante + str(compteur)
            lettre_courante = caractere  # Nouvelle lettre
            compteur = 1  # Réinitialiser le compteur

    # Ajouter la dernière séquence
    resultat += lettre_courante + str(compteur)

    return resultat

# Exemple d'utilisation
texte_original = "aaabbcccc"
texte_compresse = compresser_texte(texte_original)
print("Texte compressé :", texte_compresse)
