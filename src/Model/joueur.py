class Joueur:
    def __init__(self, pseudo : str):
        self.pseudo = pseudo
        self.sport = sport
        self.prenom = prenom
        self.nom = nom
        self.statistiques = statistiques

    def __repr__(self) -> str :
        return f"Joueur(pseudo='{self.pseudo}')"
    
    def __str__(self) -> str :
        return f"{self.nom} {self.prenom}"
    
    def __eq__(self,other) -> bool :
        if not isinstance(other,Joueur):
            return False
        return self.pseudo == other.pseudo
    
    def __hash__(self):
        return self.__hash__
