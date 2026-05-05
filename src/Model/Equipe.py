from .Joueur import Joueur
from .Coach import Coach
from datetime import date


class Equipe():
    """
    Représente une équipe sportive composée de joueurs et d'entraîneurs.

    Contient les informations générales de l'équipe (nom, région, date de création)
    ainsi que la liste de ses membres. Les attributs principaux sont exposés
    en lecture seule via des propriétés.

    Attributs :
        __id (int | None) : L'identifiant unique de l'équipe.
        __nom (str) : Le nom officiel de l'équipe.
        __abrev (str | None) : L'abréviation du nom de l'équipe (ex. : "PSG").
        __surnom (str | None) : Le surnom de l'équipe (ex. : "Les Bleus").
        __region_small (str | None) : La région locale de l'équipe (ex. : ville).
        __region_big (str | None) : La région élargie de l'équipe (ex. : pays).
        __date_creation (date | None) : La date de création de l'équipe.
        __joueurs (list[Joueur]) : La liste des joueurs de l'équipe.
        __coachs (list[Coach] | None) : La liste des entraîneurs de l'équipe.
    """

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
        """
        Initialise une instance d'Equipe.

        Args:
            nom (str): Le nom officiel de l'équipe (ex. : "Paris Saint-Germain").
            joueurs (list[Joueur]): La liste initiale des joueurs de l'équipe.
            id (int, optional): L'identifiant unique de l'équipe. Par défaut None.
            abrev (str, optional): L'abréviation du nom de l'équipe (ex. : "PSG").
                Par défaut None.
            surnom (str, optional): Le surnom de l'équipe (ex. : "Les Parisiens").
                Par défaut None.
            region_small (str, optional): La région locale de l'équipe (ex. : ville
                ou département). Par défaut None.
            region_big (str, optional): La région élargie de l'équipe (ex. : pays
                ou continent). Par défaut None.
            date_creation (date, optional): La date de création de l'équipe.
                Par défaut None.
            coachs (list[Coach], optional): La liste des entraîneurs de l'équipe.
                Par défaut None.

        Returns:
            None
        """
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
    def nom(self) -> str:
        """str : Le nom officiel de l'équipe."""
        return self.__nom

    @property
    def abrev(self) -> str | None:
        """str | None : L'abréviation du nom de l'équipe."""
        return self.__abrev

    @property
    def surnom(self) -> str | None:
        """str | None : Le surnom de l'équipe."""
        return self.__surnom

    @property
    def region_small(self) -> str | None:
        """str | None : La région locale de l'équipe (ex. : ville)."""
        return self.__region_small

    @property
    def region_big(self) -> str | None:
        """str | None : La région élargie de l'équipe (ex. : pays)."""
        return self.__region_big

    @property
    def date_creation(self) -> date | None:
        """date | None : La date de création de l'équipe."""
        return self.__date_creation

    @property
    def joueurs(self) -> list[Joueur]:
        """list[Joueur] : La liste des joueurs de l'équipe."""
        return self.__joueurs

    @property
    def coachs(self) -> list[Coach] | None:
        """list[Coach] | None : La liste des entraîneurs de l'équipe."""
        return self.__coachs

    def __str__(self) -> str:
        """
        Retourne une représentation lisible de l'équipe.

        Returns:
            str: Le nom officiel de l'équipe.
        """
        return f"{self.__nom}"

    def __repr__(self) -> str:
        """
        Retourne une représentation technique de l'équipe.

        Returns:
            str: Une chaîne contenant tous les attributs de l'équipe,
                utile pour le débogage.
        """
        return (f"Equipe({self.__sport}, {self.__id}, {self.__nom}, "
                f"{self.__abrev}, {self.__surnom}, {self.__region_small}, "
                f"{self.__region_big}, {self.__date_creation}, {self.__joueurs})")
    