from src.Model.Sport import Sport
from src.Analysis import display all competitions

supported_sport = [
    Sport(name="football", team_sport=True),
    Sport(name="tennis atp",team_sport=False),
    Sport(name="tennis wta",team_sport=False),
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


display_all_competitions = {"tennis atp": ["Brisbane", "United Cup","Hong Kong",
                                        "Adelaide", "Auckland", "Australian Open",
                                        "Montpellier", "Cordoba","Dallas", "Marseille",
                                        "Delray Beach", "Buenos Aires", "Rotterdam",
                                        "Doha", "Los Cabos", "Rio De Janeiro",
                                        "Acapulco", "Dubai", "Santiago",
                                        "Indian Wells", "Miami Masters", "Estoril",
                                        "Houston", "Marrakech", "Monte Carlo Masters",
                                        "Barcelona", "Munich", "Bucharest",
                                        "Madrid Masters", "Rome Masters","Geneva",
                                        "Lyon", "Roland Garros", "s Hertogenbosch",
                                        "Stuttgart", "Halle", "Queen's Club",
                                        "Mallorca","Eastbourne", "Wimbledon",
                                        "Gstaad", "Hamburg", "Bastad", "Newport",
                                        "Atlanta", "Kitzbuhel","Umag", "Washington",
                                        "Paris Olympics","Canada Masters", "Cincinnati Masters",
                                        "Winston-Salem", "Us Open", "Chengdu", "Hangzhou",
                                        "Laver Cup", "Tokyo","Beijing", "Shanghai Masters",
                                        "Almaty", "Antwerp", "Stockholm", "Basel",
                                        "Vienna", "Paris Masters", "Belgrade",
                                        "Metz", "Tour Finals", "Next Gen Finals",
                                        "Davis Cup"],
                            "football": ["Ligue des champions", "Jupiler League", 
                                        "Premier League", "Ligue 1", "Bundesliga", 
                                        "Serie A", "Eredivisie", "Ekstraklasa", 
                                        "Liga ZON Sagres","Scotland Premier League", 
                                        "LIGA BBVA", "Super League"],
                            "badminton": ["JO 2024 Homme", "JO 2024 Femme"],
                            "basketball": ["regular", "play-off"],
                            "échecs":["Coupe du Monde d'échecs de la FIDE"],
                            "counter strike 2": ["Major d'hiver 2025"],
                            "league of legends":["LEC Winter Split 2025"],
                            "starcraft 2": ["Global StarCraft II League 2016"],
                            }
selected_competitions = input(
    "Sélectionnez une compétition parmi {display_all_competitions(selected_sport)}")
    



