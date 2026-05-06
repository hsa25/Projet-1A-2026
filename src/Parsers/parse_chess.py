import os
import csv
from ..Model.Joueur import Joueur
from ..Model.Equipe import Equipe
from ..Model.Match import Match
from ..Model.Competition import Competition
from ..Model.Base import Base
from ..Model.Sport import Sport


player = list(csv.reader(open(os.path.join(path, "player.csv"))))
match = list(csv.reader(open(os.path.join(path, "match.csv"))))


def parse_chess(player: list[list[str]],
                match: list[list[str]],
                nom_base: str) -> Base:

    # Modification du formatage pour ne pas avoir les "" et , dans le nom
    # (compatible même avec les typos qui les oublient en plus \^0^/)
    for i in range(len(player)):
        player[i][0].replace('"', '')
        player[i][0].replace(',', '')

    for j in range(len(match)):
        player[j][3].replace('"', '')
        player[j][3].replace(',', '')
        player[j][4].replace('"', '')
        player[j][4].replace(',', '')

    liste_equipe = []
    liste_matchs = []

    for i in range(1, len(player)):
        liste_equipe.append(Equipe(nom=player[i][0],
                                   region_big=player[i][4],
                                   joueurs=Joueur(nom=player[i][0],
                                                  id=int(player[i][1]),
                                                  date_naissance=player[i][2],
                                                  genre=player[i][3],
                                                  role=player[i][5],
                                                  statistiques={'elo_standard': player[i][6],
                                                                'elo_rapide': player[i][7],
                                                                'elo_blitz': player[i][8]}
                                                  )))

    for j in range(1, len(match)):
        j1 = 0
        j2 = 0
        while j1 == 0 and j2 == 0:
            for k in range(len(liste_equipe)):
                if match[j][3] == liste_equipe[k].nom:
                    j1 = liste_equipe[k]
                if match[j][4] == liste_equipe[k].nom:
                    j2 = liste_equipe[k]
        liste_matchs.append(Match(round=match[j][0],
                                  groupe=match[j][1],
                                  ordre=match[j][2],
                                  equipe_1=j1,
                                  equipe_2=j2,
                                  score_1=[int(match[j][5])],
                                  score_2=[int(match[j][6])],
                                  stats={'seed_joueur_1': float(match[j][7]),
                                         'seed_joueur_2': float(match[j][8])}))

    return Base(nom=nom_base,
                sport=Sport('Échecs', 1),
                equipes=liste_equipe,
                competitions=[Competition(nom='Sans nom',
                                          matchs=liste_matchs)])
