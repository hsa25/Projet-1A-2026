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
    """
    Parse des données brutes de Counter-Strike 2 et retourne un objet Base structuré.

    Cette fonction transforme quatre tableaux 2D (joueurs, coachs, matchs, équipes)
    en un objet Base contenant une unique Competition regroupant l'ensemble des
    équipes, coachs, joueurs et matchs du tournoi.

    Args:
        player (list[list[str]]): Tableau 2D des joueurs.
            La ligne 0 est ignorée (en-tête).
            Format des lignes suivantes :
                [0] pseudo         - Pseudo en jeu du joueur
                [1] nom            - Nom réel du joueur
                [2] nationalite    - Nationalité du joueur
                [3] date_naissance - Date de naissance
                [4] role           - Rôle en jeu (ex: "IGL", "AWPer", "Entry")
                [5] nom_equipe     - Nom de l'équipe (clé de jointure)

        coach (list[list[str]]): Tableau 2D des coachs.
            La ligne 0 est ignorée (en-tête).
            Format des lignes suivantes :
                [0] pseudo         - Pseudo du coach
                [1] nom            - Nom réel du coach
                [2] nationalite    - Nationalité du coach
                [3] date_naissance - Date de naissance
                [4] nom_equipe     - Nom de l'équipe (clé de jointure)

        match (list[list[str]]): Tableau 2D des matchs.
            La ligne 0 est ignorée (en-tête).
            Format des lignes suivantes :
                [0] date           - Date du match
                [1] groupe         - Groupe ou poule
                [2] round          - Tour du tournoi
                [3] best_of        - Format (ex: "3" pour BO3)
                [4] nom_equipe_1   - Nom de l'équipe 1 (clé de résolution)
                [5] nom_equipe_2   - Nom de l'équipe 2 (clé de résolution)
                [6] score_1        - Score final de l'équipe 1
                [7] score_2        - Score final de l'équipe 2

        team (list[list[str]]): Tableau 2D des équipes.
            La ligne 0 est ignorée (en-tête).
            Format des lignes suivantes :
                [0] nom            - Nom complet de l'équipe
                [1] abrev          - Abréviation (ex: "NAVI")
                [2] region_small   - Région courte (ex: "EU")
                [3] region_big     - Région complète (ex: "Europe")

        nom_base (str): Nom attribué à l'objet Base retourné. Utilisé également
            comme nom de l'unique Competition créée.

    Returns:
        Base: Objet Base peuplé avec :
            - sport        : Sport(nom='Counter Strike 2', taille_equipe=5)
            - equipes      : liste d'objets Equipe avec leurs Joueurs et Coachs
            - competitions : liste contenant une unique Competition dont le nom
                             est nom_base, regroupant tous les Matchs

    Notes:
        - La ligne 0 de chaque tableau est toujours ignorée (en-tête).
        - Les coachs puis les joueurs sont rattachés à leur équipe via
          correspondance par nom (coach[c][4] == equipe.nom et
          player[j][5] == equipe.nom). Un coach ou joueur sans équipe
          correspondante est silencieusement ignoré.
        - La résolution des équipes dans les matchs se fait par correspondance
          match[m][4]/match[m][5] == equipe.nom. Si aucune correspondance
          n'est trouvée, la variable d'équipe vaut 0 (entier), ce qui peut
          provoquer des erreurs en aval — les données doivent être cohérentes.
        - Il existe un bug dans la boucle d'ajout des joueurs : le pseudo est
          lu depuis player[c][0] (indice de boucle des coachs) au lieu de
          player[j][0]. Il faudrait écrire player[j][0].
        - Tous les matchs appartiennent à une seule Competition portant le nom
          de nom_base, ce qui reflète le principe "1 base = 1 compétition".

    Example:
        >>> teams = [
        ...     ["nom", "abrev", "region_small", "region_big"],
        ...     ["Natus Vincere", "NAVI", "EU", "Europe"],
        ...     ["Team Vitality",  "VIT",  "EU", "Europe"],
        ... ]
        >>> coaches = [
        ...     ["pseudo", "nom", "nationalite", "naissance", "equipe"],
        ...     ["B1ad3", "Andrii Horodenskyi", "Ukraine", "1991-05-19",
        ...      "Natus Vincere"],
        ... ]
        >>> players = [
        ...     ["pseudo", "nom", "nationalite", "naissance", "role", "equipe"],
        ...     ["s1mple", "Oleksandr Kostyliev", "Ukraine", "1997-10-02",
        ...      "AWPer", "Natus Vincere"],
        ... ]
        >>> matches = [
        ...     ["date", "groupe", "round", "best_of", "eq1", "eq2", "s1", "s2"],
        ...     ["2024-03-15", "A", "QF", "3",
        ...      "Natus Vincere", "Team Vitality", "2", "1"],
        ... ]
        >>> base = parse_CS2(players, coaches, matches, teams, "IEM2024")
        >>> base.nom
        'IEM2024'
        >>> len(base.competitions)
        1
    """
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
                e.ajouter_joueur(Joueur(pseudo=player[c][0],  # bug: devrait être player[j][0]
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