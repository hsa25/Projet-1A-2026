from src.Common.utils import print_timings
import csv


@print_timings
def parse_players_csv(filepath: str, sep: str = ";") -> list:
    liste = []
    with open(filepath, 'r') as file:
        reader = csv.reader(file, delimiter=sep)
        for row in reader:
            liste.append(row)
    return liste
