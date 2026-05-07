from ..Model.Joueur import Joueur
from ..Model.Equipe import Equipe
from ..Model.Match import Match
from ..Model.Competition import Competition
from ..Model.Base import Base
from ..Model.Sport import Sport


def parse_starcraft2(player: list[list[str]],
                     match: list[list[str]],
                     nom_base: str) -> Base:
    """
    Parse des données brutes de StarCraft II et retourne un objet Base structuré.

    Cette fonction transforme deux tableaux 2D (joueurs et matchs) en un objet
    Base contenant une unique Competition regroupant l'ensemble des équipes,
    joueurs et matchs du tournoi.

    Contrairement aux autres parsers, chaque joueur constitue sa propre équipe
    individuelle, et la résolution des équipes dans les matchs se fait par
    pseudo de joueur plutôt que par nom ou abréviation d'équipe.

    Args:
        player (list[list[str]]): Tableau 2D des joueurs.
            La ligne 0 est ignorée (en-tête).
            Format des lignes suivantes :
                [0] pseudo         - Pseudo en jeu du joueur (clé de résolution
                                     dans les matchs)
                [1] nom            - Nom réel du joueur
                [2] nationalite    - Nationalité du joueur
                [3] date_naissance - Date de naissance
                [4] role           - Race jouée (ex: "Terran", "Zerg", "Protoss")
                [5] nom_equipe     - Nom de l'équipe / organisation du joueur

        match (list[list[str]]): Tableau 2D des matchs.
            La ligne 0 est ignorée (en-tête).
            Format des lignes suivantes :
                [0] date      - Date du match
                [1] round     - Tour du tournoi
                [2] groupe    - Groupe ou poule
                [3] best_of   - Format (ex: "3" pour BO3, "5" pour BO5)
                [4] pseudo_j1 - Pseudo du joueur 1 (clé de résolution)
                [5] pseudo_j2 - Pseudo du joueur 2 (clé de résolution)
                [6] score_1   - Score du joueur 1
                [7] score_2   - Score du joueur 2

        nom_base (str): Nom attribué à l'objet Base retourné. Utilisé également
            comme nom de l'unique Competition créée.

    Returns:
        Base: Objet Base peuplé avec :
            - sport        : Sport('Starcraft2', 1)
            - equipes      : liste d'objets Equipe, une par joueur, chacune
                             contenant un unique Joueur
            - competitions : liste contenant une unique Competition dont le nom
                             est nom_base, regroupant tous les Matchs

    Notes:
        - La ligne 0 de chaque tableau est toujours ignorée (en-tête).
        - Chaque Equipe est créée à partir d'un seul joueur : player[i][5]
          fournit le nom de l'équipe et player[i][0] le pseudo du joueur unique
          qu'elle contient. Cela reflète la nature individuelle de StarCraft II.
        - La résolution des équipes dans les matchs se fait par correspondance
          match[j][4]/match[j][5] == equipe.joueurs[0].pseudo, et non par nom
          d'équipe comme dans les autres parsers. Si aucune correspondance n'est
          trouvée, la variable d'équipe vaut 0 (entier), ce qui peut provoquer
          des erreurs en aval — les pseudos doivent être cohérents entre les
          deux tableaux.
        - score_1 et score_2 sont stockés sous forme de listes à un élément
          ([match[j][6]] et [match[j][7]]) sans conversion en int — les valeurs
          restent des chaînes de caractères.
        - Tous les matchs appartiennent à une seule Competition portant le nom
          de nom_base.

    Example:
        >>> players = [
        ...     ["pseudo", "nom", "nationalite", "naissance", "race", "equipe"],
        ...     ["Serral",  "Joona Sotala",   "Finnish", "1998-05-07",
        ...      "Zerg",    "ENCE"],
        ...     ["Maru",    "Cho Seong-ju",   "Korean",  "1998-08-05",
        ...      "Terran",  "Team NV"],
        ... ]
        >>> matches = [
        ...     ["date", "round", "groupe", "best_of", "j1", "j2", "s1", "s2"],
        ...     ["2024-11-03", "SF", "A", "5", "Serral", "Maru", "3", "1"],
        ... ]
        >>> base = parse_starcraft2(players, matches, "BlizzCon2024")
        >>> base.nom
        'BlizzCon2024'
        >>> len(base.competitions)
        1
        >>> base.equipes[0].joueurs[0].pseudo
        'Serral'
    """
    liste_equipe = []
    liste_matchs = []

    for i in range(1, len(player)):
        liste_equipe.append(Equipe(nom=player[i][5],
                                   joueurs=[Joueur(nom=player[i][1],
                                                   pseudo=player[i][0],
                                                   nationalite=player[i][2],
                                                   date_naissance=player[i][3],
                                                   role=player[i][4],
                                                   )]))

    for j in range(1, len(match)):
        j1 = 0
        j2 = 0
        for k in range(len(liste_equipe)):
            if match[j][4] == liste_equipe[k].joueurs[0].pseudo:
                j1 = liste_equipe[k]
            if match[j][5] == liste_equipe[k].joueurs[0].pseudo:
                j2 = liste_equipe[k]
        liste_matchs.append(Match(equipe_1=j1,
                                  equipe_2=j2,
                                  date=match[j][0],
                                  round=match[j][1],
                                  groupe=match[j][2],
                                  best_of=match[j][3],
                                  score_1=[match[j][6]],
                                  score_2=[match[j][7]]))

    return (Base(nom=nom_base,
                 sport=Sport('Starcraft2', 1),
                 equipes=liste_equipe,
                 competitions=[Competition(nom=nom_base,
                                           matchs=liste_matchs)]))