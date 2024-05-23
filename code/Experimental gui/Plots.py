import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

df = pd.read_csv('organism_database_20240428124116.csv')

print(df.head())
# Calculate the lifespan of each organism
df['Lifespan'] = df['Death time (milsec)'] - df['Birth time (milsec)']
print(df['Lifespan'])
print(df.columns)

# Sort the dataframe by lifespan in descending order and select the top 10 organisms
top_10_longest_lived = df.sort_values('Lifespan', ascending=False).head(10)

# Plot a bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x=top_10_longest_lived.index, y=top_10_longest_lived['Plants killed'], palette='viridis')
plt.xlabel('Organism ID')
plt.ylabel('Number of Plants Killed')
plt.title('Top 10 Longest Lived Organisms and the Number of Plants They Killed')
plt.savefig('plot.png')