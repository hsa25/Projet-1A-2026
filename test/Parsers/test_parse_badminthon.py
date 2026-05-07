import pytest
from src.parsers.badminton import parse_badminton

def test_parse_badminton_valide():
    """Vérifie que le parser lit correctement les données factices."""

    test_equipes = [
        ["nom", "region_small", "region_big"],
        ["Viktor Axelsen", "EUR", "Denmark"],
        ["Kento Momota", "ASI", "Japan"]
    ]

    test_matchs = [
        ["nom_comp", "ville", "pays", "date", "type", "round", "eq1", "eq2", "vide", "s1", "s2", "s3"],
        ["BWF World Champ", "Paris", "France", "2024-08-05", "WC", "Final", "Viktor Axelsen", "Kento Momota", "", "21-18", "19-21", "21-15"]
    ]

    base = parse_badminton(test_equipes, test_matchs, "Test_Badminton")

    assert base._Base__nom == "Test_Badminton"
    assert base._Base__sport.nom_sport == "Badminton"
    
    assert len(base._Base__equipes) == 2
    assert base._Base__equipes[0].nom == "Viktor Axelsen"
    assert base._Base__equipes[0].region_big == "Denmark"
    
    assert len(base._Base__competitions) == 1
    comp = base._Base__competitions[0]
    assert comp._Competition__nom == "BWF World Champ"
    assert comp._Competition__ville == "Paris"
    
    assert len(comp._Competition__matchs) == 1
    match = comp._Competition__matchs[0]
    
    assert match._Match__score_1 == [21, 19, 21]
    assert match._Match__score_2 == [18, 21, 15]