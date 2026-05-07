import os
import csv
from ..Model.Joueur import Joueur
from ..Model.Equipe import Equipe
from ..Model.Match import Match
from ..Model.Competition import Competition
from ..Model.Base import Base
from ..Model.Sport import Sport


def parse_foot_el(chemin: str, nom_base: str) -> Base:
    """
    Parse un dataset de football européen depuis un répertoire de fichiers CSV
    et retourne un objet Base structuré.

    Cette fonction lit cinq fichiers CSV depuis le répertoire indiqué, construit
    les équipes, joueurs et matchs correspondants, puis regroupe les matchs par
    compétition (ligue + saison). Contrairement aux autres parsers, les données
    sont lues directement depuis le disque et non passées en paramètre.

    Args:
        chemin (str): Chemin vers le répertoire contenant les cinq fichiers CSV
            attendus :
                - country.csv  : liste des pays
                - league.csv   : liste des ligues
                - team_2.csv   : liste des équipes
                - player_2.csv : liste des joueurs
                - match.csv    : liste des matchs

        nom_base (str): Nom attribué à l'objet Base retourné.

    Formats des fichiers CSV (ligne 0 = en-tête, ignorée) :

        country.csv :
            [0] id_pays  - Identifiant unique du pays
            [1] nom_pays - Nom du pays

        league.csv :
            [0] id_ligue  - (non utilisé directement)
            [1] id_pays   - Clé de jointure vers country.csv
            [2] nom_ligue - Nom de la ligue (ex: "France Ligue 1")
            (index 0 ignoré, clé du dictionnaire = valeur brute de la ligne)

        team_2.csv :
            [1] id         - Identifiant unique de l'équipe (api_id)
            [2] nom        - Nom complet de l'équipe
            [3] abrev - Abréviation de l'équipe

        player_2.csv :
            [1] id             - Identifiant unique du joueur (api_id)
            [2] nom            - Nom du joueur
            [3] date_naissance - Date de naissance
            [4] poids          - Poids du joueur
            [5] taille         - Taille du joueur

        match.csv :
            [2]  id_ligue          - Clé de jointure vers league.csv
            [3]  saison            - Saison (ex: "2015/2016")
            [4]  round             - Journée / tour
            [5]  date              - Date du match
            [7]  home_team_api_id  - ID de l'équipe domicile (clé de résolution)
            [8]  away_team_api_id  - ID de l'équipe extérieur (clé de résolution)
            [9]  score_1           - Buts marqués par l'équipe domicile
            [10] score_2           - Buts marqués par l'équipe extérieur

    Returns:
        Base: Objet Base peuplé avec :
            - sport        : Sport('Football', 1)
            - equipes      : liste d'objets Equipe (sans joueurs rattachés,
                             voir Notes)
            - competitions : liste d'objets Competition, une par couple
                             (ligue, saison), nommées selon le format
                             "<nom_ligue> <saison>" (ex: "France Ligue 1 2015/2016"),
                             de type "Championnat", chacune regroupant ses Matchs

    Notes:
        - La ligne 0 de chaque fichier CSV est toujours ignorée (en-tête).
        - Les fichiers sont ouverts sans gestionnaire de contexte (sans `with`) :
          ils ne sont pas explicitement fermés après lecture. Cela fonctionne
          mais n'est pas recommandé — préférer `with open(...) as f`.
        - Les joueurs sont bien créés dans liste_joueurs mais ne sont jamais
          rattachés à une équipe. La liste est construite puis inutilisée.
        - La résolution des équipes dans les matchs se fait par correspondance
          fichier_matchs[j][7]/[8] == equipe.id. Si aucune correspondance
          n'est trouvée, equipe_domicile ou equipe_exterieur vaut None, ce qui
          peut provoquer des erreurs en aval.
        - Le regroupement des compétitions utilise la clé "<id_ligue>_<saison>"
          (ex: "1_2015/2016"). La première occurrence crée l'entrée ; les
          suivantes ajoutent un Match à la liste existante.
        - Si un id_ligue présent dans match.csv est absent de league.csv,
          dictionnaire_ligues.get() retourne {"nom": "Inconnu", "pays": ""} par
          défaut, évitant un KeyError.
        - Les colonnes [0] de team_2.csv et player_2.csv (index 0) ne sont pas
          utilisées ; les identifiants métier sont en colonne [1].

    Example:
        >>> base = parse_foot_el("data/football/european", "EuropeanLeagues")
        >>> base.nom
        'EuropeanLeagues'
        >>> base.sport.nom
        'Football'
        >>> # Chaque compétition correspond à une ligue pour une saison donnée
        >>> base.competitions[0].nom
        'France Ligue 1 2015/2016'
    """
    # 1. Ouverture des 5 fichiers
    fichier_pays = list(csv.reader(open(os.path.join(chemin, "country.csv"), encoding="utf-8")))
    fichier_ligues = list(csv.reader(open(os.path.join(chemin, "league.csv"), encoding="utf-8")))
    fichier_equipes = list(csv.reader(open(os.path.join(chemin, "team_2.csv"), encoding="utf-8")))
    fichier_joueurs = list(csv.reader(open(os.path.join(chemin, "player_2.csv"), encoding="utf-8")))
    fichier_matchs = list(csv.reader(open(os.path.join(chemin, "match.csv"), encoding="utf-8")))

    liste_equipes = []
    liste_joueurs = []
    liste_competitions = []
    competitions = {}

    # 2. Création de dictionnaires pour lier les ID de Pays et Ligues facilement
    dictionnaire_pays = {}
    for i in range(1, len(fichier_pays)):
        dictionnaire_pays[fichier_pays[i][0]] = fichier_pays[i][1]  # {id_pays: nom_pays}

    dictionnaire_ligues = {}
    for i in range(1, len(fichier_ligues)):
        dictionnaire_ligues[fichier_ligues[i][0]] = {
            "nom": fichier_ligues[i][2],
            "pays": dictionnaire_pays[fichier_ligues[i][1]]
        }

    for i in range(1, len(fichier_joueurs)):
        liste_joueurs.append(Joueur(
            id=fichier_joueurs[i][1],
            nom=fichier_joueurs[i][2],
            date_naissance=fichier_joueurs[i][3],
            taille=fichier_joueurs[i][5],
            poids=fichier_joueurs[i][4]
        ))

    for i in range(1, len(fichier_equipes)):
        liste_equipes.append(Equipe(
            id=fichier_equipes[i][1],
            nom=fichier_equipes[i][2],
            abrev=fichier_equipes[i][3],
        ))

    for j in range(1, len(fichier_matchs)):
        equipe_domicile = None
        equipe_exterieur = None

        for k in range(len(liste_equipes)):
            if fichier_matchs[j][7] == liste_equipes[k].id:    # home_team_api_id (indice 7)
                equipe_domicile = liste_equipes[k]
            if fichier_matchs[j][8] == liste_equipes[k].id:    # away_team_api_id (indice 8)
                equipe_exterieur = liste_equipes[k]

        id_ligue = fichier_matchs[j][2]   # league_id (indice 2)
        saison = fichier_matchs[j][3]     # season (indice 3, ex: "2015/2016")

        # Clé unique pour chaque saison de chaque ligue (ex: "Ligue 1 + 2015/2016")
        cle_comp = f"{id_ligue}_{saison}"

        if cle_comp not in competitions:
            info_ligue = dictionnaire_ligues.get(id_ligue, {"nom": "Inconnu", "pays": ""})
            nom_competition = f"{info_ligue['nom']} {saison}"  # Résultat : "France Ligue 1 2015/2016"

            competitions[cle_comp] = [nom_competition,
                                      "",
                                      info_ligue["pays"],
                                      "Championnat",
                                      [Match(equipe_1=equipe_domicile,
                                             equipe_2=equipe_exterieur,
                                             date=fichier_matchs[j][5],
                                             round=fichier_matchs[j][4],
                                             score_1=[int(fichier_matchs[j][9])],
                                             score_2=[int(fichier_matchs[j][10])])]]
        else:
            competitions[cle_comp][4].append(Match(equipe_1=equipe_domicile,
                                                   equipe_2=equipe_exterieur,
                                                   date=fichier_matchs[j][5],
                                                   round=fichier_matchs[j][4],
                                                   score_1=[int(fichier_matchs[j][9])],
                                                   score_2=[int(fichier_matchs[j][10])]))

    # 6. Finalisation des compétitions et de la base
    for comp in competitions:
        liste_competitions.append(Competition(nom=competitions[comp][0],
                                              ville=competitions[comp][1],
                                              pays=competitions[comp][2],
                                              type=competitions[comp][3],
                                              matchs=competitions[comp][4]))

    return Base(nom=nom_base,
                sport=Sport('Football', 1),
                competitions=liste_competitions,
                equipes=liste_equipes)