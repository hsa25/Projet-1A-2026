from .Match import Match


class Competition:
    """
    Représente une compétition sportive regroupant plusieurs matchs.

    Une compétition peut être de différents types (tournoi, championnat, coupe, etc.)
    et se déroule dans une ville et un pays donnés. Elle gère la liste des matchs
    qui la composent ainsi que le nombre de participants.

    Attributs :
        __nom (str) : Le nom de la compétition.
        __matchs (list[Match]) : La liste des matchs de la compétition.
        __ville (str | None) : La ville où se déroule la compétition.
        __pays (str | None) : Le pays où se déroule la compétition.
        __type (str | None) : Le type de la compétition (ex. : "tournoi", "championnat").
        __id (str | None) : L'identifiant unique de la compétition.
        __nombre_participants (int | None) : Le nombre de participants à la compétition.
    """

    def __init__(self,
                 nom: str,
                 matchs: list[Match],
                 ville: str = None,
                 pays: str = None,
                 type: str = None,
                 id: str = None,
                 nombre_participants: int = None) -> None:
        """
        Initialise une instance de Competition.

        Args:
            nom (str): Le nom de la compétition (ex. : "Roland-Garros").
            matchs (list[Match]): La liste initiale des matchs de la compétition.
            ville (str, optional): La ville où se déroule la compétition.
                Par défaut None.
            pays (str, optional): Le pays où se déroule la compétition.
                Par défaut None.
            type (str, optional): Le type de la compétition
                (ex. : "tournoi", "championnat", "coupe"). Par défaut None.
            id (str, optional): L'identifiant unique de la compétition.
                Par défaut None.
            nombre_participants (int, optional): Le nombre de participants
                à la compétition. Par défaut None.

        Returns:
            None
        """
        self.__nom = nom
        self.__matchs = matchs
        self.__ville = ville
        self.__pays = pays
        self.__type = type
        self.__id = id
        self.__nombre_participants = nombre_participants

    def ajouter_match(self, other: Match) -> None:
        """
        Ajoute un match à la liste des matchs de la compétition.

        Args:
            other (Match): Le match à ajouter à la compétition.

        Returns:
            None
        """
        self.__matchs.append(other)

    @property
    def nom(self):
        return self.__nom

    @property
    def matchs(self):
        return self.__matchs
