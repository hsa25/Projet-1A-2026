from ..Model.Joueur import Joueur
from ..Model.Equipe import Equipe
from ..Model.Match import Match
from ..Model.Competition import Competition
from ..Model.Base import Base
from ..Model.Sport import Sport


def parse_starcraft2(player: list[list[str]],
                     match: list[list[str]],
                     nom_base: str) -> Base:

    liste_equipe = []
    liste_matchs = []

    for i in range(1, len(player)):
        liste_equipe.append(Equipe(nom=player[i][5],
                                   joueurs=[Joueur(nom=player[i][1],
                                                   pseudo=player[i][0],
                                                   nationalite=player[i][2],
                                                   date_naissance=player[i][3],
                                                   role=player[i][4],
                                                   )]))

    for j in range(1, len(match)):
        j1 = 0
        j2 = 0
        for k in range(len(liste_equipe)):
            if match[j][4] == liste_equipe[k].joueurs[0].pseudo:
                j1 = liste_equipe[k]
            if match[j][5] == liste_equipe[k].joueurs[0].pseudo:
                j2 = liste_equipe[k]
        liste_matchs.append(Match(equipe_1=j1,
                                  equipe_2=j2,
                                  date=match[j][0],
                                  round=match[j][1],
                                  groupe=match[j][2],
                                  best_of=match[j][3],
                                  score_1=[match[j][6]],
                                  score_2=[match[j][7]]))

    return (Base(nom=nom_base,
                 sport=Sport('Starcraft2', 1),
                 equipes=liste_equipe,
                 competitions=[Competition(nom=nom_base,
                                           matchs=liste_matchs)]))
