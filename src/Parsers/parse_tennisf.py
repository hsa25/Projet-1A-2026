from ..Model.Joueur import Joueur
from ..Model.Equipe import Equipe
from ..Model.Match import Match
from ..Model.Competition import Competition
from ..Model.Base import Base
from ..Model.Sport import Sport


def parse_tennisf(player: list[list[str]],
                  match: list[list[str]],
                  nom_base: str) -> Base:
    """
    Parse des données brutes de tennis et retourne un objet Base structuré.

    Cette fonction transforme deux tableaux 2D (joueurs et matchs) en un objet
    Base contenant plusieurs Competitions regroupées par tournoi, chacune avec
    ses équipes (un joueur par équipe), ses matchs et leurs statistiques de
    service détaillées.

    Args:
        player (list[list[str]]): Tableau 2D des joueurs.
            La ligne 0 est ignorée (en-tête).
            Format des lignes suivantes :
                [0] id             - Identifiant unique du joueur (int)
                [1] prenom         - Prénom du joueur
                [2] nom            - Nom de famille du joueur (utilisé aussi
                                     comme nom de l'Equipe)
                [3] role           - Classement ou rôle (ex: "ATP", "WTA")
                [4] date_naissance - Date de naissance au format "YYYYMMDD",
                                     reformatée en "YYYY-MM-DD"
                [5] nationalite    - Nationalité (code pays, ex: "FRA")
                [6] taille         - Taille en mètres (float)

        match (list[list[str]]): Tableau 2D des matchs.
            La ligne 0 est ignorée (en-tête).
            Format des lignes suivantes :
                [0]  id_competition      - Identifiant unique du tournoi
                                          (clé de regroupement)
                [1]  nom_competition     - Nom du tournoi (ex: "Roland Garros")
                [2]  contexte            - Surface ou contexte (ex: "Clay")
                [3]  nb_participants     - Nombre de participants au tournoi
                [4]  type               - Type de tournoi (ex: "Grand Slam")
                [5]  date               - Date du match
                [6]  id_match           - Identifiant unique du match (int)
                [7]  id_joueur_1        - ID du joueur 1 (clé de résolution, int)
                [8]  id_joueur_2        - ID du joueur 2 (clé de résolution, int)
                [9]  score             - Score au format "X-Y Xa-Ya ..."
                                         un set par token séparé par espace ;
                                         seul le premier caractère de chaque
                                         côté est conservé (tie-break ignoré)
                [10] best_of           - Format (ex: "3" pour BO3, int)
                [11] round             - Tour du tournoi (ex: "F", "SF", "QF")
                [12] duree             - Durée du match en heures (float)
                [13] ace_j1            - Aces du joueur 1
                [14] df_j1             - Double fautes joueur 1
                [15] svpt_j1           - Points de service joués joueur 1
                [16] 1stIn_j1          - Premières balles réussies joueur 1
                [17] 1stWon_j1         - Points gagnés sur 1ère balle joueur 1
                [18] 2ndWon_j1         - Points gagnés sur 2ème balle joueur 1
                [19] SvGms_j1          - Jeux de service joueur 1
                [20] bpSaved_j1        - Balles de break sauvées joueur 1
                [21] bpFaced_j1        - Balles de break affrontées joueur 1
                [22]-[30]              - Mêmes statistiques pour le joueur 2

        nom_base (str): Nom attribué à l'objet Base retourné.

    Returns:
        Base: Objet Base peuplé avec :
            - sport        : Sport('Tennis', 1)
            - equipes      : liste d'objets Equipe, une par joueur, chacune
                             contenant un unique Joueur (nom complet = prénom + nom)
            - competitions : liste d'objets Competition, une par tournoi
                             (regroupées par id_competition), chacune avec ses
                             Matchs et leurs statistiques de service sous forme
                             [stat_j1, stat_j2]

    Example:
        >>> players = [
        ...     ["id", "prenom", "nom", "role", "naissance", "nat", "taille"],
        ...     ["101", "Rafael",   "Nadal",    "ATP", "19860603", "ESP", "1.85"],
        ...     ["102", "Novak",    "Djokovic", "ATP", "19870522", "SRB", "1.88"],
        ... ]
        >>> matches = [
        ...     ["id_comp", "nom_comp", "surface", "nb", "type", "date",
        ...      "id_match", "id_j1", "id_j2", "score", "bo", "round", "duree",
        ...      "ace1","df1","svpt1","1stIn1","1stWon1","2ndWon1","SvGms1",
        ...      "bpS1","bpF1",
        ...      "ace2","df2","svpt2","1stIn2","1stWon2","2ndWon2","SvGms2",
        ...      "bpS2","bpF2"],
        ...     ["1", "Roland Garros", "Clay", "128", "Grand Slam", "2024-06-09",
        ...      "42", "101", "102", "6-3 6-4 6-2", "3", "F", "2.5",
        ...      "5","2","80","52","40","18","12","3","4",
        ...      "3","4","75","45","30","15","10","4","7"],
        ... ]
        >>> base = parse_tennis(players, matches, "RG2024")
        >>> base.nom
        'RG2024'
        >>> base.competitions[0].nom
        'Roland Garros'
        >>> base.equipes[0].joueurs[0].nom
        'Rafael Nadal'
    """
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
                                                   taille=(player[j][6]))]))

    # Création des compétitions
    for m in range(1, len(match)):
        # Association des équipes
        j1 = 0
        j2 = 0
        for e in liste_equipe:
            if e.id == int(match[m][7]):
                j1 = e
            if e.id == int(match[m][8]):
                j2 = e
        # Modification du format du score
        s1 = []
        s2 = []
        for s in range(len(match[m][9].split(' '))):
            s1.append((match[m][9].split(' ')[s].split('-')[0][0]))
            s2.append((match[m][9].split(' ')[s].split('-')[1][0]))

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
                 sport=Sport('Tennis féminin', 'tennisf'),
                 competitions=liste_competitions,
                 equipes=liste_equipe))