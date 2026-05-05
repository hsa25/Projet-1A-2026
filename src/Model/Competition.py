from .Match import Match

class Competition:

    def __init__(self,
                 nom: str,
                 matchs: list[Match],
                 ville: str = None,
                 pays: str = None,
                 type: str = None,
                 id: str  = None,
                 nombre_participants: int = None)-> None:
        self.__nom = nom
        self.__matchs = matchs
        self.__ville = ville
        self.__pays = pays
        self.__type = type
        self.__id = id
        self.__nombre_participants = nombre_participants