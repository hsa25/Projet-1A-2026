from ..Model.Joueur import Joueur
from ..Model.Equipe import Equipe
from ..Model.Match import Match
from ..Model.Competition import Competition
from ..Model.Base import Base
from ..Model.Sport import Sport
from ..Model.Coach import Coach


def parse_LoL(player: list[list[str]],
              coach: list[list[str]],
              match: list[list[str]],
              team: list[list[str]],
              nom_base: str) -> Base:

    liste_equipes = []
    liste_matchs = []

    # Création des équipes (encore)
    for t in range(1, len(team)):
        liste_equipes.append(Equipe(nom=team[t][0],
                                    abrev=team[t][1],
                                    region_big=team[t][3],
                                    region_small=team[t][2],
                                    joueurs=[],
                                    coachs=[]))

    # Ajout des coachs (ça devrait être familier à force)
    for c in len(1, len(coach)):
        for e in liste_equipes:
            if e.nom == coach[c][5]:
                e.ajouter_coach(Coach(pseudo=coach[c][0],
                                      nom=coach[c][1],
                                      nationalite=coach[c][2],
                                      date_naissance=coach[c][3],
                                      role=coach[c][4]))

    # Ajout des joueurs
    for j in len(1, len(player)):
        for e in liste_equipes:
            if e.nom == player[j][5]:
                e.ajouter_joueur(Joueur(pseudo=player[c][0],
                                        nom=player[c][1],
                                        nationalite=player[c][2],
                                        date_naissance=player[c][3],
                                        role=player[c][4]))

    # Création des matchs
    for m in range(1, len(match)):
        # Association équipe
        j1 = 0
        j2 = 0
        for e in liste_equipes:
            if e.abrev == match[m][5]:
                j1 = e
            if e.abrev == match[m][6]:
                j2 = e
        if j1.abrev == match[m][7]:
            s1 = 1
            s2 = 0
        else:
            s1 = 0
            s2 = 1
        liste_matchs.append(Match(equipe_1=j1,
                                  equipe_2=j2,
                                  contexte=match[m][0],
                                  date=match[m][1],
                                  ordre=match[m][2] + '/' + match[m][3] + '/' + match[m][4],
                                  score_1=s1,
                                  score_2=s2,
                                  duree=match[m][8],
                                  stats={'kills': [int(match[m][9]), int(match[m][16])],
                                         'assists': [int(match[m][10]), int(match[m][17])],
                                         'deaths': [int(match[m][11]), int(match[m][18])],
                                         'gold': [int(match[m][12]), int(match[m][19])],
                                         'turrets': [int(match[m][13]), int(match[m][20])],
                                         'dragons': [int(match[m][14]), int(match[m][21])],
                                         'barons': [int(match[m][15]), int(match[m][22])]}))

    return (Base(nom=nom_base,
                 sport=Sport(nom='League of Legends',
                             taille_equipe=5),
                 equipes=liste_equipes,
                 competitions=[Competition(nom=nom_base,
                                           matchs=liste_matchs)]))
