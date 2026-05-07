import pytest

from .Competition import Competition


def test_competition_init_valide() -> None:
    """Vérifie que la compétition se crée bien avec les infos obligatoires."""
    # On donne juste un nom et une petite liste (qui simule les matchs)
    comp = Competition("Ligue 1", ["Match 1", "Match 2"])

    # On utilise _Competition__ car les attributs sont privés et sans @property
    assert comp._Competition__nom == "Ligue 1"
    assert comp._Competition__matchs == ["Match 1", "Match 2"]
    
    # Vérifie que les valeurs optionnelles par défaut sont bien None
    assert comp._Competition__ville is None
    assert comp._Competition__pays is None


def test_competition_init_complet() -> None:
    """Vérifie que tous les paramètres optionnels sont bien stockés."""
    comp = Competition(
        nom="Roland-Garros",
        matchs=[],
        ville="Paris",
        pays="France",
        type="Tournoi",
        id="RG2024",
        nombre_participants=128
    )

    assert comp._Competition__ville == "Paris"
    assert comp._Competition__pays == "France"
    assert comp._Competition__type == "Tournoi"
    assert comp._Competition__id == "RG2024"
    assert comp._Competition__nombre_participants == 128


def test_competition_ajouter_match() -> None:
    """Vérifie que la méthode ajouter_match fonctionne correctement."""
    comp = Competition("Premier League", ["Match 1"])
    
    comp.ajouter_match("Match 2")
    
    # La liste doit maintenant contenir 2 matchs
    assert comp._Competition__matchs == ["Match 1", "Match 2"]


def test_competition_erreurs_types() -> None:
    """Vérifie que la classe refuse les mauvais types de données."""
    
    # ⚠️ Pour que ce test passe au vert, n'oublie pas de rajouter 
    # les sécurités (if not isinstance...) dans ton __init__ !
    
    # Erreur : le nom est un entier au lieu d'une chaîne de caractères
    with pytest.raises(TypeError):
        Competition(123, [])

    # Erreur : les matchs sont fournis sous forme de texte au lieu d'une liste
    with pytest.raises(TypeError):
        Competition("Ligue 1", "Ceci n'est pas une liste")