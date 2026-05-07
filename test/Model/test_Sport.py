import pytest

from .Sport import Sport


def test_sport_init_valide() -> None:
    """Vérifie que le sport se crée bien avec ses informations."""
    sport = Sport(nom="Football", taille_equipe=11)

    assert sport.nom_sport == "Football"
    assert sport.taille_equipe == 11


def test_sport_basket() -> None:
    """Vérifie la création d'un autre sport."""
    sport = Sport(nom="Basketball", taille_equipe=5)

    assert sport.nom_sport == "Basketball"
    assert sport.taille_equipe == 5


def test_sport_erreurs_types() -> None:
    """Vérifie que la classe refuse les mauvais types de données."""
    
    # Erreur : le nom n'est pas une chaîne de caractères
    with pytest.raises(TypeError):
        Sport(nom=123, taille_equipe=11)

    # Erreur : la taille de l'équipe n'est pas un nombre entier
    with pytest.raises(TypeError):
        Sport(nom="Football", taille_equipe="Onze")