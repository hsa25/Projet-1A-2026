from datetime import date
from Sport import Sport


class Joueur:
    def __init__(self,
                 id: int,
                 nom: str,
                 sport: Sport,
                 date_naissance: date,
                 taille: float,
                 poids: float,
                 role: str,
                 pseudo: str,
                 genre: str,
                 statistiques: dict,
                 nationalite: str):
        self.__id = id
        self.__nom = nom
        self.__sport = sport
        self.__date_naissance = date_naissance
        self.__taille = taille
        self.__poids = poids
        self.__role = role
        self.__pseudo = pseudo
        self.__genre = genre
        self.__statistiques = statistiques
        self.__nationnalite = nationalite

    @property
    def nom(self):
        return self.__nom

    @property
    def sport(self):
        return self.__sport

    @property
    def date_naissance(self):
        return self.__date_naissance

    @property
    def taille(self):
        return self.__taille

    @property
    def poids(self):
        return self.__poids

    @property
    def role(self):
        return self.__role

    @property
    def pseudo(self):
        return self.__pseudo

    @property
    def genre(self):
        return self.__genre

    @property
    def statistiques(self):
        return self.__statistiques

    @property
    def nationalite(self):
        return self.__nationnalite

    def __str__(self):
        return f"{self.__nom}"

    def __repr__(self):
        return f"'Joueur({self.__id}, {self.__nom}, {self.__sport}, {self.__date_naissance}, {self.__taille}, {self.poids}, {self.__role}, {self.__pseudo}, {self.__genre}, {self.__statistiques}, {self.__nationalite})'"

    def __eq__(self, other):
        if not isinstance(other, Joueur):
            raise TypeError("L'objet n'est pas un joueur")
        else:
            return self.__id == other.__id
