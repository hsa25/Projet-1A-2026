from .Competition import Competition
from .Equipe import Equipe
from .Sport import Sport


class Base:
    """
    Regroupe toutes les entités principales (sport, compétitions, équipes)

    Attributs :
        __nom (str) : Le nom de cette instance de base.
        __sport (Sport) : Le sport associé à cette base.
        __competitions (list[Competition]) : L'ensemble des compétitions enregistrées.
        __equipes (list[Equipe]) : L'ensemble des équipes enregistrées.
    """

    def __init__(
        self,
        nom: str,
        sport: Sport,
        competitions: list[Competition],
        equipes: list[Equipe],
    ) -> None:
        """
        Initialise une instance de Base.

        Args:
            nom (str): Le nom de la base (ex. : "Base Ligue 1").
            sport (Sport): Le sport auquel cette base est associée.
            competitions (list[Competition]): La liste des compétitions
                enregistrées dans cette base.
            equipes (list[Equipe]): La liste des équipes enregistrées
                dans cette base.

        Returns:
            None
        """
        self.__nom = nom
        self.__sport = sport
        self.__competitions = competitions
        self.__equipes = equipes