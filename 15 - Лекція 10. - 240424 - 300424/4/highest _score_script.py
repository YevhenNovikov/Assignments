import csv


data = []
with open('players_scores.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append({'Player name': row['Player name'], 'Score': row['Score']})


max_scores = {}

for row in data:
    name = row['Player name']
    score = row['Score']
    if name in max_scores:
        max_scores[name] = max(max_scores[name], score)
    else:
        max_scores[name] = score


with open('high_scores.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Player name', 'Highest score'])
    for name, score in sorted(max_scores.items(), key=lambda x: x[1], reverse=True):
        writer.writerow([name, score])