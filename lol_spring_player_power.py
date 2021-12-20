import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from tabulate import tabulate
# %matplotlib inline

df=pd.read_excel('test rankings.xlsx')

top_dict={}
jg_dict={}
mid_dict={}
adc_dict={}
sup_dict={}
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
    pos.rename(index={0:'Johann', 1: 'Milad', 2: 'Tak', 3: 'Joimes'}, inplace=True)
    pos.loc['average rank']=df.mean()
    pos.reset_index(inplace=True)
    pos.rename(columns={'index': 'Name'}, inplace=True)
    s=pos.iloc[4]
    s.drop(s.index[0], inplace=True)
    s.sort_values(ascending=True, inplace=True)
    average.append(s)

for df in dfs:
    print(tabulate(df, headers='keys'))

