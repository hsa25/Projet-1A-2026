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
    """
    Parse des données brutes de League of Legends et retourne un objet Base structuré.

    Cette fonction transforme quatre tableaux 2D (joueurs, coachs, matchs, équipes)
    en un objet Base contenant une unique Competition regroupant l'ensemble des
    équipes, coachs, joueurs et matchs avec leurs statistiques de jeu.

    Args:
        player (list[list[str]]): Tableau 2D des joueurs.
            La ligne 0 est ignorée (en-tête).
            Format des lignes suivantes :
                [0] pseudo         - Pseudo en jeu du joueur
                [1] nom            - Nom réel du joueur
                [2] nationalite    - Nationalité du joueur
                [3] date_naissance - Date de naissance
                [4] role           - Rôle en jeu (ex: "Top", "Jungle", "Mid",
                                     "ADC", "Support")
                [5] nom_equipe     - Nom de l'équipe (clé de jointure)

        coach (list[list[str]]): Tableau 2D des coachs.
            La ligne 0 est ignorée (en-tête).
            Format des lignes suivantes :
                [0] pseudo         - Pseudo du coach
                [1] nom            - Nom réel du coach
                [2] nationalite    - Nationalité du coach
                [3] date_naissance - Date de naissance
                [4] role           - Rôle du coach (ex: "Head Coach", "Analyst")
                [5] nom_equipe     - Nom de l'équipe (clé de jointure)

        match (list[list[str]]): Tableau 2D des matchs.
            La ligne 0 est ignorée (en-tête).
            Format des lignes suivantes :
                [0]  contexte      - Contexte / compétition du match
                [1]  date          - Date du match
                [2]  ordre_1       - Première composante de l'ordre
                [3]  ordre_2       - Deuxième composante de l'ordre
                [4]  ordre_3       - Troisième composante de l'ordre
                                     (concaténées : "[2]/[3]/[4]")
                [5]  abrev_eq1     - Abréviation équipe 1 (clé de résolution)
                [6]  abrev_eq2     - Abréviation équipe 2 (clé de résolution)
                [7]  abrev_winner  - Abréviation de l'équipe gagnante
                                     (détermine score_1/score_2 : 1/0 ou 0/1)
                [8]  duree         - Durée du match
                [9]  kills_eq1     - Kills équipe 1
                [10] assists_eq1   - Assists équipe 1
                [11] deaths_eq1    - Deaths équipe 1
                [12] gold_eq1      - Or total équipe 1
                [13] turrets_eq1   - Tourelles détruites équipe 1
                [14] dragons_eq1   - Dragons tués équipe 1
                [15] barons_eq1    - Barons tués équipe 1
                [16] kills_eq2     - Kills équipe 2
                [17] assists_eq2   - Assists équipe 2
                [18] deaths_eq2    - Deaths équipe 2
                [19] gold_eq2      - Or total équipe 2
                [20] turrets_eq2   - Tourelles détruites équipe 2
                [21] dragons_eq2   - Dragons tués équipe 2
                [22] barons_eq2    - Barons tués équipe 2

        team (list[list[str]]): Tableau 2D des équipes.
            La ligne 0 est ignorée (en-tête).
            Format des lignes suivantes :
                [0] nom          - Nom complet de l'équipe
                [1] abrev        - Abréviation (clé de résolution dans les matchs)
                [2] region_small - Région courte (ex: "LEC")
                [3] region_big   - Région complète (ex: "Europe")

        nom_base (str): Nom attribué à l'objet Base retourné. Utilisé également
            comme nom de l'unique Competition créée.

    Returns:
        Base: Objet Base peuplé avec :
            - sport        : Sport(nom='League of Legends', taille_equipe=5)
            - equipes      : liste d'objets Equipe avec leurs Joueurs et Coachs
            - competitions : liste contenant une unique Competition dont le nom
                             est nom_base, regroupant tous les Matchs avec leurs
                             statistiques de jeu (kills, assists, deaths, gold,
                             turrets, dragons, barons) sous forme [eq1, eq2]

    Example:
        >>> teams = [
        ...     ["nom", "abrev", "region_small", "region_big"],
        ...     ["T1",            "T1",  "LCK", "Korea"],
        ...     ["Cloud9",        "C9",  "LCS", "North America"],
        ... ]
        >>> coaches = [
        ...     ["pseudo", "nom", "nationalite", "naissance", "role", "equipe"],
        ...     ["Kkoma", "Kim Jeong-gyun", "Korean", "1986-09-07",
        ...      "Head Coach", "T1"],
        ... ]
        >>> players = [
        ...     ["pseudo", "nom", "nationalite", "naissance", "role", "equipe"],
        ...     ["Faker", "Lee Sang-hyeok", "Korean", "1996-05-07", "Mid", "T1"],
        ... ]
        >>> matches = [
        ...     ["contexte", "date", "o1", "o2", "o3", "eq1", "eq2", "winner",
        ...      "duree", "k1","a1","d1","g1","t1","dr1","b1",
        ...               "k2","a2","d2","g2","t2","dr2","b2"],
        ...     ["Worlds 2024", "2024-11-02", "GF", "1", "5",
        ...      "T1", "C9", "T1", "32:14",
        ...      "18","25","4","52000","8","4","2",
        ...      "4","10","18","38000","2","1","0"],
        ... ]
        >>> base = parse_LoL(players, coaches, matches, teams, "Worlds2024")
        >>> base.nom
        'Worlds2024'
        >>> len(base.competitions)
        1
    """
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

    # Ajout des coachs 
    for c in range(1, len(coach)):          
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
                e.ajouter_joueur(Joueur(pseudo=player[j][0],   
                                        nom=player[j][1],    
                                        nationalite=player[j][2],   
                                        date_naissance=player[j][3],
                                        role=player[j][4]))       

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