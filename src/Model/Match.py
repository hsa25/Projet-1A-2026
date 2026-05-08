from datetime import date
from .Equipe import Equipe


class Match:

    def __init__(self,
                 equipe_1: Equipe,
                 equipe_2: Equipe,
                 score_1: list[int],
                 score_2: list[int],
                 id: int = None,
                 round: int | str = None,
                 groupe: str = None,
                 ordre: str = None,
                 date: date = None,
                 best_of: int = None,
                 duree: float = None,
                 contexte: str = None,
                 stats: dict[float] = None) -> None:
        self.__equipe_1 = equipe_1
        self.__equipe_2 = equipe_2
        self.__score_1 = score_1
        self.__score_2 = score_2
        self.__id = id
        self.__round = round
        self.__groupe = groupe
        self.__ordre = ordre
        self.__date = date
        self.__best_of = best_of
        self.__duree = duree
        self.__contexte = contexte
        self.__stats = stats

    def afficher_match(self) -> str:
        return (f"{self.__round}"
                f"{self.__equipe_1.nom}-{self.__equipe_2.nom}"
                f"{self.__equipe_1.nom} : {self.__score_1}"
                f"{self.__equipe_2.nom} : {self.__score_2}")
