from ..Model.Joueur import Joueur
from ..Model.Equipe import Equipe
from ..Model.Match import Match
from ..Model.Competition import Competition
from ..Model.Base import Base
from ..Model.Sport import Sport

def parse_football_cl(player: list[list[str]],
                      match: list[list[str]],
                      team: list[list[str]],
                      nom_base: str) -> Base:

    liste_equipes = []
    liste_matchs = []

    # Création des équipes
    for t in range(1, len(team)):
        liste_equipes.append(Equipe(nom=team[t][0],
                                    abrev=team[t][1],
                                    date_creation=[t][2],
                                    region_big=match[t][3],
                                    region_small=match[t][5],
                                    id=team[t][4],
                                    joueurs=[]))

    # Ajout des joueurs
    for j in range(1, len(player)):
        for e in liste_equipes:
            if e.abrev == player[j][1]:
                e.ajouter_joueur(Joueur(nom=player[j][0],
                                        role=player[j][2],
                                        statistiques={'assists': player[j][3],
                                                      'corners': player[j][4],
                                                      'offsides': player[j][5],
                                                      'dribbles': player[j][6],
                                                      'total_attempts': player[j][7],
                                                      'on_target': player[j][8],
                                                      'off_target': player[j][9],
                                                      'blocked': player[j][10],
                                                      'balls_recovered': player[j][11],
                                                      'tackles_won': player[j][12],
                                                      'tackles_lost': player[j][13],
                                                      'clearance_attempted': player[j][14],
                                                      'fouls_committed': player[j][15],
                                                      'fouls_suffered': player[j][16],
                                                      'red': player[j][17],
                                                      'yellow': player[j][18],
                                                      'pass_attempted': player[j][19],
                                                      'pass_completed': player[j][20],
                                                      'cross_attempted': player[j][21],
                                                      'cross_completed': player[j][22],
                                                      'freekicks_taken': player[j][23],
                                                      'saved': player[j][25],
                                                      'conceded': player[j][26],
                                                      'saved_penalties': player[j][27],
                                                      'cleansheets': player[j][28],
                                                      'punches_made': player[j][29],
                                                      'goals': player[j][30],
                                                      'goals_right_foot': player[j][31],
                                                      'goals_left_foot': player[j][32],
                                                      'goals_headers': player[j][33],
                                                      'goals_others': player[j][34],
                                                      'goals_inside_area': player[j][35],
                                                      'gaols_outside_area': player[j][36],
                                                      'penalties': player[j][37],
                                                      'minutes_played': player[j][38],
                                                      'match_played': player[j][39],
                                                      'distance_covered': player[j][40]}))
    # Ce dictionnaire est absolument interminable

    # Création matchs
    for m in range(1, len(match)):
        j1 = 0
        j2 = 0
        for e in liste_equipes:
            if e.abrev == match[m][5]:
                j1 = e
            if e.abrev == match[m][6]:
                j2 = e
        liste_matchs.append(Match(date=match[m][0],
                                  round=match[m][2],
                                  ordre=match[m][3],
                                  groupe=match[m][4],
                                  equipe_1=j1,
                                  equipe_2=j2,
                                  score_1=match[m][7],
                                  score_2=match[m][8]))

    return (Base(nom=nom_base,
                 sport=Sport('Football Champions League'),
                 competitions=[Competition(nom=nom_base, matchs=liste_matchs)],
                 equipes=liste_equipes))
