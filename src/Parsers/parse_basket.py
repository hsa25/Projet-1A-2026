from ..Model.Joueur import Joueur
from ..Model.Equipe import Equipe
from ..Model.Match import Match
from ..Model.Competition import Competition
from ..Model.Base import Base
from ..Model.Sport import Sport


def parse_basket(player: list[list[str]],
                 game: list[list[str]],
                 team: list[list[str]],
                 nom_base: str) -> Base:

    liste_equipes = []
    dico_compet = {}
    liste_competitions = []

    # Création équipes
    for t in range(1, len(team)):
        liste_equipes.append(Equipe(id=int(team[t][0]),
                                    nom=team[t][1],
                                    abrev=team[t][2],
                                    surnom=team[t][3],
                                    region_big=team[t][5],
                                    region_small=team[t][4]))

    # Ajout joueurs
    for j in range(1, len(player)):
        for e in liste_equipes:
            if e.id == int(player[j][8]):
                e.ajouter_joueur(Joueur(id=int(player[j][0]),
                                        nom=player[j][1] + ' ' + player[j][2],
                                        date_naissance=player[j][3],
                                        taille=player[j][4],
                                        poids=player[j][5],
                                        role=player[j][7],
                                        pseudo=player[j][6]
                                        ))

    # Création matchs
    for m in range(1, len(game)):
        j1 = 0
        j2 = 0
        for e in liste_equipes:
            if e.id == int(game[m][2]):
                j1 = e
            if e.id == int(game[m][24]):
                j2 = e
        if game[m][0] not in dico_compet:
            dico_compet[game[m][0]] = Competition(nom=game[m][0],
                                                  type=game[m][1],
                                                  matchs=[Match(equipe_1=j1,
                                                                equipe_2=j2,
                                                                id=game[m][3],
                                                                date=game[m][4],
                                                                duree=game[m][5],
                                                                score_1=game[m][23],
                                                                score_2=game[m][42],
                                                                stats={'fgm': [game[m][6], game[m][25]],
                                                                       'fga': [game[m][7], game[m][26]],
                                                                       'fg_pct': [game[m][8], game[m][27]],
                                                                       'fg3m': [game[m][9], game[m][28]],
                                                                       'fg3a': [game[m][10], game[m][29]],
                                                                       'fg3_pct': [game[m][11], game[m][30]],
                                                                       'ftm': [game[m][12], game[m][31]],
                                                                       'fta': [game[m][13], game[m][32]],
                                                                       'ft_pct': [game[m][14], game[m][33]],
                                                                       'oreb': [game[m][15], game[m][34]],
                                                                       'dreb': [game[m][16], game[m][35]],
                                                                       'reb': [game[m][17], game[m][36]],
                                                                       'ast': [game[m][18], game[m][37]],
                                                                       'stl': [game[m][19], game[m][38]],
                                                                       'blk': [game[m][20], game[m][39]],
                                                                       'tov': [game[m][21], game[m][40]],
                                                                       'pf': [game[m][22], game[m][41]]})])
        else:
            dico_compet[game[m][0]].ajouter_match(Match(equipe_1=j1,
                                                        equipe_2=j2,
                                                        id=game[m][3],
                                                        date=game[m][4],
                                                        duree=game[m][5],
                                                        score_1=game[m][23],
                                                        score_2=game[m][42],
                                                        stats={'fgm': [game[m][6], game[m][25]],
                                                               'fga': [game[m][7], game[m][26]],
                                                               'fg_pct': [game[m][8], game[m][27]],
                                                               'fg3m': [game[m][9], game[m][28]],
                                                               'fg3a': [game[m][10], game[m][29]],
                                                               'fg3_pct': [game[m][11], game[m][30]],
                                                               'ftm': [game[m][12], game[m][31]],
                                                               'fta': [game[m][13], game[m][32]],
                                                               'ft_pct': [game[m][14], game[m][33]],
                                                               'oreb': [game[m][15], game[m][34]],
                                                               'dreb': [game[m][16], game[m][35]],
                                                               'reb': [game[m][17], game[m][36]],
                                                               'ast': [game[m][18], game[m][37]],
                                                               'stl': [game[m][19], game[m][38]],
                                                               'blk': [game[m][20], game[m][39]],
                                                               'tov': [game[m][21], game[m][40]],
                                                               'pf': [game[m][22], game[m][41]]}))

    for comp in dico_compet:
        liste_competitions.append(dico_compet[comp])

    return (Base(nom=nom_base,
                 sport=Sport('Basketball'),
                 competitions=liste_competitions,
                 equipes=liste_equipes))
