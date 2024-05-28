import pandas as pd

url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv'
df = pd.read_csv(url)

selected_columns = df[['Team', 'Yellow Cards', 'Red Cards']]


selected_columns