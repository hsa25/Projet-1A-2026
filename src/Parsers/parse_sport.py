import os
import csv
from ..Model.Sport import Sport
from ..Model.Base import Base
from .parse_badminton import parse_badminton
from .parse_basket import parse_basket
from .parse_chess import parse_chess
from .parse_CS2 import parse_CS2
from .parse_football_cl import parse_football_cl
from .parse_LoL import parse_LoL
from .parse_starcraft2 import parse_starcraft2
from .parse_tennism import parse_tennism
from .parse_volleyf import parse_volleyf
from .parse_tennisf import parse_tennisf
from .parse_volleym import parse_volleym


def parse_sport(sport: Sport, path, nom_base) -> Base:
    if sport.nom_sport == 'Badminton':
        player = list(csv.reader(open(os.path.join(path, "player.csv"))))
        match = list(csv.reader(open(os.path.join(path, "match.csv"))))
        return parse_badminton(player, match, nom_base)
    if sport.nom_sport == 'Basketball':
        player = list(csv.reader(open(os.path.join(path, "player.csv"))))
        game = list(csv.reader(open(os.path.join(path, "game.csv"))))
        team = list(csv.reader(open(os.path.join(path, "team.csv"))))
        return parse_basket(player, game, team, nom_base)
    if sport.nom_sport == 'Échecs':
        player = list(csv.reader(open(os.path.join(path, "player.csv"))))
        match = list(csv.reader(open(os.path.join(path, "match.csv"))))
        return parse_chess(player, match, nom_base)
    if sport.nom_sport == 'Counter Strike 2':
        player = list(csv.reader(open(os.path.join(path, "player.csv"))))
        match = list(csv.reader(open(os.path.join(path, "match.csv"))))
        coach = list(csv.reader(open(os.path.join(path, "coach.csv"))))
        team = list(csv.reader(open(os.path.join(path, "team.csv"))))
        return parse_CS2(player, coach, match, team, nom_base)
    if sport.nom_sport == 'Football Champions League':
        player = list(csv.reader(open(os.path.join(path, "player.csv"))))
        match = list(csv.reader(open(os.path.join(path, "match.csv"))))
        team = list(csv.reader(open(os.path.join(path, "team.csv"))))
        return parse_football_cl(player, match, team, nom_base)
    if sport.nom_sport == 'League of Legends':
        player = list(csv.reader(open(os.path.join(path, "player.csv"))))
        match = list(csv.reader(open(os.path.join(path, "match.csv"))))
        coach = list(csv.reader(open(os.path.join(path, "coach.csv"))))
        team = list(csv.reader(open(os.path.join(path, "team.csv"))))
        return parse_LoL(player, coach, match, team, nom_base)
    if sport.nom_sport == 'Starcraft 2':
        player = list(csv.reader(open(os.path.join(path, "player.csv"))))
        match = list(csv.reader(open(os.path.join(path, "match.csv"))))
        return parse_starcraft2(player, match, nom_base)
    if sport.nom_sport == 'Tennis masculin':
        player = list(csv.reader(open(os.path.join(path, "atp_players_2024.csv"))))
        match = list(csv.reader(open(os.path.join(path, "atp_matches_2024.csv"))))
        return parse_tennism(player, match, nom_base)
    if sport.nom_sport == 'Tennis féminin':
        player = list(csv.reader(open(os.path.join(path, "wta_players_2024.csv"))))
        match = list(csv.reader(open(os.path.join(path, "wta_matches_2024.csv"))))
        return parse_tennisf(player, match, nom_base)
    if sport.nom_sport == 'Volley masculin':
        player = list(csv.reader(open(os.path.join(path, "player_men.csv"))))
        match = list(csv.reader(open(os.path.join(path, "match_men.csv"))))
        coach = list(csv.reader(open(os.path.join(path, "coach_men.csv"))))
        country = list(csv.reader(open(os.path.join(path, "country.csv"))))
        return parse_volleym(player, coach, match, country, nom_base)
    if sport.nom_sport == 'Volley féminin':
        player = list(csv.reader(open(os.path.join(path, "player_women.csv"))))
        match = list(csv.reader(open(os.path.join(path, "match_women.csv"))))
        coach = list(csv.reader(open(os.path.join(path, "coach_women.csv"))))
        country = list(csv.reader(open(os.path.join(path, "country.csv"))))
        return parse_volleyf(player, coach, match, country, nom_base)