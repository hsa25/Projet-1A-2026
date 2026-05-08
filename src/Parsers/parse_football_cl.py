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
    """
    Parse des données brutes de Champions League et retourne un objet Base structuré.

    Cette fonction transforme trois tableaux 2D (joueurs, matchs, équipes) en un
    objet Base contenant une unique Competition regroupant l'ensemble des équipes,
    joueurs avec leurs statistiques détaillées, et matchs du tournoi.

    Args:
        player (list[list[str]]): Tableau 2D des joueurs.
            La ligne 0 est ignorée (en-tête).
            Format des lignes suivantes :
                [0]  nom                - Nom du joueur
                [1]  abrev_equipe       - Abréviation de l'équipe (clé de jointure)
                [2]  role               - Poste du joueur
                [3]  assists            - Passes décisives
                [4]  corners            - Corners tirés
                [5]  offsides           - Hors-jeux
                [6]  dribbles           - Dribbles réussis
                [7]  total_attempts     - Tentatives de tir totales
                [8]  on_target          - Tirs cadrés
                [9]  off_target         - Tirs non cadrés
                [10] blocked            - Tirs bloqués
                [11] balls_recovered    - Ballons récupérés
                [12] tackles_won        - Tacles réussis
                [13] tackles_lost       - Tacles ratés
                [14] clearance_attempted- Dégagements tentés
                [15] fouls_committed    - Fautes commises
                [16] fouls_suffered     - Fautes subies
                [17] red                - Cartons rouges
                [18] yellow             - Cartons jaunes
                [19] pass_attempted     - Passes tentées
                [20] pass_completed     - Passes réussies
                [21] cross_attempted    - Centres tentés
                [22] cross_completed    - Centres réussis
                [23] freekicks_taken    - Coups francs tirés
                [24] (non utilisé)
                [25] saved              - Arrêts (gardien)
                [26] conceded           - Buts encaissés (gardien)
                [27] saved_penalties    - Penalties arrêtés (gardien)
                [28] cleansheets        - Clean sheets (gardien)
                [29] punches_made       - Sorties au poing (gardien)
                [30] goals              - Buts marqués
                [31] goals_right_foot   - Buts du pied droit
                [32] goals_left_foot    - Buts du pied gauche
                [33] goals_headers      - Buts de la tête
                [34] goals_others       - Buts autres
                [35] goals_inside_area  - Buts dans la surface
                [36] gaols_outside_area - Buts hors surface (typo conservée)
                [37] penalties          - Penalties marqués
                [38] minutes_played     - Minutes jouées
                [39] match_played       - Matchs joués
                [40] distance_covered   - Distance parcourue

        match (list[list[str]]): Tableau 2D des matchs.
            La ligne 0 est ignorée (en-tête).
            Également utilisé par erreur pour lire region_big et region_small
            des équipes (voir Notes).
            Format des lignes suivantes :
                [0] date        - Date du match
                [1] (non utilisé)
                [2] round       - Tour du tournoi
                [3] ordre       - Ordre du match dans le tour
                [4] groupe      - Groupe ou poule
                [5] abrev_eq1   - Abréviation équipe 1 (clé de résolution)
                [6] abrev_eq2   - Abréviation équipe 2 (clé de résolution)
                [7] score_1     - Score final équipe 1
                [8] score_2     - Score final équipe 2

        team (list[list[str]]): Tableau 2D des équipes.
            La ligne 0 est ignorée (en-tête).
            Format des lignes suivantes :
                [0] nom           - Nom complet de l'équipe
                [1] abrev         - Abréviation (clé de jointure avec joueurs et matchs)
                [2] date_creation - Date de création du club
                [3] region_big    - Région complète (ex: "England")
                [4] id            - Identifiant unique de l'équipe
                [5] region_small  - Région courte (ex: "ENG")

        nom_base (str): Nom attribué à l'objet Base retourné. Utilisé également
            comme nom de l'unique Competition créée.

    Returns:
        Base: Objet Base peuplé avec :
            - sport        : Sport('Football Champions League')
            - equipes      : liste d'objets Equipe avec leurs Joueurs et leurs
                             statistiques individuelles détaillées
            - competitions : liste contenant une unique Competition dont le nom
                             est nom_base, regroupant tous les Matchs

    Example:
        >>> teams = [
        ...     ["nom", "abrev", "date_creation", "region_big", "id", "region_small"],
        ...     ["Real Madrid", "RMA", "1902-03-06", "Spain", "1", "ESP"],
        ...     ["Bayern Munich", "BAY", "1900-02-27", "Germany", "2", "GER"],
        ... ]
        >>> players = [
        ...     ["nom", "abrev", "role", "assists", "corners", "offsides",
        ...      "dribbles", "total_attempts", "on_target", "off_target",
        ...      "blocked", "balls_recovered", "tackles_won", "tackles_lost",
        ...      "clearance_attempted", "fouls_committed", "fouls_suffered",
        ...      "red", "yellow", "pass_attempted", "pass_completed",
        ...      "cross_attempted", "cross_completed", "freekicks_taken", "?",
        ...      "saved", "conceded", "saved_penalties", "cleansheets",
        ...      "punches_made", "goals", "goals_right_foot", "goals_left_foot",
        ...      "goals_headers", "goals_others", "goals_inside_area",
        ...      "gaols_outside_area", "penalties", "minutes_played",
        ...      "match_played", "distance_covered"],
        ...     ["Vinicius Jr", "RMA", "FW", "8", "0", "22", "120", "95", "42",
        ...      "38", "15", "60", "10", "5", "2", "18", "30", "0", "3",
        ...      "450", "380", "45", "20", "5", "0", "0", "0", "0", "0",
        ...      "0", "21", "14", "2", "4", "1", "18", "3", "3", "2980",
        ...      "38", "350.5"],
        ... ]
        >>> matches = [
        ...     ["date", "?", "round", "ordre", "groupe",
        ...      "eq1", "eq2", "score_1", "score_2"],
        ...     ["2024-04-09", "", "QF", "1", "A",
        ...      "RMA", "BAY", "2", "1"],
        ... ]
        >>> base = parse_football_cl(players, matches, teams, "UCL2024")
        >>> base.nom
        'UCL2024'
        >>> len(base.competitions)
        1
    """
    liste_equipes = []
    liste_matchs = []

    # Création des équipes
    for t in range(1, len(team)):
        liste_equipes.append(Equipe(nom=team[t][0],
                                    abrev=team[t][1],
                                    date_creation=team[t][2],
                                    region_big=team[t][3],
                                    region_small=team[t][5],
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
                 sport=Sport('Football Champions League', 'football_champions_league'),
                 competitions=[Competition(nom=nom_base, matchs=liste_matchs)],
                 equipes=liste_equipes))