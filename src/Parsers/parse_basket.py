import os
import csv
from ..Model.Joueur import Joueur
from ..Model.Equipe import Equipe
from ..Model.Match import Match
from ..Model.Competition import Competition
from ..Model.Base import Base
from ..Model.Sport import Sport


def parse_basket(path, nom_base: str) -> Base:

    team = list(csv.reader(open(os.path.join(path, "team.csv"), encoding="utf-8")))
    player = list(csv.reader(open(os.path.join(path, "player.csv"), encoding="utf-8")))
    game = list(csv.reader(open(os.path.join(path, "game.csv"), encoding="utf-8")))

    liste_equipe = []
    liste_competition = []
    competitions = {}

    # 1. Création des équipes
    for i in range(1, len(team)):
        liste_equipe.append(Equipe(id=team[i][0],            
                                   nom=team[i][1],            
                                   abrev=team[i][2],     
                                   surnom=team[i][3],          
                                   region_small=team[i][4],    
                                   region_big=team[i][5],      
                                   joueurs=[]))

    # 2. Ajout des joueurs aux équipes
    for i in range(1, len(player)):
        for k in range(len(liste_equipe)):
            if player[i][8] == liste_equipe[k].id:
                liste_equipe[k].joueurs.append(Joueur(
                    id=player[i][0],                           
                    nom=player[i][1] + " " + player[i][2],    
                    date_naissance=player[i][3],              
                    taille=player[i][4],                       
                    poids=player[i][5],                        
                    pseudo=player[i][6],                       
                    role=player[i][7]                         
                )) 


    for j in range(1, len(game)):
        j1 = 0
        j2 = 0
        
        
        for k in range(len(liste_equipe)):
            if game[j][2] == liste_equipe[k].id:               
                j1 = liste_equipe[k]
            if game[j][24] == liste_equipe[k].id:              
                j2 = liste_equipe[k]

        
        if game[j][0] not in competitions:
            competitions[game[j][0]] = ["",                    
                                        "USA",                 
                                        game[j][1],            
                                        [Match(equipe_1=j1,
                                               equipe_2=j2,
                                               date=game[j][4],                        
                                               round=game[j][1],                      
                                               score_1=int(game[j][23]) if game[j][23] else 0, 
                                               score_2=int(game[j][42]) if game[j][42] else 0,
                                               temps=game[j][5])]]                    
        else:
            competitions[game[j][0]][3].append(Match(equipe_1=j1,
                                                     equipe_2=j2,
                                                     date=game[j][4],
                                                     round=game[j][1],
                                                     score_1=int(game[j][23]) if game[j][23] else 0,
                                                     score_2=int(game[j][42]) if game[j][42] else 0,
                                                     temps=game[j][5]))

   
    for comp in competitions:
        liste_competition.append(Competition(nom=f"Saison {comp}",
                                             ville=competitions[comp][0],
                                             pays=competitions[comp][1],
                                             type=competitions[comp][2],
                                             matchs=competitions[comp][3]))

    return (Base(nom=nom_base,
                 sport=Sport('Basketball', 1),
                 competitions=liste_competition,
                 equipes=liste_equipe))