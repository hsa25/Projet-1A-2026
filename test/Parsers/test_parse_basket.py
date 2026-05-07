import pytest
from src.parsers.basket import parse_basket

def test_parse_basket_valide():
    """Vérifie que le parser de basketball lit et structure correctement les données de test."""
    
    # 1. Création des données de test
    test_equipes = [
        ["id", "nom", "abrev", "surnom", "region_small", "region_big"],
        ["1", "Los Angeles Lakers", "LAL", "Lakers", "LA", "Los Angeles"],
        ["2", "Boston Celtics", "BOS", "Celtics", "BOS", "Boston"]
    ]

    test_joueurs = [
        ["id", "prenom", "nom", "naissance", "taille", "poids", "pseudo", "role", "id_equipe"],
        ["10", "LeBron", "James", "1984-12-30", "206", "113", "King James", "SF", "1"],
        ["11", "Jayson", "Tatum", "1998-03-03", "203", "95", "JT", "SF", "2"]
    ]

    test_matchs = [
        ["comp", "type", "id_e1", "id_match", "date", "duree", 
         "fgm1","fga1","fg_pct1","fg3m1","fg3a1","fg3_pct1","ftm1","fta1","ft_pct1","oreb1","dreb1","reb1","ast1","stl1","blk1","tov1","pf1","score1",
         "id_e2",
         "fgm2","fga2","fg_pct2","fg3m2","fg3a2","fg3_pct2","ftm2","fta2","ft_pct2","oreb2","dreb2","reb2","ast2","stl2","blk2","tov2","pf2","score2"],
        ["NBA 2024", "Regular", "1", "42", "2024-01-15", "48", 
         "40", "85", "0.47", "12", "30", "0.40", "18", "22", "0.82", "10", "35", "45", "25", "8", "5", "12", "20", "110",
         "2", 
         "38", "80", "0.48", "10", "28", "0.36", "14", "18", "0.78", "8", "30", "38", "22", "7", "4", "15", "18", "100"]
    ]

    base = parse_basket(test_joueurs, test_matchs, test_equipes, "Test_NBA")

    
    assert base._Base__nom == "Test_NBA"
    assert base._Base__sport.nom_sport == "Basketball"
    
    assert len(base._Base__equipes) == 2
    lakers = base._Base__equipes[0]
    assert lakers.nom == "Los Angeles Lakers"
    assert lakers.abrev == "LAL"
    
    assert len(lakers.joueurs) == 1
    assert lakers.joueurs[0].nom == "LeBron James"
    assert lakers.joueurs[0].role == "SF"
    
    assert len(base._Base__competitions) == 1
    comp = base._Base__competitions[0]
    assert comp._Competition__nom == "NBA 2024"
    assert comp._Competition__type == "Regular"
    
    assert len(comp._Competition__matchs) == 1
    match = comp._Competition__matchs[0]
    assert match._Match__date == "2024-01-15"
    assert match._Match__equipe_1.nom == "Los Angeles Lakers"
    assert match._Match__equipe_2.nom == "Boston Celtics"
    
    stats = match._Match__stats
    assert stats['fgm'] == ["40", "38"]
    assert stats['ast'] == ["25", "22"]
    assert stats['score_1'] == "110"
    assert stats['score_2'] == "100"