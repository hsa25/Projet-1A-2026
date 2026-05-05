from datetime import date, time
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
                 duree: time = None,
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

"""    def ajouter_participant_1(self, Equipe_1):
        if not isinstance(Equipe_1, Equipe):
            raise TypeError("L'équipe 1 doit être une équipe")
        self.__Equipe_1 = Equipe_1

    def ajouter_participant_2(self, Equipe_2):
        if not isinstance(Equipe_2, Equipe):
            raise TypeError("L'équipe 2 doit être une équipe")
        self.__Equipe_2 = Equipe_2

    def ajouter_equipes(self, Equipe_1, Equipe_2):
        self.ajouter_participant_1(self, Equipe_1)
        self.ajouter_participant_2(self, Equipe_2)

    def ajouter_scores(self, score_1, score_2):
        if not isinstance(score_1, list[int]) or not isinstance(score_2, list[int]):
            raise TypeError("Les scores doivent être des listes d'entier")
        if len(score_1) != len(score_2):
            raise ValueError("Les scores doivent avoir la même taille")

    def ajouter_equipes_et_scores(self, Equipe_1, Equipe_2, score_1, score_2):
        self.ajouter_equipes(Equipe_1, Equipe_2)
        self.ajouter_scores(self, score_1, score_2)

    def match_nul(self, Equipe_1, Equipe_2, score_1, score_2):
        self.ajouter_equipes_et_scores(self, Equipe_1, Equipe_2, score_1, score_2)
        return self.__score_1 == self.__score_2

    def renvoyer_equipe_gagnante(self, Equipe_1, Equipe_2, score_1, score_2):
        resultat_1 = 0
        resultat_2 = 0
        self.ajouter_equipes_et_scores(self, Equipe_1, Equipe_2, score_1, score_2)
        for i in len(score_1):
            if score_1[i] > score_2[i]:
                resultat_1 += 1
            else:
                resultat_2 += 1
        if resultat_1 > resultat_2:
            return self.__Equipe_1
        elif resultat_2 > resultat_1:
            return self.__Equipe_2
        else:
            raise ValueError("Il n'y a pas de gagnant, le match se solde par un nul.")

    def renvoyer_equipe_perdante(self, Equipe_1, Equipe_2, score_1, score_2):
        resultat_1 = 0
        resultat_2 = 0
        self.ajouter_equipes_et_scores(self, Equipe_1, Equipe_2, score_1, score_2)
        for i in len(score_1):
            if score_1[i] > score_2[i]:
                resultat_1 += 1
            else:
                resultat_2 += 1
        if resultat_1 < resultat_2:
            return self.__Equipe_1
        elif resultat_2 < resultat_1:
            return self.__Equipe_2
        else:
            raise ValueError("Il n'y a pas de perdant, le match se solde par un nul.") """
