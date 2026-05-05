from .Sport import Sport
from .Joueur import Joueur
from .Coach import Coach
from datetime import date


class Equipe():

    def __init__(self,
                 nom: str,
                 joueurs: list[Joueur],
                 id: int = None,
                 abrev: str = None,
                 surnom: str = None,
                 region_small: str = None,
                 region_big: str = None,
                 date_creation: date = None,
                 coachs: list[Coach] = None) -> None:
            self.__id = id
            self.__nom = nom
            self.__abrev = abrev
            self.__surnom = surnom
            self.__region_small = region_small
            self.__region_big = region_big
            self.__date_creation = date_creation
            self.__joueurs = joueurs
            self.__coachs = coachs

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
    
    @property
    def coachs(self):
        return self.__coachs

    def __str__(self) -> str:
        return f"{self.__nom}"

    def __repr__(self) -> str:
        return f"Equipe({self.__sport}, {self.__id}, {self.__nom}, {self.__abrev}, {self.__surnom}, {self.__region_small}, {self.__region_big}, {self.__date_creation}, {self.__joueurs})"

    