import pytest
from src.parsers.chess import parse_chess

def test_parse_chess_valide():
    """Vérifie que le parser d'échecs lit et structure correctement les données de test."""
    
    test_joueurs = [
        ["nom", "id", "naissance", "genre", "pays", "titre", "elo_std", "elo_rapide", "elo_blitz"],
        ["Magnus Carlsen", "1", "1990-11-30", "M", "Norway", "GM", "2839", "2820", "2886"],
        ["Fabiano Caruana", "2", "1992-07-30", "M", "USA", "GM", "2804", "2760", "2755"]
    ]

    test_matchs = [
        ["round", "groupe", "ordre", "j1", "j2", "s1", "s2", "seed1", "seed2"],
        ["1", "A", "1", "Magnus Carlsen", "Fabiano Caruana", "1", "0", "1.0", "2.0"]
    ]

    base = parse_chess(test_joueurs, test_matchs, "Test_Chess")

    assert base._Base__nom == "Test_Chess"
    assert base._Base__sport.nom_sport == "Échecs"
    
    assert len(base._Base__equipes) == 2
    carlsen_team = base._Base__equipes[0]
    assert carlsen_team.nom == "Magnus Carlsen"
    assert carlsen_team.region_big == "Norway"
    
    joueur_carlsen = carlsen_team.joueurs 
    assert joueur_carlsen.nom == "Magnus Carlsen"
    assert joueur_carlsen.id == 1
    assert joueur_carlsen.role == "GM"
    
    stats_carlsen = joueur_carlsen.statistiques
    assert stats_carlsen['elo_standard'] == "2839"
    assert stats_carlsen['elo_blitz'] == "2886"
    
    assert len(base._Base__competitions) == 1
    comp = base._Base__competitions[0]
    assert comp._Competition__nom == "Test_Chess"
    
    assert len(comp._Competition__matchs) == 1
    match = comp._Competition__matchs[0]
    assert match._Match__round == "1"
    assert match._Match__equipe_1.nom == "Magnus Carlsen"
    assert match._Match__equipe_2.nom == "Fabiano Caruana"
    
    assert match._Match__score_1 == [1]
    assert match._Match__score_2 == [0]
    
    assert match._Match__stats['seed_joueur_1'] == 1.0
    assert match._Match__stats['seed_joueur_2'] == 2.0