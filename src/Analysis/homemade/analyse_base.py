from .Model.Base import Base
from .Model.Competition import Competition
from .Model.Equipe import Equipe

class Analyseur:

    def __init__(self, base: Base):
        self.base = base

    def lister_competitions(self) -> list[str]:
        """Retourne la liste des noms de toutes les compétitions pour cette base (ce sport)."""
        return [comp._Competition__nom for comp in self.base._Base__competitions]

    def afficher_resultats_competition(self, nom_competition: str) -> None:
        """Affiche dans la console tous les matchs d'une compétition."""
        for comp in self.base._Base__competitions:
            if comp._Competition__nom == nom_competition:
                print(f"--- Résultats pour {nom_competition} ({self.base._Base__sport}) ---")
                for match in comp._Competition__matchs:
                    eq1 = match._Match__equipe_1.nom if match._Match__equipe_1 else "Inconnu"
                    eq2 = match._Match__equipe_2.nom if match._Match__equipe_2 else "Inconnu"
                    score1 = match._Match__score_1
                    score2 = match._Match__score_2
                   
                    print(f"{match._Match__date} | {eq1} {score1} - {score2} {eq2}")
                return
      
        print(f"Compétition '{nom_competition}' introuvable.")

    def rechercher_joueur(self, nom_joueur: str) -> dict:
        """
        Cherche un joueur par son nom et renvoie sa fiche technique (informations et statistiques).
        """
        for equipe in self.base._Base__equipes:
            for joueur in equipe.joueurs:
                if nom_joueur.lower() in joueur.nom.lower():
                    return {
                        "equipe": equipe.nom,
                        "joueur": joueur.nom,
                        "role": joueur.role,
                        "stats": joueur.statistiques
                    }
        return {"erreur": "Joueur introuvable"}

    def matchs_par_equipe(self, nom_equipe: str) -> list:
        """Retourne tous les matchs joués par une équipe."""
        matchs_trouves = []
        for comp in self.base._Base__competitions:
            for match in comp._Competition__matchs:
                eq1 = match._Match__equipe_1
                eq2 = match._Match__equipe_2
                
                if (eq1 and eq1.nom.lower() == nom_equipe.lower()) or \
                   (eq2 and eq2.nom.lower() == nom_equipe.lower()):
                    matchs_trouves.append(match)
        return matchs_trouves