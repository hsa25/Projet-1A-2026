class Sport:

    def __init__(self, nom: str, nom_dossier: int) -> None:
        self.__nom = nom
        self.__nom_dossier = nom_dossier

    @property
    def nom_sport(self) -> str:
        return self.__nom

    @property
    def nom_dossier(self) -> int:
        return self.__nom_dossier
