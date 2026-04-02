from .Sport import Sport
from .Joueur import Joueur  # Modifier quand la classe sera vraiment implémentée
from .Coach import Coach


class Equipe():

    def __init__(self, sport: Sport, nom_officiel: str, nom_abreviation: str, joueurs: list(Joueur), coachs: list(Coach), lieu: str, region: str) -> None:
        if len(joueurs) != sport.taille_equipe:
            raise ValueError("Le nombre de joueurs dans l'équipe n'est pas le bon")
        else:
            self.__sport = sport
            self.__nom_officiel = nom_officiel
            self.__nom_abreviation = nom_abreviation
            self.__joueurs = joueurs
            self.__coachs = coachs
            self.__lieu = lieu
            self.__region = region

    @property
    def nom_officiel(self):
        return self.__nom_officiel

    @property
    def nom_abreviation(self):
        return self.__nom_abreviation

    def __str__(self) -> str:
        return f"{self.__nom_officiel}"

    def __repr__(self) -> str:
        return f"Equipe({self.__sport}, {self.__nom_officiel}, {self.__nom_abreviation}, {self.__joueurs})"
