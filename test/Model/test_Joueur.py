import pytest
from datetime import date

from .Joueur import Joueur


def test_joueur_init_minimal() -> None:
    """Vérifie que le joueur se crée bien avec juste son nom."""
    joueur = Joueur("Kylian Mbappé")
    
    assert joueur.nom == "Kylian Mbappé"
    assert joueur.taille is None
    assert joueur.role is None
    assert joueur.statistiques is None
    assert joueur.id is None


def test_joueur_init_complet() -> None:
    """Vérifie que tous les paramètres sont correctement enregistrés."""
    stats = {"buts": 250, "passes": 100}
    naissance = date(1987, 6, 24)
    
    joueur = Joueur(
        nom="Lionel Messi",
        id=10,
        date_naissance=naissance,
        taille=1.70,
        poids=70.0,
        role="Attaquant",
        pseudo="10",
        genre="Masculin",
        statistiques=stats,
        nationalite="Argentine"
    )

    assert joueur.nom == "Lionel Messi"
    assert joueur.id == 10
    assert joueur.date_naissance == naissance
    assert joueur.taille == 1.70
    assert joueur.poids == 70.0
    assert joueur.role == "Attaquant"
    assert joueur.pseudo == "10"
    assert joueur.genre == "Masculin"
    assert joueur.statistiques == stats
    assert joueur.nationalite == "Argentine"


def test_joueur_str() -> None:
    """Vérifie l'affichage simple du joueur."""
    joueur = Joueur("Zinedine Zidane")
    assert str(joueur) == "Zinedine Zidane"


def test_joueur_repr() -> None:
    """Vérifie la représentation technique du joueur."""
    joueur = Joueur("Antoine Griezmann", id=7, role="Attaquant")
    
    representation = repr(joueur)
    assert "Attaquant" in representation


def test_joueur_egalite() -> None:
    """Vérifie que deux joueurs sont considérés égaux s'ils ont le même ID."""
    j1 = Joueur("Joueur A", id=99)
    j2 = Joueur("Joueur B", id=99) 
    j3 = Joueur("Joueur A", id=100) 
    
    assert j1 == j2
    assert j1 != j3


def test_joueur_egalite_erreur() -> None:
    """Vérifie que la comparaison avec un autre type d'objet lève une erreur."""
    joueur = Joueur("Test", id=1)
    
    with pytest.raises(TypeError):
        joueur == "Ceci n'est pas un joueur"