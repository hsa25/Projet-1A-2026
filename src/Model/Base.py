from .Competition import Competition
from .Match import Match
from .Equipe import Equipe
from .Joueur import Joueur
from .Coach import Coach
from .Sport import Sport

class Base:

    def __init__(self,
                 nom: str,
                 sport: Sport,
                 competitions: list[Competition],
                 equipes: list[Equipe]) -> None:
        self.__nom = nom
        self.__sport = sport
        self.__competitions = competitions
        self.__equipes = equipes
