class Sport:

    def __init__(self, nom: str, taille_equipe: int) -> None:
        self.__nom = nom
        self.__taille_equipe = taille_equipe

    @property
    def nom_sport(self) -> str:
        return self.__nom

    @property
    def taille_equipe(self) -> int:
        return self.__taille_equipe
