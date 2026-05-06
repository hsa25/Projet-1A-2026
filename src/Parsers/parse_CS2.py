from ..Model.Joueur import Joueur
from ..Model.Equipe import Equipe
from ..Model.Match import Match
from ..Model.Competition import Competition
from ..Model.Base import Base
from ..Model.Sport import Sport
from ..Model.Coach import Coach


def parse_CS2(player: list[list[str]],
              coach: list[list[str]],
              match: list[list[str]],
              team: list[list[str]],
              nom_base: str) -> Base:

    liste_equipes = []
    liste_matchs = []

    # Création des équipes
    for t in range(1, len(team)):
        liste_equipes.append(Equipe(nom=team[t][0],
                                    abrev=team[t][1],
                                    region_big=team[t][3],
                                    region_small=team[t][2],
                                    joueurs=[],
                                    coachs=[]))

    # Ajout des coachs
    for c in range(1, len(coach)):
        for e in liste_equipes:
            if e.nom == coach[c][4]:
                e.ajouter_coach(Coach(pseudo=coach[c][0],
                                      nom=coach[c][1],
                                      nationalite=coach[c][2],
                                      date_naissance=coach[c][3]))

    # Ajout des joueurs
    for j in range(1, len(player)):
        for e in liste_equipes:
            if e.nom == player[j][5]:
                e.ajouter_joueur(Joueur(pseudo=player[c][0],
                                        nom=player[j][1],
                                        nationalite=player[j][2],
                                        date_naissance=player[j][3],
                                        role=player[j][4]))

    # Création des matchs
    for m in range(1, len(match)):
        # Sélection des équipes
        # (Décidément ce code revient vraiment partout de la même façon)
        j1 = 0
        j2 = 0
        for e in liste_equipes:
            if match[m][4] == e.nom:
                j1 = e
            if match[m][5] == e.nom:
                j2 = e
        liste_matchs.append(Match(equipe_1=j1,
                                  equipe_2=j2,
                                  date=match[m][0],
                                  groupe=match[m][1],
                                  round=match[m][2],
                                  best_of=match[m][3],
                                  score_1=match[m][6],
                                  score_2=match[m][7]))
    # Puisque 1 base de donnée = 1 compétition alors le nom est le même
    # (ça évite de perdre le nom à la sauvegarde ou de devoir recréer une variable)
    return (Base(nom=nom_base,
                 sport=Sport(nom='Counter Strike 2',
                             taille_equipe=5),
                 equipes=liste_equipes,
                 competitions=[Competition(nom=nom_base,
                                           matchs=liste_matchs)]))
