import datetime as dt
from .Equipe import Equipe

class Competition:

    def __init__(self, nom: str,
            date_debut: dt.date, 
            date_fin: dt.date, 
            participants: dict[str: "Equipe"]| None = None, 
            sport: str,
            classement: dict["Equipe": int]| None = None):
            self.__nom= nom
            self.__date_debut= date_debut
            self.__date_fin= date_fin
            self.__participants= participants
            self.__sport= sport
            self.__classement= classement 
        
    def ajouter_participant(self, Equipe_1):
        if not isinstance(Equipe_1, Equipe):
            raise TypeError("L'équipe doit être une équipe")
        self.__participants[self.__str__.Equipe_1()]=Equipe_1

    def retirer_participant(self, Equipe_1):
        if not isinstance(Equipe_1, Equipe):
            raise TypeError("L'équipe doit être une équipe")
        del self.__participants[self.__str__.Equipe_1()]        

