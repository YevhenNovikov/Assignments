import pandas as pd

url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv'
df = pd.read_csv(url)


teams_more_than_six_goals = df[df['Goals'] > 6]

teams_more_than_six_goals