import os
from src.Parsers.parse_sport import parse_sport

# Import des modèles
from src.Model.Sport import Sport

donnees_chargees = []
requete = ''
menu = 'principal'
sport_supportes = [Sport('Badminton', 'badminton'),
                   Sport('Basketball', 'basketball'),
                   Sport('Échecs', 'chess'),
                   Sport('Counter Strike 2', 'counter_strike_2'),
                   Sport('Football Champions League', 'football_champions_league'),
                   Sport('League of Legends', 'league_of_legends'),
                   Sport('Starcraft 2', 'starcraft_2'),
                   Sport('Tennis masculin', 'tennism'),
                   Sport('Tennis féminin', 'tennisf'),
                   Sport('Volley masculin', 'volleyballm'),
                   Sport('Volley féminin', 'volleyballf')]

while requete.lower() != 'quit':
    if requete.lower() != 'back':
        if menu == 'principal':
            print('Menu principal'.center(150, '-'))
            print('[0] Charger des données')
            print('[2] Observer les données')
            requete = input()
            if requete == '0':
                menu += '/charger'
            if requete == '2':
                menu += '/lire'
        if menu == 'principal/charger':
            choix = []
            for i in range(len(sport_supportes)):
                choix.append(str(i))
                print(f"[{i}] {sport_supportes[i].nom_sport}")
            requete = input()
            if requete in choix:
                sport_selection = int(requete)
                menu += '/dossier'
        if menu == 'principal/charger/dossier':
            choix = []
            path = os.path.join('data', sport_supportes[sport_selection].nom_dossier)
            for i in range(len(os.listdir(path))):
                choix.append(str(i))
                print(f"[{i}] {os.listdir(path)[i]}")
            requete = input()
            if requete in choix:
                nom_base = os.listdir(path)[int(requete)]
                path = os.path.join('data', sport_supportes[sport_selection].nom_dossier, nom_base)
                donnees_chargees.append(parse_sport(sport_supportes[sport_selection], path, nom_base))
                menu = 'principal'
        if menu == 'principal/lire':
            choix = []
            for i in range(len(donnees_chargees)):
                choix.append(str(i))
                print(f"[{i}] {donnees_chargees[i].nom}")
            requete = input()
            if requete in choix:
                base_choisie = int(requete)
                menu += '/base'
        if menu == 'principal/lire/base':
            print(donnees_chargees[base_choisie].nom.center(150, '-'))
            print(donnees_chargees[base_choisie].sport.nom_sport.center(150, '-'))
            print("[0] Équipes")
            print("[1] Competitions")
            requete = input()
            if requete == '0':
                menu += '/equipes'
            if requete == '1':
                menu += '/competitions'
        if menu == 'principal/lire/base/equipes':
            for e in (donnees_chargees[base_choisie].equipes):
                if len(e.joueurs) == 1:
                    print(e.joueurs[0].nom.center(150, '-'))
                    print(f"date de naissance : {e.joueurs[0].date_naissance}")
                    print(f"lieu de naissance : {e.joueurs[0].nationalite}")
                    print(f"taille : {e.joueurs[0].taille}")
                    print(f"poids : {e.joueurs[0].poids}")
                    print(f"pseudo : {e.joueurs[0].pseudo}")
                    print(f"genre : {e.joueurs[0].genre}")
                    print(f"role : {e.joueurs[0].role}")
                    print(f"statistiques : {e.joueurs[0].statistiques}")
                else:
                    choix = []
                    for i in range(len(donnees_chargees[base_choisie].equipes)):
                        choix.append(str(i))
                        print(f"[{i}] {donnees_chargees[base_choisie].equipes[i].nom}")
                    requete = input()
                    if requete in choix:
                        print(donnees_chargees[base_choisie].equipes[int(requete)].nom.center(150, '-'))
                        print(donnees_chargees[base_choisie].equipes[int(requete)].abrev.center(150, '-'))
                        print(donnees_chargees[base_choisie].equipes[int(requete)].region_small.center(150, '-'))
                        print(donnees_chargees[base_choisie].equipes[int(requete)].region_big.center(150, '-'))
                        for j in donnees_chargees[base_choisie].equipes[int(requete)].joueurs:
                            print("Joueurs".center(150, '+'))
                            print(j.nom.center(150, '-'))
                            print(f"date de naissance : {j.date_naissance}")
                            print(f"lieu de naissance : {j.nationalite}")
                            print(f"taille : {j.taille}")
                            print(f"poids : {j.poids}")
                            print(f"pseudo : {j.pseudo}")
                            print(f"genre : {j.genre}")
                            print(f"role : {j.role}")
                            print(f"statistiques : {j.statistiques}")
                requete = input()
        if menu = 'principal/lire/competitions':
        
    else:
        menu = menu[:- len(menu.split('/')[-1]) - 1]
        requete = ''



'''
# Import de l'analyseur
from src.Analysis.homemade.analyse_base import Analyseur


def charger_csv_liste(chemin: str) -> list:
    """Fonction utilitaire pour transformer un CSV en liste de listes."""
    try:
        with open(chemin, mode='r', encoding='utf-8') as f:
            return list(csv.reader(f))
    except FileNotFoundError:
        print(f"⚠️  Attention : Le fichier '{chemin}' est introuvable.")
        return []


def main():
    display_all_competitions = {
        "tennis atp": ["Brisbane", "United Cup","Hong Kong",
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
        "tennis wta":["United Cup","Brisbane","Auckland","Adelaide","Hobart",
                        "Australian Open","Hua Hin","Linz","Abu Dhabi","Cluj-Napoca",
                        "Doha","Dubai","Austin","San Diego","Indian Wells","Miami",
                        "Bogota","Charleston","Rouen","Stuttgart","Madrid","Rome",
                        "Rabat","Strasbourg""Roland Garros","Hertogenbosch","Nottingham",
                        "Berlin","Birmingham","Bad Homburg","Eastbourne","Wimbledon",
                        "Budapest","Palermo","Iasi","Prague","Paris Olympics","Washington",
                        "Toronto","Cincinnati","Cleveland","Monterrey","Us Open",
                        "Guadalajara","Monastir","Hua Hin 2","Seoul","Beijing","Wuhan",
                        "Ningbo","Osaka","Guangzhou","Tokyo","Hong Kong","Jiujiang","Merida",
                        "Riyadh Finals","Buenos Aires","BJK Cup Qualifiers","BJK Cup Finals",
                        "BJK Cup Playoffs"],     
        "football": ["Ligue des champions", "Jupiler League", 
                    "Premier League", "Ligue 1", "Bundesliga", 
                    "Serie A", "Eredivisie", "Ekstraklasa", 
                    "Liga ZON Sagres","Scotland Premier League", 
                    "LIGA BBVA", "Super League"],
        "badminton": ["JO 2024 Homme", "JO 2024 Femme"],
        "basketball": ["regular", "play-off"],
        "échecs": ["Coupe du Monde d'échecs de la FIDE"],
        "counter strike 2": ["Major d'hiver 2025"],
        "league of legends": ["LEC Winter Split 2025"],
        "starcraft 2": ["Global StarCraft II League 2016"],
        "volleyball":["Homme", "Femme"]
    }
    
    supported_sports = list(display_all_competitions.keys())

    # Choix du sport
    print(f"Sports disponibles : {', '.join(supported_sports)}")
    selected_sport = input("Sélectionnez un sport : \n> ").lower()

    if selected_sport not in supported_sports:
        raise Exception(f"Le sport '{selected_sport}' n'est pas supporté.")

    # Choix de la competition
    competitions_possibles = display_all_competitions[selected_sport]
    print(f"\nCompétitions disponibles pour {selected_sport} :")
    for i, comp in enumerate(competitions_possibles, 1):
        print(f"{i}. {comp}")

    selected_competition = input("\nSélectionnez une compétition (entrez son nom exact) : \n> ")

    if selected_competition not in competitions_possibles:
        raise Exception(f"La compétition '{selected_competition}' n'existe pas pour ce sport.")

    print(f"\n⏳ Chargement des données pour '{selected_competition}' en cours...")

    # Chargement des données
    data_path = "data/" 
    base_donnees = None

    if selected_sport == "football":
        if selected_competition == "Ligue des champions":
            players = charger_csv_liste(f"{data_path}football_champions_league/player.csv")
            matches = charger_csv_liste(f"{data_path}football_champions_league/match.csv")
            teams = charger_csv_liste(f"{data_path}football_champions_league/team.csv")
            base_donnees = parse_football_cl(players, matches, teams, selected_competition)
        else:
            base_donnees = parse_foot_el(f"{data_path}football_european_leagues", selected_competition)
    
    elif selected_sport == "basketball":
        players = charger_csv_liste(f"{data_path}basketball/player.csv")
        games = charger_csv_liste(f"{data_path}basketball/game.csv")
        teams = charger_csv_liste(f"{data_path}basketball/team.csv")
        base_donnees = parse_basket(players, games, teams, selected_competition)

    elif selected_sport == "tennis atp":
        players = charger_csv_liste(f"{data_path}tennis/atp_players_2024.csv")
        matches = charger_csv_liste(f"{data_path}tennis/atp_matches_2024.csv")
        base_donnees = parse_tennis(players, matches, selected_competition)

    elif selected_sport == "tennis wta":
        players = charger_csv_liste(f"{data_path}tennis/wta_players_2024.csv")
        matches = charger_csv_liste(f"{data_path}tennis/wta_matches_2024.csv")
        base_donnees = parse_tennis(players, matches, selected_competition)

    elif selected_sport == "volleyball":
        countries = charger_csv_liste(f"{data_path}volleyball/country.csv")

        if "femme" in selected_competition.lower():
            players = charger_csv_liste(f"{data_path}volleyball/player_women.csv")
            coaches = charger_csv_liste(f"{data_path}volleyball/coach_women.csv")
            matches = charger_csv_liste(f"{data_path}volleyball/match_women.csv")
        else:
            players = charger_csv_liste(f"{data_path}volleyball/player_men.csv")
            coaches = charger_csv_liste(f"{data_path}volleyball/coach_men.csv")
            matches = charger_csv_liste(f"{data_path}volleyball/match_men.csv")
        base_donnees = parse_volley(players, coaches, matches, countries, selected_competition)


    elif selected_sport == "league of legends":
        players = charger_csv_liste(f"{data_path}league_of_legends/player.csv")
        coaches = charger_csv_liste(f"{data_path}league_of_legends/coach.csv")
        matches = charger_csv_liste(f"{data_path}league_of_legends/match.csv")
        teams = charger_csv_liste(f"{data_path}league_of_legends/team.csv")
        base_donnees = parse_LoL(players, coaches, matches, teams, selected_competition)

    elif selected_sport == "badminton":
        players = charger_csv_liste(f"{data_path}badminton/player.csv")
        matches = charger_csv_liste(f"{data_path}badminton/match.csv")
        base_donnees = parse_badminton(players, matches, selected_competition)

    elif selected_sport == "échecs":
        players = charger_csv_liste(f"{data_path}chess/player.csv")
        matches = charger_csv_liste(f"{data_path}chess/match.csv")
        base_donnees = parse_chess(players, matches, selected_competition)

    elif selected_sport == "counter strike 2":
        players = charger_csv_liste(f"{data_path}counter_strike_2/player.csv")
        coachs = charger_csv_liste(f"{data_path}counter_strike_2/coach.csv")
        matchs = charger_csv_liste(f"{data_path}counter_strike_2/match.csv")
        teams = charger_csv_liste(f"{data_path}counter_strike_2/team.csv")
        base_donnees = parse_CS2(players, coachs, matchs, teams, selected_competition)

    elif selected_sport == "starcraft 2":
        players = charger_csv_liste(f"{data_path}starcraft_2/player.csv")
        matches = charger_csv_liste(f"{data_path}starcraft_2/match.csv")
        base_donnees = parse_starcraft2(players, matches, selected_competition)


    if base_donnees is None:
        print("❌ Erreur : Les données n'ont pas pu être chargées.")
        return

    # Analyse et affichage
    analyseur = Analyseur(base_donnees)
    
    print("\n✅ Données chargées!")
    print("--------------------------------------------------")
    
    analyseur.afficher_resultats_competition(selected_competition)

    # Recherche de joueur à la fin
    nom_j = input("\n🔍 Entrez le nom d'un joueur pour voir ses stats (ou 'exit' pour quitter) : ")
    if nom_j.lower() != 'exit':
        resultat = analyseur.rechercher_joueur(nom_j)
        print("\n--- Résultat de la recherche ---")
        print(resultat)

if __name__ == "__main__":
    main()
'''