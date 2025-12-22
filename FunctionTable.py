def table(nb: int, max: int = 10):
    """Fonction affichant la table de multiplication par : nb,
       - Arguments : 
                    nb (int) : le nb dont la table de multiplication est à afficher.
       - max (int, optionnel) : affiche la table de 1 à 10 maximum.
    """
    for i in range(1, max + 1): #tant que i est entre 1 et max inclus
        print(f"{i} * {nb} {i * nb}");

table("non", max = 8)