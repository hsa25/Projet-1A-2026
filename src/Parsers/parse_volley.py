from ..Model.Joueur import Joueur
from ..Model.Equipe import Equipe
from ..Model.Match import Match
from ..Model.Competition import Competition
from ..Model.Base import Base
from ..Model.Sport import Sport
from ..Model.Coach import Coach


def parse_volley(player: list[list[str]],
                 coach: list[list[str]],
                 match: list[list[str]],
                 country: list[list[str]],
                 nom_base: str) -> Base:

    liste_equipes = []
    liste_matchs = []

    # Création des différentes équipes nationnales
    for p in range(1, len(country)):
        liste_equipes.append(Equipe(nom=country[p][2],
                                    abrev=country[p][0],
                                    surnom=country[p][1],
                                    joueurs=[],
                                    coachs=[]))

    # Ajout des coachs pour chaque équipe
    for c in range(1, len(coach)):
        for e in liste_equipes:
            if e.abrev == coach[c][4]:
                e.ajouter_coach(Coach(nom=coach[c][0],
                                      date_naissance=coach[c][1],
                                      genre=coach[c][2],
                                      role=coach[c][3]))

    # Ajout des joueurs pour chaque équipe
    for j in range(1, len(player)):
        for e in liste_equipes:
            if e.abrev == player[j][1]:
                e.ajouter_joueur(Joueur(nom=player[j][0],
                                        taille=float(player[j][2]),
                                        date_naissance=player[j][3],
                                        nationalite=player[j][4],
                                        pseudo=player[j][5]))

    # Création des matchs

    for m in range(1, match):
        # Recherche des équipes en fonction de leur nom
        j1 = 0
        j2 = 0
        while j1 == 0 and j2 == 0:
            for e in liste_equipes:
                if match[m][2] == e.abrev:
                    j1 = e
                if match[m][3] == e.abrev:
                    j2 = e
        liste_matchs.append(Match(round=match[m][1],
                                  date=match[m][0],
                                  score_1=match[m][4],
                                  score_2=match[m][5],
                                  equipe_1=j1,
                                  equipe_2=j2))

    return (Base(nom=nom_base,
                 sport=Sport('Volleyball', 13),
                 competitions=[Competition(nom='sans_nom',
                                           matchs=liste_matchs)],
                 equipes=liste_equipes))
