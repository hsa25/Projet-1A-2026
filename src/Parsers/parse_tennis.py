from ..Model.Joueur import Joueur
from ..Model.Equipe import Equipe
from ..Model.Match import Match
from ..Model.Competition import Competition
from ..Model.Base import Base
from ..Model.Sport import Sport


def parse_tennis(player: list[list[str]],
                 match: list[list[str]],
                 nom_base: str) -> Base:

    liste_equipe = []
    dico_competitions = {}
    liste_competitions = []

    # Création des équipes (de 1 joueur)
    for j in range(1, len(player)):
        liste_equipe.append(Equipe(nom=player[j][2],
                                   id=int(player[j][0]),
                                   joueurs=[Joueur(nom=player[j][1] + ' ' + player[j][2],
                                                   role=player[j][3],
                                                   date_naissance=player[j][4][0:4]
                                                   + '-' + player[j][4][4:6]
                                                   + '-' + player[j][4][6:8],
                                                   nationalite=player[j][5],
                                                   taille=float(player[j][6]))]))

    # Création des compétitions
    for m in range(1, len(match)):
        # Association des équipes
        # (ce code est tellement répété, une fonction aurait probablement été plus utile)
        j1 = 0
        j2 = 0
        for e in liste_equipe:
            if e.id == int(match[m][7]):
                j1 = e
            if e.id == int(match[m][8]):
                j2 = e
        # Modification du format du score
        # (ce format enlève la partie entre parenthèses mais je n'ai aucune idée de son utilité de toute façon)
        s1 = []
        s2 = []
        for s in len(match[m][9].split(' ')):
            s1.append(int(match[m][9].split(' ')[s].split('-')[0][0]))
            s2.append(int(match[m][9].split(' ')[s].split('-')[1][0]))

        # Vérification de si la compétition existe dans les données chargées
        if match[m][0] not in dico_competitions:
            dico_competitions[match[m][0]] = Competition(nom=match[m][1],
                                                         id=match[m][0],
                                                         type=match[m][4],
                                                         nombre_participants=match[m][3],
                                                         matchs=[Match(round=match[m][11],
                                                                       equipe_1=j1,
                                                                       equipe_2=j2,
                                                                       score_1=s1,
                                                                       score_2=s2,
                                                                       date=match[m][5],
                                                                       best_of=int(match[m][10]),
                                                                       duree=float(match[m][12]),
                                                                       contexte=match[m][2],
                                                                       id=int(match[m][6]),
                                                                       stats={'ace': [match[m][13], match[m][22]],
                                                                              'df': [match[m][14], match[m][23]],
                                                                              'svpt': [match[m][15], match[m][24]],
                                                                              '1stIn': [match[m][16], match[m][25]],
                                                                              '1stWon': [match[m][17], match[m][26]],
                                                                              '2ndWon': [match[m][18], match[m][27]],
                                                                              'SvGms': [match[m][19], match[m][28]],
                                                                              'bpSaved': [match[m][20], match[m][29]],
                                                                              'bpFaced': [match[m][21], match[m][30]]
                                                                              })])
        # Si elle existe déjà on ajoute juste le match
        else:
            dico_competitions[match[m][0]].ajouter_match(Match(round=match[m][11],
                                                               equipe_1=j1,
                                                               equipe_2=j2,
                                                               score_1=s1,
                                                               score_2=s2,
                                                               date=match[m][5],
                                                               best_of=int(match[m][10]),
                                                               duree=float(match[m][12]),
                                                               contexte=match[m][2],
                                                               id=int(match[m][6]),
                                                               stats={'ace': [match[m][13], match[m][22]],
                                                                      'df': [match[m][14], match[m][23]],
                                                                      'svpt': [match[m][15], match[m][24]],
                                                                      '1stIn': [match[m][16], match[m][25]],
                                                                      '1stWon': [match[m][17], match[m][26]],
                                                                      '2ndWon': [match[m][18], match[m][27]],
                                                                      'SvGms': [match[m][19], match[m][28]],
                                                                      'bpSaved': [match[m][20], match[m][29]],
                                                                      'bpFaced': [match[m][21], match[m][30]]
                                                                      }))
    for comp in dico_competitions:
        liste_competitions.append(dico_competitions[comp])

    return (Base(nom=nom_base,
                 sport=Sport('Tennis', 1),
                 competitions=liste_competitions,
                 equipes=liste_equipe))
