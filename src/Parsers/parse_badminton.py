import os
import csv
from ..Model.Joueur import Joueur
from ..Model.Equipe import Equipe
from ..Model.Match import Match
from ..Model.Competition import Competition
from ..Model.Base import Base
from ..Model.Sport import Sport


def parse_badmintion(path, nom_base: str) -> Base:

    player = list(csv.reader(open(os.path.join(path, "player.csv"))))
    match = list(csv.reader(open(os.path.join(path, "match.csv"))))

    liste_equipe = []
    liste_competition = []
    competitions = {}

    for i in range(1, len(player)):
        liste_equipe.append(Equipe(nom=player[i][0],
                                   region_small=player[i][1],
                                   region_big=player[i][2],
                                   joueurs=Joueur(nom=player[i][0])))

    j1 = 0
    j2 = 0

    for j in range(1, len(match)):
        while j1 == 0 and j2 == 0:
            for k in range(len(liste_equipe)):
                if match[j][6] == liste_equipe[k].nom:
                    j1 = liste_equipe[k]
                if match[j][7] == liste_equipe[k].nom:
                    j2 = liste_equipe[k]
        s1 = match[j][9].split('-')
        s2 = match[j][10].split('-')
        s3 = match[j][11].split('-')

        if match[j][0] not in competitions:
            competitions[match[j][0]] = [match[j][1],
                                         match[j][2],
                                         match[j][4],
                                         [Match(equipe_1=j1,
                                                equipe_2=j2,
                                                round=match[j][5],
                                                date=match[j][3],
                                                score_1=[int(s1[0]),
                                                         int(s2[0]),
                                                         int(s3[0])],
                                                score_2=[int(s1[1]),
                                                         int(s2[1]),
                                                         int(s3[1])])]]
        else:
            competitions[match[j][0]][3].append(Match(equipe_1=j1,
                                                      equipe_2=j2,
                                                      round=match[j][5],
                                                      date=match[j][3],
                                                      score_1=[int(s1[0]),
                                                               int(s2[0]),
                                                               int(s3[0])],
                                                      score_2=[int(s1[1]),
                                                               int(s2[1]),
                                                               int(s3[1])]))
    for comp in competitions:
        liste_competition.append(Competition(nom=comp,
                                             ville=competitions[comp][0],
                                             pays=competitions[comp][1],
                                             type=competitions[comp][2],
                                             matchs=competitions[comp][3]))

    return (Base(nom=nom_base,
                 sport=Sport('Badminton', 1),
                 competitions=liste_competition,
                 equipes=liste_equipe))
