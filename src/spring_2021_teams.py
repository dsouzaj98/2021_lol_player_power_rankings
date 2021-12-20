import pandas as pd

res=pd.read_excel('data/LCS_team_predictions.xlsx')

new_cols=dict(keys=res.columns)
res.columns = res.columns.str.replace("Rank the team's performance in spring split", "")


df=res.copy()
df.drop(columns='Timestamp', axis=1, inplace=True)

df.set_index(['Name'], inplace=True)

df.loc['Average Rank']=df.mean()
df.loc['Highest']=df.max()
df.loc['Lowest']=df.min()
df=df.round(2)
df=df.T
df.sort_values('Average Rank', axis=0, inplace=True)
print(df.to_markdown())
