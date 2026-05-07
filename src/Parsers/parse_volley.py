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
    """
    Parse des données brutes de volleyball et retourne un objet Base structuré.

    Cette fonction transforme quatre tableaux 2D (joueurs, coachs, matchs,
    pays/équipes nationales) en un objet Base contenant une unique Competition
    regroupant l'ensemble des équipes nationales, coachs, joueurs et matchs
    du tournoi.

    Args:
        player (list[list[str]]): Tableau 2D des joueurs.
            La ligne 0 est ignorée (en-tête).
            Format des lignes suivantes :
                [0] nom            - Nom du joueur
                [1] abrev_equipe   - Abréviation du pays (clé de jointure)
                [2] taille         - Taille en mètres (float)
                [3] date_naissance - Date de naissance
                [4] nationalite    - Nationalité du joueur
                [5] pseudo         - Numéro de maillot ou surnom

        coach (list[list[str]]): Tableau 2D des coachs.
            La ligne 0 est ignorée (en-tête).
            Format des lignes suivantes :
                [0] nom            - Nom du coach
                [1] date_naissance - Date de naissance
                [2] genre          - Genre du coach
                [3] role           - Rôle (ex: "Head Coach", "Assistant")
                [4] abrev_equipe   - Abréviation du pays (clé de jointure)

        match (list[list[str]]): Tableau 2D des matchs.
            La ligne 0 est ignorée (en-tête).
            Format des lignes suivantes :
                [0] date         - Date du match
                [1] round        - Tour du tournoi
                [2] abrev_eq1    - Abréviation équipe 1 (clé de résolution)
                [3] abrev_eq2    - Abréviation équipe 2 (clé de résolution)
                [4] score_1      - Score final équipe 1
                [5] score_2      - Score final équipe 2

        country (list[list[str]]): Tableau 2D des équipes nationales.
            La ligne 0 est ignorée (en-tête).
            Format des lignes suivantes :
                [0] abrev  - Abréviation du pays (clé de jointure avec joueurs,
                             coachs et matchs)
                [1] surnom - Surnom de l'équipe (ex: "Les Bleus")
                [2] nom    - Nom complet du pays (ex: "France")

        nom_base (str): Nom attribué à l'objet Base retourné. Utilisé également
            comme nom de l'unique Competition créée.

    Returns:
        Base: Objet Base peuplé avec :
            - sport        : Sport('Volleyball', 13)
            - equipes      : liste d'objets Equipe (équipes nationales) avec
                             leurs Joueurs et Coachs
            - competitions : liste contenant une unique Competition dont le nom
                             est nom_base, regroupant tous les Matchs

    Notes:
        - La ligne 0 de chaque tableau est toujours ignorée (en-tête).
        - Il existe un bug dans la boucle de création des matchs : `for m in
          range(1, match)` utilise le tableau match lui-même au lieu de sa
          longueur. Il faudrait écrire `range(1, len(match))`.
        - Les coachs et joueurs sont rattachés à leur équipe par correspondance
          d'abréviation (coach[c][4] et player[j][1] == equipe.abrev). Un coach
          ou joueur sans équipe correspondante est silencieusement ignoré.
        - La résolution des équipes dans les matchs se fait par correspondance
          match[m][2]/match[m][3] == equipe.abrev. Si aucune correspondance
          n'est trouvée, la variable d'équipe vaut 0 (entier), ce qui peut
          provoquer des erreurs en aval.
        - La taille_equipe passée à Sport est 13, ce qui correspond au nombre
          de joueurs dans un effectif de volleyball (6 titulaires + remplaçants).
        - Tous les matchs appartiennent à une seule Competition portant le nom
          de nom_base.

    Example:
        >>> countries = [
        ...     ["abrev", "surnom", "nom"],
        ...     ["FRA", "Les Bleus",  "France"],
        ...     ["BRA", "Seleção",    "Brazil"],
        ... ]
        >>> coaches = [
        ...     ["nom", "naissance", "genre", "role", "equipe"],
        ...     ["Andrea Giani", "1970-06-08", "M", "Head Coach", "FRA"],
        ... ]
        >>> players = [
        ...     ["nom", "equipe", "taille", "naissance", "nationalite", "pseudo"],
        ...     ["Earvin Ngapeth", "FRA", "1.94", "1991-02-12", "French", "9"],
        ... ]
        >>> matches = [
        ...     ["date", "round", "eq1", "eq2", "s1", "s2"],
        ...     ["2024-08-10", "Pool A", "FRA", "BRA", "3", "1"],
        ... ]
        >>> base = parse_volley(players, coaches, matches, countries, "Olympics2024")
        >>> base.nom
        'Olympics2024'
        >>> len(base.competitions)
        1
        >>> base.equipes[0].nom
        'France'
    """
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
    for m in range(1, match):       # bug: devrait être range(1, len(match))
        # Recherche des équipes en fonction de leur nom
        j1 = 0
        j2 = 0
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
                 competitions=[Competition(nom=nom_base,
                                           matchs=liste_matchs)],
                 equipes=liste_equipes))