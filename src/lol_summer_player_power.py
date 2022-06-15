import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
# %matplotlib inline
import collections

df=pd.read_excel('start_2022_season.xlsx')
def create_player_rankings(df):
    top_dict={}
    jg_dict={}
    mid_dict={}
    adc_dict={}
    sup_dict={}
    dicts=[top_dict,jg_dict,mid_dict,adc_dict,sup_dict]
    teams=['TL','TSM','C9','100T','EG','IMT','GGS','CLG','DIG','FLY']
    team_dict=collections.defaultdict(list)
    for (col, data) in df.iteritems():
        if col.startswith('Top'):
            top_dict[col]=data
        if col.startswith('Jungle'):
            jg_dict[col]=data
        if col.startswith('Mid'):
            mid_dict[col]=data
        if col.startswith('ADC'):
            adc_dict[col]=data
        if col.startswith('SUP'):
            sup_dict[col]=data
    top_df=pd.DataFrame.from_dict(top_dict)
    jg_df=pd.DataFrame.from_dict(jg_dict)
    mid_df=pd.DataFrame.from_dict(mid_dict)
    adc_df=pd.DataFrame.from_dict(adc_dict)
    sup_df=pd.DataFrame.from_dict(sup_dict)
    dfs=[top_df,jg_df, mid_df, adc_df, sup_df]
    average=[]

    for pos in dfs:
        pos.rename(index={0:'Johann', 1: 'Milad', 2: 'Tak', 3: 'Joimes', 4:'Zain'}, inplace=True)
        pos.loc['Average Rank']=df.mean()
        pos.loc['Highest']=df.max()
        pos.loc['Lowest']=df.min()
        pos.reset_index(inplace=True)
        pos.rename(columns={'index': 'Name'}, inplace=True)
        s=pos.iloc[4]
        s.drop(s.index[0], inplace=True)
        s.sort_values(ascending=True, inplace=True)
        average.append(s)

    for df in dfs:
        df.set_index(['Name'], inplace=True)
        df=df.T
        df.sort_values('Average Rank', inplace=True)
        print(df.to_markdown( headers='keys'))
    return dfs

# dfs=create_player_rankings(df)
# def get_player_rankings_by_team():
#     final_dict= collections.defaultdict(list,keys=teams)
#     for team in teams:
#         for pos in dicts:
#             for key, value in pos.items():
#                     if team in key:
#                         team_dict[team].append((key,value))
#     for team in team_dict:
#         player=team_dict[team][0][1].mean()
#         final_dict[team].append(player)
#     return final_dict





