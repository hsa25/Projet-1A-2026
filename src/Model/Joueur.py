from datetime import date


class Joueur:
    """
    Représente un joueur sportif avec ses informations personnelles et statistiques.

    Contient les données d'identité (nom, pseudonyme, nationalité), les
    caractéristiques physiques (taille, poids), ainsi que le rôle et les
    statistiques du joueur. Les attributs sont exposés en lecture seule
    via des propriétés.

    Attributs :
        __id (int | None) : L'identifiant unique du joueur.
        __nom (str) : Le nom complet du joueur.
        __date_naissance (date | str | None) : La date de naissance du joueur.
        __taille (float | None) : La taille du joueur en mètres.
        __poids (float | None) : Le poids du joueur en kilogrammes.
        __role (str | None) : Le rôle ou poste du joueur (ex. : "attaquant").
        __pseudo (str | None) : Le pseudonyme du joueur.
        __genre (str | None) : Le genre du joueur.
        __statistiques (dict | None) : Les statistiques du joueur sous forme
            de dictionnaire.
        __nationalite (str | None) : La nationalité du joueur.
    """

    def __init__(self,
                 nom: str,
                 id: int = None,
                 date_naissance: date | str = None,
                 taille: float = None,
                 poids: float = None,
                 role: str = None,
                 pseudo: str = None,
                 genre: str = None,
                 statistiques: dict = None,
                 nationalite: str = None):
        """
        Initialise une instance de Joueur.

        Args:
            nom (str): Le nom complet du joueur (ex. : "Kylian Mbappé").
            id (int, optional): L'identifiant unique du joueur. Par défaut None.
            date_naissance (date | str, optional): La date de naissance du joueur,
                sous forme d'objet date ou de chaîne de caractères. Par défaut None.
            taille (float, optional): La taille du joueur en mètres (ex. : 1.78).
                Par défaut None.
            poids (float, optional): Le poids du joueur en kilogrammes (ex. : 73.0).
                Par défaut None.
            role (str, optional): Le rôle ou poste du joueur (ex. : "attaquant",
                "gardien"). Par défaut None.
            pseudo (str, optional): Le pseudonyme du joueur. Par défaut None.
            genre (str, optional): Le genre du joueur (ex. : "masculin", "féminin").
                Par défaut None.
            statistiques (dict, optional): Les statistiques du joueur sous forme
                de dictionnaire (ex. : {"buts": 10, "passes": 5}). Par défaut None.
            nationalite (str, optional): La nationalité du joueur (ex. : "française").
                Par défaut None.
        """
        self.__id = id
        self.__nom = nom
        self.__date_naissance = date_naissance
        self.__taille = taille
        self.__poids = poids
        self.__role = role
        self.__pseudo = pseudo
        self.__genre = genre
        self.__statistiques = statistiques
        self.__nationalite = nationalite

    @property
    def nom(self) -> str:
        """str : Le nom complet du joueur."""
        return self.__nom

    @property
    def sport(self):
        """Le sport pratiqué par le joueur."""
        return self.__sport

    @property
    def date_naissance(self) -> date | str | None:
        """date | str | None : La date de naissance du joueur."""
        return self.__date_naissance

    @property
    def taille(self) -> float | None:
        """float | None : La taille du joueur en mètres."""
        return self.__taille

    @property
    def poids(self) -> float | None:
        """float | None : Le poids du joueur en kilogrammes."""
        return self.__poids

    @property
    def role(self) -> str | None:
        """str | None : Le rôle ou poste du joueur."""
        return self.__role

    @property
    def pseudo(self) -> str | None:
        """str | None : Le pseudonyme du joueur."""
        return self.__pseudo

    @property
    def genre(self) -> str | None:
        """str | None : Le genre du joueur."""
        return self.__genre

    @property
    def statistiques(self) -> dict | None:
        """dict | None : Les statistiques du joueur."""
        return self.__statistiques

    @property
    def nationalite(self) -> str | None:
        """str | None : La nationalité du joueur."""
        return self.__nationalite

    def __str__(self) -> str:
        """
        Retourne une représentation lisible du joueur.

        Returns:
            str: Le nom complet du joueur.
        """
        return f"{self.__nom}"

    def __repr__(self) -> str:
        """
        Retourne une représentation technique du joueur.

        Returns:
            str: Une chaîne contenant tous les attributs du joueur,
                utile pour le débogage.
        """
        return (f"'Joueur({self.__id}, {self.__nom}, {self.__sport}, "
                f"{self.__date_naissance}, {self.__taille}, {self.poids}, "
                f"{self.__role}, {self.__pseudo}, {self.__genre}, "
                f"{self.__statistiques}, {self.__nationalite})'")

    def __eq__(self, other) -> bool:
        """
        Vérifie l'égalité entre deux joueurs sur la base de leur identifiant.

        Args:
            other: L'objet à comparer avec le joueur courant.

        Raises:
            TypeError: Si l'objet passé en paramètre n'est pas une instance
                de Joueur.

        Returns:
            bool: True si les deux joueurs ont le même identifiant, False sinon.
        """
        if not isinstance(other, Joueur):
            raise TypeError("L'objet n'est pas un joueur")
        else:
            return self.__id == other.__id