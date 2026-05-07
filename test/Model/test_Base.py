import pytest

from .Base import Base


def test_base_init_valide() -> None:
    """Vérifie que la base stocke bien les infos qu'on lui donne."""
    
    base = Base("Ligue 1", "Football", ["Comp1", "Comp2"], ["PSG", "OM"])

    assert base._Base__nom == "Ligue 1"
    assert base._Base__sport == "Football"
    assert base._Base__competitions == ["Comp1", "Comp2"]
    assert base._Base__equipes == ["PSG", "OM"]


def test_base_nom_invalide() -> None:
    """Vérifie que le nom doit absolument être du texte."""
    
    with pytest.raises(TypeError):
        Base(123, "Football", [], [])  # 123 n'est pas du texte


def test_base_listes_invalides() -> None:
    """Vérifie que les compétitions et équipes doivent être des listes."""
    
    # Erreur sur les compétitions (un mot au lieu d'une liste)
    with pytest.raises(TypeError):
        Base("Ligue 1", "Football", "Ceci n'est pas une liste", [])

    # Erreur sur les équipes (un tuple au lieu d'une liste)
    with pytest.raises(TypeError):
        Base("Ligue 1", "Football", [], ("EQ1", "EQ2"))