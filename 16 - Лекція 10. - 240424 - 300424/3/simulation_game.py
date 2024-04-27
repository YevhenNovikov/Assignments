import csv


players = ["Josh", "Luke", "Kate", "Mark", "Mary"]

import random

with open('players_scores.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["Player name", "Score"])
    for _ in range(100):
        for player in players:
            score = random.randint(0, 1000)
            writer.writerow([player, score])