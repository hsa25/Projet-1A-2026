import os
import csv
from ..Model.Joueur import Joueur
from ..Model.Equipe import Equipe
from ..Model.Match import Match
from ..Model.Competition import Competition
from ..Model.Base import Base
from ..Model.Sport import Sport


def parse_foot_el(chemin, nom_base: str) -> Base:

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
            abreviation=fichier_equipes[i][3],        
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
            nom_competition = f"{info_ligue['nom']} {saison}" # Résultat : "France Ligue 1 2015/2016"
            
            competitions[cle_comp] = [nom_competition,           
                                      "",                       
                                      info_ligue["pays"],       
                                      "Championnat",             
                                      [Match(equipe_1=equipe_domicile,
                                             equipe_2=equipe_exterieur,
                                             date=fichier_matchs[j][5],          
                                             round=fichier_matchs[j][4],         
                                             score_1=int(fichier_matchs[j][9]),
                                             score_2=int(fichier_matchs[j][10]))]] 
        else:
            competitions[cle_comp][4].append(Match(equipe_1=equipe_domicile,
                                                   equipe_2=equipe_exterieur,
                                                   date=fichier_matchs[j][5],
                                                   round=fichier_matchs[j][4],
                                                   score_1=int(fichier_matchs[j][9]),
                                                   score_2=int(fichier_matchs[j][10])))

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