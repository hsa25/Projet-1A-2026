from ..Model.Joueur import Joueur
from ..Model.Equipe import Equipe
from ..Model.Match import Match
from ..Model.Competition import Competition
from ..Model.Base import Base
from ..Model.Sport import Sport


def parse_chess(player: list[list[str]],
                match: list[list[str]],
                nom_base: str) -> Base:
    """
    Parse des données brutes d'échecs et retourne un objet Base structuré.

    Cette fonction transforme deux tableaux 2D (joueurs et matchs) en un objet
    Base contenant une unique Competition regroupant l'ensemble des équipes,
    joueurs et matchs avec leurs statistiques Elo.

    Un nettoyage préalable des noms est effectué pour supprimer les guillemets
    et virgules éventuellement présents dans les données source.

    Args:
        player (list[list[str]]): Tableau 2D des joueurs.
            La ligne 0 est ignorée (en-tête).
            Format des lignes suivantes :
                [0] nom            - Nom du joueur (nettoyé des '"' et ',')
                [1] id             - Identifiant unique du joueur
                [2] date_naissance - Date de naissance
                [3] genre          - Genre du joueur
                [4] region_big     - Pays / région complète
                [5] role           - Titre FIDE ou rôle (ex: "GM", "IM")
                [6] elo_standard   - Classement Elo en partie classique
                [7] elo_rapide     - Classement Elo en partie rapide
                [8] elo_blitz      - Classement Elo en blitz

        match (list[list[str]]): Tableau 2D des matchs.
            La ligne 0 est ignorée (en-tête).
            Les noms en colonnes [3] et [4] sont nettoyés des '"' et ','.
            Format des lignes suivantes :
                [0] round          - Tour du tournoi
                [1] groupe         - Groupe ou poule
                [2] ordre          - Ordre du match dans le tour
                [3] nom_joueur_1   - Nom du joueur 1 (clé de résolution)
                [4] nom_joueur_2   - Nom du joueur 2 (clé de résolution)
                [5] score_1        - Score du joueur 1 (entier)
                [6] score_2        - Score du joueur 2 (entier)
                [7] seed_joueur_1  - Classement/seed du joueur 1 (float)
                [8] seed_joueur_2  - Classement/seed du joueur 2 (float)

        nom_base (str): Nom attribué à l'objet Base retourné. Utilisé également
            comme nom de l'unique Competition créée.

    Returns:
        Base: Objet Base peuplé avec :
            - sport        : Sport('Échecs', 1)
            - equipes      : liste d'objets Equipe, chacun contenant un Joueur
                             avec ses trois classements Elo en statistiques
            - competitions : liste contenant une unique Competition dont le nom
                             est nom_base, regroupant tous les Matchs
                             
    Example:
        >>> players = [
        ...     ["nom", "id", "naissance", "genre", "pays", "titre",
        ...      "elo_std", "elo_rapide", "elo_blitz"],
        ...     ["Magnus Carlsen", "1", "1990-11-30", "M", "Norway", "GM",
        ...      "2839", "2820", "2886"],
        ...     ["Fabiano Caruana", "2", "1992-07-30", "M", "USA", "GM",
        ...      "2804", "2760", "2755"],
        ... ]
        >>> matches = [
        ...     ["round", "groupe", "ordre", "j1", "j2", "s1", "s2", "seed1", "seed2"],
        ...     ["1", "A", "1", "Magnus Carlsen", "Fabiano Caruana",
        ...      "1", "0", "1.0", "2.0"],
        ... ]
        >>> base = parse_chess(players, matches, "WorldChess2024")
        >>> base.nom
        'WorldChess2024'
        >>> len(base.competitions)
        1
    """
    # Modification du formatage pour ne pas avoir les "" et , dans le nom
    # (compatible même avec les typos qui les oublient en plus \^0^/)
    for i in range(1,len(player)):
        player[i][0].replace('"', '')
        player[i][0].replace(',', '')

    for j in range(1, len(match)):
        match[j][3] = match[j][3].replace('"', '')
        match[j][3] = match[j][3].replace(',', '')
        match[j][4] = match[j][4].replace('"', '')
        match[j][4] = match[j][4].replace(',', '')

    liste_equipe = []
    liste_matchs = []

    for i in range(1, len(player)):
        liste_equipe.append(Equipe(nom=player[i][0],
                                   region_big=player[i][4],
                                   joueurs=[Joueur(nom=player[i][0],
                                                  id=int(player[i][1]),
                                                  date_naissance=player[i][2],
                                                  genre=player[i][3],
                                                  role=player[i][5],
                                                  statistiques={'elo_standard': player[i][6],
                                                                'elo_rapide': player[i][7],
                                                                'elo_blitz': player[i][8]}
                                                  )]))

    for j in range(1, len(match)):
        j1 = 0
        j2 = 0
        for k in range(len(liste_equipe)):
            if match[j][3] == liste_equipe[k].nom:
                j1 = liste_equipe[k]
            if match[j][4] == liste_equipe[k].nom:
                j2 = liste_equipe[k]
        liste_matchs.append(Match(round=match[j][0],
                                  groupe=match[j][1],
                                  ordre=match[j][2],
                                  equipe_1=j1,
                                  equipe_2=j2,
                                  score_1=[int(match[j][5])],
                                  score_2=[int(match[j][6])],
                                  stats={'seed_joueur_1': float(match[j][7]),
                                         'seed_joueur_2': float(match[j][8])}))

    return Base(nom=nom_base,
                sport=Sport('Échecs', 1),
                equipes=liste_equipe,
                competitions=[Competition(nom=nom_base,
                                          matchs=liste_matchs)])