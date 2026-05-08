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


print("Application projet traitement de données groupe 56".center(150, '+'))
print("En tout moment, vous pouvez quittez l'application en tapant 'quit' (avec ou sans majuscules) pour quitter")
print("De même, la commande back permet de revenir au menu précédent")
print("/!\ La lecture de base de données peut rencontrer des erreurs si les csv ont des données manquantes")
input('> Appuyez sur Entrée pour continuer \n')

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
            print("Sélectionnez un sport".center(150, '-'))
            choix = []
            for i in range(len(sport_supportes)):
                choix.append(str(i))
                print(f"[{i}] {sport_supportes[i].nom_sport}")
            requete = input()
            if requete in choix:
                sport_selection = int(requete)
                menu += '/dossier'
        if menu == 'principal/charger/dossier':
            print("Sélectionnez une base de données".center(150, '-'))
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
            print("Sélectionnez une base de données".center(150, '-'))
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
        if menu == 'principal/lire/base/competitions':
            choix = []
            for i in range(len(donnees_chargees[base_choisie].competitions)):
                choix.append(str(i))
                print(f"[{i}] {donnees_chargees[base_choisie].competitions[i].nom}")
            requete = input()
            if requete in choix:
                print(donnees_chargees[base_choisie].competitions[int(requete)].nom.center(150, '-'))
                for m in donnees_chargees[base_choisie].competitions[int(requete)].matchs:
                    nom = f"{m.equipe_1.nom} - {m.equipe_2.nom}"
                    print(nom.center(150, '-'))
                    print(f"round : {m.round}")
                    print(f"best of : {m.best_of}")
                    print(f"date : {m.date}")
                    print(f"{m.equipe_1.nom} : {m.score_1}")
                    print(f"{m.equipe_2.nom} : {m.score_2}")
                    print(f"statistiques : {m.stats}")
    else:
        menu = menu[:- len(menu.split('/')[-1]) - 1]
        requete = ''
