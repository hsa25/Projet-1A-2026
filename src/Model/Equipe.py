from .Sport import Sport
from .Joueur import Joueur  # Modifier quand la classe sera vraiment implémentée
from datetime import date


class Equipe():

    def __init__(self,
                 sport: Sport,
                 id: int,
                 nom: str,
                 abrev: str,
                 surnom: str,
                 region_small: str,
                 region_big: str,
                 date_creation: date,
                 joueurs: list[Joueur]) -> None:
        if len(joueurs) != sport.taille_equipe:
            raise ValueError("Le nombre de joueurs dans l'équipe n'est pas le bon")
        else:
            self.__sport = sport
            self.__id = id
            self.__nom = nom
            self.__abrev = abrev
            self.__surnom = surnom
            self.__region_small = region_small
            self.__region_big = region_big
            self.__date_creation = date_creation
            self.__joueurs = joueurs

    @property
    def nom(self):
        return self.__nom

    @property
    def abrev(self):
        return self.__abrev

    @property
    def surnom(self):
        return self.__surnom

    @property
    def region_small(self):
        return self.__region_small

    @property
    def region_big(self):
        return self.__region_big

    @property
    def date_creation(self):
        return self.__date_creation

    @property
    def joueurs(self):
        return self.__joueurs

    def __str__(self) -> str:
        return f"{self.__nom}"

    def __repr__(self) -> str:
        return f"Equipe({self.__sport}, {self.__id}, {self.__nom}, {self.__abrev}, {self.__surnom}, {self.__region_small}, {self.__region_big}, {self.__date_creation}, {self.__joueurs})"
