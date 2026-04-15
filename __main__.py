from src.Model.Sport import Sport
from src.Analysis import display all competitions

supported_sport = [
    Sport(name="football", team_sport=True),
    Sport(name="tennis",team_sport=False),
    Sport(name="volleyball", team_sport= True),
    Sport(name="basketball", team_sport=True),
    Sport(name="league of legends", team_sport=True),
    Sport(name="badminton", team_sport= False),
    Sport(name="échecs", team_sport=False),
    Sport(name="counter strike 2", team_sport=True),
    Sport(name="starcraft 2", team_sport=False)
    ]

selected_sport = input("Sélectionnez un sport parmi {supported_sports}")
if selected_sport not in supported_sports:
    Raise Exception("Le sport sélectionné n'est pas encore supporté par l'appli")


display_all_competitions = {"tennis": ["wta","atp"],"footba}
selected_competitions = input(
    "Sélectionnez une compétition parmi {display_all_competitions(selected_sport)}")
    











import pandas as pd

from src.Parsers.parse_csv import parse_players_csv
from src.Analysis.pandas.GoatFinder import find_the_goat_in_df
from src.Analysis.homemade.GoatFinder import find_the_goat

setting = input("Select a setting, 0=pandas-powered, 1=àlamain-powered\n")

if setting == "0":
    players_df = pd.read_csv("./data/players.csv")
else:
    players = parse_players_csv("./data/players.csv")

print("Select your journey through the data")
print("1 - I want to know who is the greatest football player of all time")
input("2 - Just kidding, there's only one option\n")

if setting == "0":
    the_goat = find_the_goat_in_df(players_df)
else:
    the_goat = find_the_goat(players)



