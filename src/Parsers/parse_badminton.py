from ..Model.Joueur import Joueur
from ..Model.Equipe import Equipe
from ..Model.Match import Match
from ..Model.Competition import Competition
from ..Model.Base import Base
from ..Model.Sport import Sport


def parse_badmintion(player: list[list[str]],
                     match: list[list[str]],
                     nom_base: str) -> Base:
    """
    Parse des données brutes de badminton et retourne un objet Base structuré.

    Cette fonction transforme deux tableaux 2D (joueurs et matchs) en un objet
    Base contenant l'ensemble des compétitions, équipes, joueurs et résultats
    de matchs associés.

    Args:
        player (list[list[str]]): Tableau 2D des joueurs/équipes.
            La ligne 0 est ignorée (en-tête).
            Format des lignes suivantes :
                [0] nom       - Nom du joueur / de l'équipe
                [1] region_small - Région courte (ex: "EUR")
                [2] region_big   - Région complète (ex: "Denmark")

        match (list[list[str]]): Tableau 2D des matchs.
            La ligne 0 est ignorée (en-tête).
            Format des lignes suivantes :
                [0]  nom de la compétition (clé unique de regroupement)
                [1]  ville de la compétition
                [2]  pays de la compétition
                [3]  date du match
                [4]  type de compétition
                [5]  round (tour)
                [6]  nom de l'équipe 1
                [7]  nom de l'équipe 2
                [8]  (non utilisé)
                [9]  scores du set 1, format "X-Y"
                [10] scores du set 2, format "X-Y"
                [11] scores du set 3, format "X-Y"

            Les scores [9], [10], [11] sont chacun séparés par '-' :
                score_1 regroupe les valeurs gauches (X) des trois sets,
                score_2 regroupe les valeurs droites (Y) des trois sets.

        nom_base (str): Nom attribué à l'objet Base retourné.

    Returns:
        Base: Objet Base peuplé avec :
            - sport   : Sport('Badminton', 1)
            - equipes : liste d'objets Equipe, chacun contenant un Joueur
            - competitions : liste d'objets Competition regroupant leurs Matchs

    Notes:
        - La ligne 0 de player et match est toujours ignorée (en-tête).
        - La résolution des équipes se fait par correspondance de noms entre
          match[j][6]/match[j][7] et liste_equipe. Si aucune correspondance
          n'est trouvée, la variable d'équipe vaut 0 (entier), ce qui peut
          provoquer des erreurs en aval — les données doivent être cohérentes.
        - Le regroupement des compétitions utilise match[j][0] comme clé de
          dictionnaire. La première occurrence crée l'entrée ; les suivantes
          ajoutent un Match à la liste existante.
        - Chaque Equipe est créée avec un unique Joueur portant le même nom,
          reflétant la structure individuelle des épreuves de badminton.

    Example:
        >>> players = [
        ...     ["Name", "Region", "Country"],           # en-tête
        ...     ["Viktor Axelsen", "EUR", "Denmark"],
        ...     ["Kento Momota",   "ASI", "Japan"],
        ... ]
        >>> matches = [
        ...     ["Comp", "City", "Country", "Date", "Type", "Round",
        ...      "P1", "P2", "?", "S1", "S2", "S3"],   # en-tête
        ...     ["BWF WC", "Paris", "France", "2024-08-05", "WC", "QF",
        ...      "Viktor Axelsen", "Kento Momota", "", "21-18", "19-21", "21-15"],
        ... ]
        >>> base = parse_badmintion(players, matches, "BWF_2024")
        >>> base.nom
        'BWF_2024'
    """
    liste_equipe = []
    liste_competition = []
    competitions = {}

    for i in range(1, len(player)):
        liste_equipe.append(Equipe(nom=player[i][0],
                                   region_small=player[i][1],
                                   region_big=player[i][2],
                                   joueurs=Joueur(nom=player[i][0])))

    for j in range(1, len(match)):
        j1 = 0
        j2 = 0
        for k in range(len(liste_equipe)):
            if match[j][6] == liste_equipe[k].nom:
                j1 = liste_equipe[k]
            if match[j][7] == liste_equipe[k].nom:
                j2 = liste_equipe[k]
        s1 = match[j][9].split('-')
        s2 = match[j][10].split('-')
        s3 = match[j][11].split('-')

        if match[j][0] not in competitions:
            competitions[match[j][0]] = [match[j][1],
                                         match[j][2],
                                         match[j][4],
                                         [Match(equipe_1=j1,
                                                equipe_2=j2,
                                                round=match[j][5],
                                                date=match[j][3],
                                                score_1=[int(s1[0]),
                                                         int(s2[0]),
                                                         int(s3[0])],
                                                score_2=[int(s1[1]),
                                                         int(s2[1]),
                                                         int(s3[1])])]]
        else:
            competitions[match[j][0]][3].append(Match(equipe_1=j1,
                                                      equipe_2=j2,
                                                      round=match[j][5],
                                                      date=match[j][3],
                                                      score_1=[int(s1[0]),
                                                               int(s2[0]),
                                                               int(s3[0])],
                                                      score_2=[int(s1[1]),
                                                               int(s2[1]),
                                                               int(s3[1])]))
    for comp in competitions:
        liste_competition.append(Competition(nom=comp,
                                             ville=competitions[comp][0],
                                             pays=competitions[comp][1],
                                             type=competitions[comp][2],
                                             matchs=competitions[comp][3]))

    return (Base(nom=nom_base,
                 sport=Sport('Badminton', 1),
                 competitions=liste_competition,
                 equipes=liste_equipe))