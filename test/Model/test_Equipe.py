import pytest
from datetime import date

from .Equipe import Equipe


def test_equipe_init_valide() -> None:
    """Vérifie que l'équipe stocke bien les informations de base."""
    equipe = Equipe("Paris SG", ["Joueur 1", "Joueur 2"], abrev="PSG")

    assert equipe.nom == "Paris SG"
    assert equipe.abrev == "PSG"
    assert equipe.joueurs == ["Joueur 1", "Joueur 2"]
    assert equipe.surnom is None


def test_equipe_str() -> None:
    """Vérifie l'affichage simple de l'équipe."""
    equipe = Equipe("Paris SG", [])
    
    # __str__ doit renvoyer juste le nom
    assert str(equipe) == "Paris SG"


def test_equipe_repr() -> None:
    """Vérifie la représentation technique de l'équipe."""
    equipe = Equipe("Olympique Lyonnais", ["J1"], id=1, abrev="OL")
    
    # Le __repr__ renvoie une grande chaîne de caractères. 
    # On vérifie juste qu'elle contient bien les éléments clés sans erreur.
    representation = repr(equipe)
    assert "Equipe(" in representation
    assert "Olympique Lyonnais" in representation
    assert "OL" in representation


def test_equipe_ajouter_joueur() -> None:
    """Vérifie que la méthode ajouter_joueur fonctionne bien."""
    equipe = Equipe("Real Madrid", ["Joueur 1"])
    
    equipe.ajouter_joueur("Joueur 2")
    
    # La liste doit maintenant contenir 2 joueurs
    assert equipe.joueurs == ["Joueur 1", "Joueur 2"]


def test_equipe_ajouter_coach() -> None:
    """Vérifie que la méthode ajouter_coach range le coach au bon endroit."""
    equipe = Equipe("Chelsea", ["Joueur 1"], coachs=[])
    
    equipe.ajouter_coach("Coach 1")
    
    # Le coach doit être dans la liste des coachs
    assert equipe.coachs == ["Coach 1"]
    
    # Et on vérifie qu'il n'a PAS été ajouté aux joueurs par erreur !
    assert equipe.joueurs == ["Joueur 1"]


def test_equipe_erreurs_types() -> None:
    """Vérifie que la classe refuse les mauvais types de données."""
    
    # Erreur : le nom est un entier au lieu d'une chaîne de caractères
    with pytest.raises(TypeError):
        Equipe(123, [])

    # Erreur : les joueurs sont une chaîne de caractères au lieu d'une liste
    with pytest.raises(TypeError):
        Equipe("Arsenal", "Ceci n'est pas une liste")