from lol_spring_player_power import create_player_rankings
from lol_spring_player_power import df
import pandas as pd
import numpy as np

old_dfs=create_player_rankings(df)

new_df=pd.read_excel('mid_season.xlsx')
x=create_player_rankings(new_df)
def test_round(list_of_pos):
    for pos in list_of_pos:
        pos=pos.round(2)
        pos=pos.rename(index={5: 'Kwan'})
        breakpoint()
    return list_of_pos
